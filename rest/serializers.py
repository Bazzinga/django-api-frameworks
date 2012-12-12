# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group, Permission
from django.contrib.admin.models import LogEntry
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class LogSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.RelatedField(source='user')
    class Meta:
        model = LogEntry


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    permissions = serializers.ManySlugRelatedField(
#        slug_field='codename',
#        queryset=Permission.objects.all()
#    )
#
#    class Meta:
#        model = Group
#        fields = ('url', 'name', 'permissions')
#
