from django import forms

from .models import DownloadLink, Comment, Genre


CHOICES = [
    ('720p.BluRay', '720p.BluRay'),
    ('1080p.BluRay', '1080p.BluRay'),
    ('720p.WEBRip', '720p.WEBRip'),
    ('1080p.WEBRip', '1080p.WEBRip'),
]


class DownloadLinkForm(forms.ModelForm):
    quality = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = DownloadLink
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )


class BrowseMoviesForm(forms.Form):
    query = forms.CharField(required=False)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all().order_by('name'),
        empty_label="Select Genre",
        required=False)
