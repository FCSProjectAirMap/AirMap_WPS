from django.db import models
from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    pass
