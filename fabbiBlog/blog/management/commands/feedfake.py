from django.core.management.base import BaseCommand, CommandError
from blog.models import *
from faker import Faker
fake = Faker(['en_US'])
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('recodes', nargs='+', type=int)

    def handle(self, *args, **options):
        pass
        # for poll_id in options['recodes']:
        #     try:
        #         poll = PostModel.objects.get(pk=poll_id)
        #     except PostModel.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     PostModel.post_title =
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
