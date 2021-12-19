from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_answered = models.BooleanField(default=False)


    class Meta:
        db_table = 'auth_user'
