from django.db import models

from .travel import Travel


class ImageMetaData(models.Model):

    travel = models.ForeignKey(Travel)

    latitude = models.CharField(
        max_length=256,
    )
    longitude = models.CharField(
        max_length=256,
    )
    country = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
    )

    image = models.ImageField(
    )

#    thumbnail_image = models.ImageField(
#        blank=True,
#        null=True,
#    )

#    image_url = models.URLField(
#        blank=True,
#        null=True,
#    )

#    thumbnail_image_url = models.URLField(
#        blank=True,
#        null=True,
#    )

    timestamp = models.CharField(
        max_length=256,
    )

    creation_date = models.DateTimeField()
#    timezone_date = models.DateTimeField()
