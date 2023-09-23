from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views


teacher = DefaultRouter()
teacher.register(r"subjects", views.SubjectViewSetTeacher)
teacher.register(r"signup", views.TeacherViewsetTeacher)
teacher.register(r"mark", views.MarkViewsetTeacher)
teacher.register(r"students", views.StudentViewsetTeacher)



student = DefaultRouter()
student.register(r"subjects", views.SubjectViewSetStudent)
student.register(r"signup", views.StudentViewsetStudent)
student.register(r"mark", views.MarkViewsetStudent)

app_name = 'api'
urlpatterns = [
    path("login/", views.login),
    path("teachers/", include((teacher.urls, 'teacher'))),
    path("students/", include((student.urls, 'student')))
]
