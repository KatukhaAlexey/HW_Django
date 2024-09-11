import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            if phone["lte_exists"] == 'True':
                lte = True
            else:
                lte = False
            release = datetime.strptime(phone["release_date"], '%Y-%m-%d')
            Phone.objects.create(
                name=phone["name"],
                image=phone["image"],
                price=int(phone["price"]),
                release_date=release,
                lte_exists=lte,
                slug=slugify(phone["name"])
            )
