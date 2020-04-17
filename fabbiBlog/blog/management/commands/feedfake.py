from django.core.management.base import BaseCommand, CommandError
from blog.models import *
from faker import Faker
from faker.generator import random

fake = Faker(['en_US'])
class Command(BaseCommand):
    help = 'Faker T1'

    def add_arguments(self, parser):
        parser.add_argument('record', help='get type int', type=int)

    def handle(self, *args, **options):
        records = options['record']
        user = User.objects.all()
        for _ in range(0, records):
            PostModel.objects.create(
                post_title=fake.name(),
                user_id=random.choice(user),
                content=fake.name(),
            )
