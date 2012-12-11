# coding: utf-8
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Drops tests data'

    def handle(self, *args, **options):
        MODELS = [
            'auth.user',
            'auth.group',
        ]

        for models in MODELS:
            self._drop_all(models=models)

    def _drop_all(self, models):
        content_type = ContentType.objects.get_by_natural_key(
            *models.split('.'))
        content_type.model_class().objects.all().delete()
