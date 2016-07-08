from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from api.users import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', SignupApi.as_view(), name="signup"),
    url(r'^login/$', obtain_jwt_token),
    ]
