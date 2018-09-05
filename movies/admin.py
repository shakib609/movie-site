from django.contrib import admin

from .models import Movie, Comment, DownloadLink, Genre
from .forms import DownloadLinkForm


class DownloadLinkInline(admin.TabularInline):
    model = DownloadLink
    form = DownloadLinkForm
    extra = 0


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [DownloadLinkInline]


admin.site.register(DownloadLink)
admin.site.register(Comment)
admin.site.register(Genre)
