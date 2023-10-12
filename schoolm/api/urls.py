from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .Views import *
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'register', UserModelViewSet)
router.register(r'subject', SubjectModelViewSet)
# router.register(r'login',views.obtain_auth_token,basename="login")

app_name = 'api'
urlpatterns = [
    path('login/', views.obtain_auth_token, name="login"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]