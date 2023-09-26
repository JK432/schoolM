from rest_framework import viewsets
from . import models
from rest_framework.request import Request
from rest_framework.decorators import api_view
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . import permissions
from django.http import HttpRequest, JsonResponse
from django.db import IntegrityError

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
    roll = 'noroll'
    userdata = models.Teacher
    try:
        userdata = models.Teacher.objects.get(user=user)
        roll = 'teacher'
        # If the teacher instance exists, you can do something with it
    except models.Teacher.DoesNotExist:
        pass
    try:
        userdata = models.Student.objects.get(user = user)
        roll = 'student'
        # If the teacher instance exists, you can do something with it
    except models.Student.DoesNotExist:

        pass

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,'roll':roll,'userid':userdata.id},
                    status=status.HTTP_200_OK)




@csrf_exempt
@api_view(['POST'])
def teachersignup(request: HttpRequest):
    username = request.data.get("username")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    if username is None and password is None and password2 is None:
        return Response({'error': 'Please provide user & password & password2'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.create_user(password=password,username=username)
        user.set_password(password)
        user.save()
        teacher = models.Teacher(user=user,name = username)
        teacher.save()

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,'roll':'teacher','id':teacher.id},
                    status=status.HTTP_200_OK)

    except IntegrityError:
        return Response({'error': 'Already Taken'},
                        status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
@api_view(['POST'])
def studentsignup(request: HttpRequest):
    username = request.data.get("username")
    password = request.data.get("password")
    password2 = request.data.get("password2")
    if username is None and password is None and password2 is None:
        return Response({'error': 'Please provide user & password & password2'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.create_user(password=password,username=username)
        user.set_password(password)
        user.save()
        student = models.Student(user=user,name = username)
        student.save()

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,'roll':'student','id':student.id},
                    status=status.HTTP_200_OK)

    except IntegrityError:
        return Response({'error': 'Already Taken'},
                        status=status.HTTP_404_NOT_FOUND)





class SubjectViewSetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer
    queryset = models.Subject.objects.all()
    permission_classes = [IsAuthenticated,permissions.TeachersOwnSubject]

class TeacherViewsetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [IsAuthenticated]

class MarkViewsetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.MarkSerializer
    queryset = models.Mark.objects.all()
    permission_classes = [IsAuthenticated]

class StudentViewsetTeacher(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    permission_classes = [IsAuthenticated]



class StudentViewsetStudent(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    permission_classes = [IsAuthenticated]

class MarkViewsetStudent(viewsets.ModelViewSet):
    serializer_class = serializers.MarkSerializer
    queryset = models.Mark.objects.all()
    permission_classes = [IsAuthenticated]

class SubjectViewSetStudent(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer
    queryset = models.Subject.objects.all()
    permission_classes = [IsAuthenticated]