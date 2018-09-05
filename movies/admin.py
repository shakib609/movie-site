from django.contrib import admin

from .models import Movie, Comment, DownloadLink, Genre


admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(DownloadLink)
admin.site.register(Genre)
