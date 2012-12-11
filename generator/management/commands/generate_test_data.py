# coding: utf-8
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from ...datagenerators import ApiGenerator

class Command(BaseCommand):
    help = 'Generates tests data'

    def handle(self, *args, **options):
        ApiGenerator().generate()
