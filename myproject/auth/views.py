from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from user.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        # Lưu người dùng và mã hóa mật khẩu
        user = serializer.save()
        user.set_password(request.data['password'])  # Mã hóa mật khẩu trước khi lưu
        user.save()  # Lưu thay đổi mật khẩu
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)  # Kiểm tra người dùng với email
        if user.check_password(password):  # Kiểm tra mật khẩu đã mã hóa
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
