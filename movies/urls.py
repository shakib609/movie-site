from django.urls import path

from .views import HomePageView, MovieDetailView

app_name = 'movies'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='detail'),
]
