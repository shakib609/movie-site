from django.views.generic import ListView

from .models import Movie


class HomePageView(ListView):
    template_name = 'movies/homepage.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.all()[:8]
