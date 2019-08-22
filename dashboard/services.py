import requests


def get_channel_light_data():
    # url = 'https://thingspeak.com/channels/9/field/1.json'
    url = 'https://api.thingspeak.com/channels/9/feeds.json'
    r = requests.get(url)
    data = r.json()
    feed_data = data
    return feed_data


def get_channel_temp_data():
    url = 'https://thingspeak.com/channels/9/field/2.json'
    r = requests.get(url)
    data = r.json()
    feed_data = data
    return feed_data
