# views.py
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('UserId')
    serializer_class = UserSerializer