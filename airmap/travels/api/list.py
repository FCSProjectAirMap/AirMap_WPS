from rest_framework.generics import ListAPIView
from api.travel.serializers import TravelModelSerializer


class TravelListAPIView(ListAPIView):
    queryset = request.user.travel_set.all()
    serializer_class = TravelModelSerializer
