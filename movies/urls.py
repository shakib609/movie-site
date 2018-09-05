from django.urls import path

from .views import HomePageView

app_name = 'movies'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
