import os
from TwitterAPI import TwitterAPI


def get_stream_with_track(api, place):
    return api.request('statuses/filter', {'locations': place})


def main():
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
      '69.12597656249999',
      '41.178653972331674',
      '69.4281005859375',
      '41.39741506646461'
      ]

    print 'Connecting to Twitter stream ...'
    r = get_stream_with_track(api, tashkent)
    for item in r:
        print item['user']['name'], '-->', item['text']


if __name__ == '__main__':
    main()
