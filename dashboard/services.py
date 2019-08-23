import requests


def get_channel_data():
    url = 'https://thingspeak.com/channels/845365/feed.json'
    r = requests.get(url)
    feed_data = r.json()
    return feed_data
