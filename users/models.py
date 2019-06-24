from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return "Email = {}".format(self.email)
