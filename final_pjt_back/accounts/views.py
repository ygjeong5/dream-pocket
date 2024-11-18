from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(['POST'])
# def signup(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = User.objects.filter(username=username).first()
    
#     if user and user.check_password(password):  # 비밀번호 검증
#         refresh = RefreshToken.for_user(user)  # 토큰 생성
#         access_token = str(refresh.access_token)

#         return Response({
#             'refresh': str(refresh),
#             'access': access_token
#         }, status=status.HTTP_200_OK)
    
#     return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateUserView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user  # 로그인한 사용자의 정보만 수정하도록 설정

    def perform_update(self, serializer):
        serializer.save()           # 사용자 정보 저장