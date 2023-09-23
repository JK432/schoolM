from rest_framework import viewsets
from . import models
from rest_framework.decorators import api_view
from . import serializers
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated,
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .permissions import TeachersOwnSubject

@csrf_exempt
@api_view(['POST'])

def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None and password is None:
        return Response({'error': 'Please provide user & password'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)




@csrf_exempt
@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    if username is None and password is None and password2 is None:
        return Response({'error': 'Please provide user & password & password2'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        username=username,password=password
    )
    user.set_password(password)
    user.save()

    if not user:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

    # token, _ = Token.objects.get_or_create(user=user)
    return Response({'user':user.id},
                    status=status.HTTP_200_OK)









class SubjectViewSetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer
    queryset = models.Subject.objects.all()
    # permission_classes = [IsAuthenticated,IsOwnSubject]

class TeacherViewsetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.all()

class MarkViewsetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.MarkSerializer
    queryset = models.Mark.objects.all()

class StudentViewsetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()




class StudentViewsetStudent(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

class MarkViewsetStudent(viewsets.ModelViewSet):
    serializer_class = serializers.MarkSerializer
    queryset = models.Mark.objects.all()

class SubjectViewSetStudent(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer
    queryset = models.Subject.objects.all()