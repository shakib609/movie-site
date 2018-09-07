from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.text import slugify

import uuid


def generate_upload_location(instance, filename):
    random = str(uuid.uuid4())
    return '{}/{}.jpg'.format(slugify(instance.title), random)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    plot = models.TextField()
    poster_image = models.ImageField(
        upload_to=generate_upload_location,
        null=True,
        blank=True)
    year = models.IntegerField()
    imdb_rating = models.FloatField(default=0)
    trailer_link = models.URLField(null=True, blank=True, max_length=512)
    genres = models.ManyToManyField(
        'Genre', related_name='movies')

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return '{}({})'.format(self.title, self.year)

    def get_absolute_url(self):
        return reverse_lazy('movies:detail', kwargs={'pk': self.id})


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('movies:browse_movies') +\
            '?genre={}'.format(self.id)


class Comment(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return '{}... - {}'.format(self.text[:5], self.created_by.username)


class DownloadLink(models.Model):
    quality = models.CharField(max_length=16)
    link = models.CharField(max_length=512)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='download_links')

    def __str__(self):
        return '{} - {}'.format(self.quality, self.movie.title)
