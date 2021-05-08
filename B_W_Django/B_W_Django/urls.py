from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # import token auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Backend.url')),
    path('auth/',obtain_auth_token) # for get the user token

]
