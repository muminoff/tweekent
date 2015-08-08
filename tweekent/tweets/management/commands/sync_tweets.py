import os
from TwitterAPI import TwitterAPI
from django.core.management.base import BaseCommand
from tweets.models import User, Tweet
import json


class Command(BaseCommand):
    help = 'Retrieve real time tweets and synchronyze'

    def get_stream_with_track(self, api, place):
        return api.request('statuses/filter', {'locations': place})

    def handle(self, *args, **options):
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token_key = os.environ.get('ACCESS_TOKEN_KEY')
        access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
        api = TwitterAPI(
            consumer_key,
            consumer_secret,
            access_token_key,
            access_token_secret
        )
        tashkent = [
            '69.140877',
            '41.209011',
            '69.397034',
            '41.401421'
        ]
        r = self.get_stream_with_track(api, tashkent)
        for item in r:
            # print(json.dumps(item))
            user = User()
            # user.id = item['user']['id_str']
            user.name = item['user']['name']
            user.screen_name = item['user']['screen_name']
            user.location = item['user']['location']
            user.description = item['user']['description']
            user.profile_image = item['user']['profile_image_url']
            user.save()

            tweet = Tweet()
            tweet.text = item['text']
            tweet.timestamp = item['timestamp_ms']
            tweet.user = user
            tweet.save()
            print(item['user']['name'], '-->', item['text'])
