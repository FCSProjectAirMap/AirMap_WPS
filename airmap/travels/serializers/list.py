from rest_framework import serializers
from travels.models import travel


class TravelModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = [
                "travel_title",
                ]
