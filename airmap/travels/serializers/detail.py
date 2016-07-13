from rest_framework import serializers
from travels.models import travel


class DetailModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = travel
        fields = [
                "creation_data",
                "latitude",
                "longitude",
                "country",
                "city".
                ]
