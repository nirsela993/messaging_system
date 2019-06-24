from django.db import models

from users.models import User


class Message(models.Model):

    sender = models.ForeignKey(User, related_name='sent_messages')

    receiver = models.ForeignKey(User, related_name='received_messages')

    message = models.CharField(max_length=200)

    subject = models.CharField(max_length=50)

    creation_date = models.DateTimeField(auto_now_add=True)

    unread = models.BooleanField(default=True)

    def read(self):
        self.unread = False
        self.save()
