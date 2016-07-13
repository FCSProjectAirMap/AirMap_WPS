from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.genseric import View
from django.shortucts import redirect

from geopy.geocoders import GoogleV3


class TravelsCreateView(LoginRequiredMixin, View, GoogleV3):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):

        geolocator = GoogleV3(api_key=GOOGLEV3_API_KEY)

        travel_title = request.POST.get("travel_title")
        post = request.user.travel_set.create(
            travel_title=travel_title
            )

        image_metadatas = request.Post.get("image_metadatas")

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

            post = request.travel.imagemetadata_set.create(
                creation_data=creation_data,
                latitude=latitude,
                longitude=longitude,
                country=country,
                city=city,
            )

            return redirect(post)
