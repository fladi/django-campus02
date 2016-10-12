#!/usr/bin/python
# -*- coding: utf-8 -*-

import purl
import requests
import tmdbsimple

from dateutil import parser

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from ...models import Movie, Genre


class Command(BaseCommand):
    help = 'Import data from TMDB'

    def add_arguments(self, parser):
        parser.add_argument('movie_id', nargs='+', type=int)

    def handle(self, *args, **options):
        tmdbsimple.API_KEY = settings.TMDB_API_KEY
        conf = tmdbsimple.Configuration().info()
        secure_base_url = conf.get('images').get('secure_base_url')
        img_base = purl.URL(secure_base_url).add_path_segment('w780')
        for movie_id in options['movie_id']:
            info = tmdbsimple.Movies(movie_id).info()
            defaults = {
                'title': info.get('title'),
                'released': parser.parse(info.get('release_date')),
                'runtime': info.get('runtime', 0),
                'tagline': info.get('tagline'),
                'synopsis': info.get('overview'),
                'homepage': info.get('homepage')
            }
            if info.get('poster_path', None):
                poster_path = info.get('poster_path').lstrip('/')
                poster_url = img_base.add_path_segment(poster_path)
                print(poster_url.as_string())
                r = requests.get(poster_url.as_string())
                print(r.status_code)
                if r.status_code == 200:
                    defaults['poster'] = ContentFile(r.content, name=poster_path)
            movie, _ = Movie.objects.update_or_create(
                tmdb=movie_id,
                defaults=defaults
            )
            self.stdout.write(
                self.style.SUCCESS('Movie: {m}'.format(m=movie))
            )
            for genre in info.get('genres', []):
                name = genre.get('name')
                g, _ = Genre.objects.update_or_create(
                    tmdb=genre.get('id'),
                    defaults={
                        'name': name
                    }
                )
                movie.genres.add(g)
        self.stdout.write(self.style.SUCCESS('Done'))
