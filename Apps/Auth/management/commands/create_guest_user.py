from django.core.management import BaseCommand
from django.contrib.auth.models import User
from ...models import UserToken
from ...helper import Random
import os


class Command(BaseCommand):
    help = 'Create Guest User With User Token'

    def handle(self, *args, **options):
        _User = User.objects.create_user(
            username=os.environ.get('GUEST_USERNAME'),
            email=os.environ.get('GUEST_EMAIL'),
            password=os.environ.get('GUEST_PASSWORD'),
            first_name=os.environ.get('GUEST_FIRSTNAME')
        )
        _Token = UserToken.objects.create(
            user=_User,
            token=Random.create_random_token(50, 70)
        )

        self.stdout.write(self.style.SUCCESS('{ Guest } User Created Successfully'))
