import requests


def get_channel_data():
    url = 'https://thingspeak.com/channels/9/feeds.json'
    r = requests.get(url)
    data = r.json()
    feed_data = data
    return feed_data
