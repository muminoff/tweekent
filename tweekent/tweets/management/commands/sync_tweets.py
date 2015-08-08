from django.core.management.base import BaseCommand
from tweets.models import User, Tweet


class Command(BaseCommand):
    help = 'Retrieve real time tweets and synchronyze'

    def handle(self, *args, **options):

        for user in User.objects.all():
            print(user)

        for tweet in Tweet.objects.all():
            print(tweet)
