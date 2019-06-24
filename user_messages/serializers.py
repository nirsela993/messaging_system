from rest_framework import serializers
from rest_framework.fields import BooleanField
from rest_framework.relations import SlugRelatedField

from user_messages.models import Message
from users.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    receiver = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    unread = BooleanField(default=True)

    class Meta:
        model = Message
        read_only_fields = ['creation_date']
