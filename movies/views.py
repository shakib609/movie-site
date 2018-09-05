from django.views.generic import ListView, DetailView

from .models import Movie


class HomePageView(ListView):
    template_name = 'movies/homepage.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.all()[:8]


class MovieDetailView(DetailView):
    template_name = 'movies/detail.html'
    context_object_name = 'movie'
    queryset = Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = self.object.genres.all()
        context['download_links'] = self.object.download_links.all()
        context['random_movies'] = Movie.objects.order_by('?')[:4]
        context['comments'] = self.object.comments.order_by('-created_at').all()
        return context
