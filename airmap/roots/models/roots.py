from django.db import models

from users.models import User


class Title(models.Model):

    user = models.ForeignKey(User)

    title_name = models.CharField(
        max_length=120,
        null = False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_name


class File(models.Model):

    title = models.ForeignKey(Title)

    file_name = models.CharField(
        max_length=120,
    )

    latitudee = models.CharField(
        max_length=120,
    )
    longitude = models.CharField(
        max_length=120,
    )
    creation_date = models.DateTimeField()
