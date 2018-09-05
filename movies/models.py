from django.db import models
from django.contrib.auth.models import User

import uuid


def generate_upload_location(instance, filename):
    random = str(uuid.uuid4())
    return 'mov_{}/{}.jpg'.format(instance.id, random)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    plot = models.TextField()
    poster_image = models.ImageField(
        upload_to=generate_upload_location,
        null=True,
        blank=True)
    year = models.IntegerField()
    imdb_rating = models.FloatField(default=0)

    def __str__(self):
        return '{}({})'.format(self.title, self.year)


class Comment(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return '{}... - {}'.format(self.text[:5], self.created_by.username)
