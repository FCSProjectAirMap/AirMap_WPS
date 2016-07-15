from rest_framework.generics import APIView
from rest_framework.response import Response
from rest_framework import status

from geopy.geocoders import GoogleV3


class TravelCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):

        travel_title = request.POST.get("travel_title")
        travels = request.user.travel_set.create(
            travel_title=travel_title
        )

        geolocator = GoogleV3(api_key=GOOGLEV3_API_KEY)

        image_metadatas = request.POST.get("image_metadatas") 

        for image_metadata in image_metadatas:
            creation_data = image_metadata.get("creation_data")
            latitude = image_metadata.get("latitude")
            longitude = image_metadata.get("longitude")

            location = geolocatodr.reverse("{latitude}, {longitude}".format(latitude=latitud, longitude=longitude))
            point = location[0]
            address = point.address
            address_list = address.split(",")
            country = address_list[-1]
            city = address_list[-2]

            metadatas = request.travel.imagemetadata_set.create(
                creation_data=creation_data,
                latitude=latitude,
                longitude=longitude,
                country=country,
                city=city,
            )

        return Response(
                status=status.HTTP_200_OK,
                )
