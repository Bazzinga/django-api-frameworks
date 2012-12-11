# coding: utf-8
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals

class Command(BaseCommand):
    help = 'Reset\'s db and syncs again'

    def handle(self, *args, **options):
        signals.post_syncdb.disconnect(
            create_superuser,
            sender=auth_models,
            dispatch_uid='django.contrib.auth.management.create_superuser')

        call_command('reset_db', router='default')
        call_command('syncdb')
