# coding: utf-8
from __future__ import unicode_literals

from .factories import UserFactory as UserF
from .factories import AdminFactory as AdminF
from .factories import LogEntryFactory as LogF
from .factories import GroupFactory as GroupF

class ApiGenerator(object):
    def generate(self):
        self.generate_admin()
        self.generate_users()
        self.generate_logs()
        self.generate_groups()
        self.generate_memberships()

    def generate_admin(self):
        AdminF(username='admin', password='123')

    def generate_users(self):
        self.user1 = UserF()
        self.user2 = UserF()
        self.user3 = UserF()

    def generate_logs(self):
        LogF(user=self.user1)
        LogF(user=self.user1)
        LogF(user=self.user1)
        LogF(user=self.user1)
        LogF(user=self.user2)
        LogF(user=self.user2)
        LogF(user=self.user3)

    def generate_groups(self):
        self.group1 = GroupF()
        self.group2 = GroupF()

    def generate_memberships(self):
        self.group1.user_set.add(self.user1)
        self.group1.user_set.add(self.user2)
        self.group2.user_set.add(self.user2)
