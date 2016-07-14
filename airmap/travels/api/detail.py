from rest_framework.generics import ListAPIView
from api.travel.serializers import DetailModelSerializer


class TravelDetailAPIView(ListAPIView):
    queryset = request.travel.imagemetadata_set.order_by('creation_data')
    serializer_class = DetailModelSerializer
