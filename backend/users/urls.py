from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

app_name = 'users'

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
