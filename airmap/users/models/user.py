from django.db import models
from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )
