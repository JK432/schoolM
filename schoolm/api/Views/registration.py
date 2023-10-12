# from ..Serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer, SuperUserRegistrationSerializer
# from django.contrib.auth import get_user_model
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.authtoken.models import Token
#
# User = get_user_model()
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     # FOR SUPERUSER REGISTRATION
#     @action(detail=False, methods=['post'])
#     def superregister(self, request):
#         serializer = SuperUserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 login(request, user)
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_200_OK)
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#     # FOR NORMAL REGISTRATION
#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 login(request, user)
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_200_OK)
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#     # FOR LOGIN
#     @action(detail=False, methods=['post'])
#     def login(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_200_OK)
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#     # FOR LOGOUT
#     @action(detail=False, methods=['get'])
#     def logout(self, request):
#         logout(request)
#         return Response({'detail': 'Logged out successfully'}, status=status.HTTP_200_OK)
