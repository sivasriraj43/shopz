from django.contrib.auth.Models import User

from rest_framework import viewsets

from .serializers import UserSerializer

class UserView(viewsets.ModeViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer