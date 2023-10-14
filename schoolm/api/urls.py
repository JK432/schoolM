from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'register', StudentModelViewSet, basename='Student')
router.register(r'subject', SubjectModelViewSet)
router.register(r'mark', MarkModelViewSet, basename='mark')
app_name = 'api'
urlpatterns = [
    path('token/', obtain_auth_token, name="login"),
    path('', include(router.urls)),
]
