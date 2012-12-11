# coding: utf-8
from __future__ import unicode_literals

import random
import string

from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry

import factory

def random_word(length=None):
    def inner_func(o=None):
        word_length = length or random.randrange(3, 13)
        return ''.join(
            random.choice(string.ascii_lowercase) for c in range(word_length)
        )
    return inner_func

class UserFactory(factory.Factory):
    FACTORY_FOR = User

    first_name = factory.Sequence(lambda n: 'Пользователь %s' % n)
    username = factory.LazyAttribute(random_word(8))
    email = factory.LazyAttribute(random_word(8))
    password = factory.LazyAttribute(random_word(8))

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user

class AdminFactory(UserFactory):
    is_staff = True
    is_superuser = True

class LogEntryFactory(factory.Factory):
    FACTORY_FOR = LogEntry

    user = factory.LazyAttribute(lambda o: UserFactory())
    action_flag = 1

class GroupFactory(factory.Factory):
    FACTORY_FOR = Group

    name = factory.Sequence(lambda n: 'Группа %s' % n)
