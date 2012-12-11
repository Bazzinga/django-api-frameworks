# coding: utf-8
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Drops test data and generates again'

    def handle(self, *args, **options):
        call_command('drop_test_data')
        call_command('generate_test_data')
