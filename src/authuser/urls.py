from django.urls import include, path

from authuser.views import profile, RegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile', profile, name='profile'),
    path('register', RegisterView.as_view(), name='register'),
]
