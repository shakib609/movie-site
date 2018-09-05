# Generated by Django 2.1.1 on 2018-09-05 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=16)),
                ('link', models.CharField(max_length=512)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='download_links', to='movies.Movie')),
            ],
        ),
    ]
