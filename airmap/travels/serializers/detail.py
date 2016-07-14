from rest_framework import serializers
from travels.models import Travel


class DetailModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = [
                "creation_data",
                "latitude",
                "longitude",
                "country",
                "city".
                ]
