
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from user.models import User


def generate_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#register
@csrf_exempt
def register_view(request):

    if request.method == 'GET':
        return render(request, 'auth/auth.html')

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            full_name = data.get('full_name')
            display_name = data.get('display_name')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')

            if password != confirm_password:
                return JsonResponse({'success': False, 'message': 'Passwords do not match!'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'Email is already taken!'}, status=400)

            user = User.objects.create_user(
                email=email,
                password=password,
                full_name=full_name,
                display_name=display_name
            )
            tokens = generate_tokens_for_user(user)

            return JsonResponse({'success': True, 'message': 'Account created successfully!', 'tokens': tokens}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data!'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)


#login
@csrf_exempt
def login_view(request):

    if request.method == 'GET':
        return render(request, 'auth/auth.html')

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"success": False, "message": "Email and password are required!"}, status=400)

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)

                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                tokens = {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                }

                response = JsonResponse({
                    "success": True,
                    "message": "Login successful!",
                    "redirect_url": reverse('home'),
                    "tokens": tokens,
                }, status=200)

                # Set tokens in HttpOnly cookies
                response.set_cookie(
                    key='access_token',
                    value=tokens['access'],
                    httponly=True,
                    secure=False,  # Set to True in production
                    samesite='Lax',
                )
                response.set_cookie(
                    key='refresh_token',
                    value=tokens['refresh'],
                    httponly=True,
                    secure=False,  # Set to True in production
                    samesite='Lax',
                )
                return response

            return JsonResponse({"success": False, "message": "Invalid credentials!"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data!"}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=400)
