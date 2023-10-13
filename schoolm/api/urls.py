from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .Views import *
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'register', UserModelViewSet)
router.register(r'subject', SubjectModelViewSet)
router.register(r'mark', MarkModelViewSet,basename='mark')
app_name = 'api'
urlpatterns = [
    path('tocken/', obtain_auth_token, name="login"),
    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls')),

]

