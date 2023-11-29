import pandas as p

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from main.models import Organization, Sanction


def del_data():
    Organization.objects.all().delete()
    Sanction.objects.all().delete()


if __name__ == "__main__":
    del_data()
    print('deleted data')
