from django.core.management.base import BaseCommand, CommandError
from home.models import *
from faker import Faker
from faker.generator import random
from django.utils import timezone
fake = Faker(['en_US'])


class Command(BaseCommand):
    help = 'Faker T1'

    def add_arguments(self, parser):
        parser.add_argument('record', type=int, help='get type int')

    def handle(self, *args, **options):
        records = options['record']
        for _ in range(0, records):
            PostModel.objects.create(
                post_title=fake.name(),
                user_id='1',
                content=fake.text(),
            )
        for _ in range(0, records):
            CommentsModel.objects.create(
                comment=fake.text(),
                user_id='1',
            )
