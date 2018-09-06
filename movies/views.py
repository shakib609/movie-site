from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView)

from .models import Movie, Comment
from .forms import CommentForm


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
        context['comments'] = self.object.comments.order_by(
            '-created_at').all()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    http_method_names = ['post']

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy(
            'movies:detail',
            kwargs={'pk': pk})

    def form_valid(self, form):
        self.object = comment = form.save(commit=False)
        comment.created_by = self.request.user
        comment.movie = get_object_or_404(
            Movie, pk=self.kwargs.get('pk'))
        comment.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Comment can not be empty.',
            extra_tags='is-danger'
        )
        return HttpResponseRedirect(self.get_success_url())


class NoPiracyTemplateView(TemplateView):
    template_name = 'movies/nopiracy.html'
