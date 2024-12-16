
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

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

            if User.objects.filter(username=email).exists():
                return JsonResponse({'success': False, 'message': 'Email is already taken!'}, status=400)

            user = User.objects.create_user(
                username=email,  # Sử dụng email làm username
                password=password,
                first_name=full_name,
                last_name=display_name
            )
            return JsonResponse({'success': True, 'message': 'Account created successfully!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data!'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

def login_view(request):

    if request.method == 'GET':
        return render(request, 'auth/auth.html')

    if request.method == "POST":
        try:
            # Parse JSON request body
            data = json.loads(request.body.decode("utf-8"))
            username = data.get("username")
            password = data.get("password")

            # Kiểm tra username và password
            if not username or not password:
                return JsonResponse({"success": False, "message": "Username and password are required!"}, status=400)

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"success": True, "message": "Login successful!"}, status=200)

            return JsonResponse({"success": False, "message": "Invalid credentials!"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data!"}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=400)