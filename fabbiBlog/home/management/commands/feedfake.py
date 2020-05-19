from django.core.management.base import BaseCommand, CommandError
from home.models import *
from faker import Faker
from faker.generator import random
from django.utils import timezone
from uploads import *
fake = Faker(['en_US'])


class Command(BaseCommand):
    help = 'Faker T1'

    def add_arguments(self, parser):
        parser.add_argument('record', type=int, help='get type int')

    def handle(self, *args, **options):
        records = options['record']
        cate = CategoryModel.objects.all()
        c = [c for c in cate]
        for _ in range(0, records):
            PostModel.objects.create(
                title=fake.name(),
                author_id='1',
                content=fake.text(),
                thumbnail=fake.image_url(),
                sapo=fake.text(),

            )
# class Command(BaseCommand):
#     help = 'Faker data'
#
#     def add_arguments(self, parser):
#         parser.add_argument('records', type=int, help='Create records')
#
#     def handle(self, *args, **options):
#         records = options['records']
#         list_class = ['P201', 'P202', 'P203', 'P301', 'P401', 'P402', 'P403', 'P501', 'P502', 'P503']
#         list_course = CourseModel.objects.all()
#         list_faculty = FacultyModel.objects.all()
#         list_tr = TrainingSystemModel.objects.all()
#         for _ in range(0, records):
#             ClassModel.objects.create(
#                 name_class=random.choice(list_class),
#                 course_id=random.choice(list_course),
#                 training_system_id=random.choice(list_tr),
#                 faculty_id=random.choice(list_faculty)
#             )