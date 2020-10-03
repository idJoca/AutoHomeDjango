# serializers.py
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Name','CPF','Rg','Email','Password','PasswordHint')
