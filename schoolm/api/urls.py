from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .Views import login, super_signup, normal_signup, TeacherSubjectAverageMarkViewSet
from . import views

teacher = DefaultRouter()

# teacher.register(r"subjects", views.SubjectViewSetTeacher)
# teacher.register(r"profile", views.TeacherViewsetTeacher)
# teacher.register(r"mark", views.MarkViewsetTeacher)
# teacher.register(r"students", views.StudentViewsetTeacher)

student = DefaultRouter()

# student.register(r"subjects", views.SubjectViewSetStudent)
# student.register(r"profile", views.StudentViewsetStudent)
# student.register(r"mark", views.MarkViewsetStudent)

app_name = 'api'
urlpatterns = [
    path("login/", login),
    path("teachers/signup/", super_signup),
    path("students/signup/", normal_signup),
    # path("teachers/", include((teacher.urls, 'teacher'))),
    # path("students/", include((student.urls, 'student')))
]
