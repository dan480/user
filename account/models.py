from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login=datetime.datetime.now()
    date_joined=datetime.date.today()
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
