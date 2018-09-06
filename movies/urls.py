from django.urls import path

from .views import (
    HomePageView,
    MovieDetailView,
    CommentCreateView,
    NoPiracyTemplateView)

app_name = 'movies'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path(
        'movies/<int:pk>/comment/', CommentCreateView.as_view(),
        name='comment_create'),
    path(
        'nopiracy.html', NoPiracyTemplateView.as_view(), name='nopiracy')
]
