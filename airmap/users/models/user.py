from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
