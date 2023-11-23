from django.urls import include, path

from authuser.views import profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile', profile, name='profile'),
]
