from django.db import models as m


class Organization(m.Model):
    name = m.CharField(max_length=255)
    first_owner = m.FloatField(null=True)
    board_of_directors = m.TextField(null=True)
    chairman_of_the_board = m.TextField(null=True)
    members_of_the_board = m.TextField(null=True)
    director = m.FloatField(null=True)
    chief_accountant = m.CharField(null=True)
    BIN = m.FloatField(null=True)
    address = m.TextField()
    number = m.CharField(max_length=100)
    mail = m.TextField(default='0')
    site = m.CharField(max_length=100)
    license = m.CharField(max_length=255, null=True)
    branches = m.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
