from rest_framework import serializers
from rest_framework.fields import EmailField

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = EmailField()

    class Meta:
        model = User
        fields = ['email']
