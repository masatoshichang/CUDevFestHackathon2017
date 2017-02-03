import requests
import urllib
from urlparse import urlparse
import urlparse
import json

EMOTION_API_URL = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
EMOTION_API_KEY = 'e51cfa3722484ea3adc0fb7967c4ad51'


def get_emotion(json_data):
    """
    Call Emotion API
    :json_data: send url data {'url': 'www.example.com/abc.jpg'}

    :return: JSON data
    """
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': EMOTION_API_KEY,
    }

    payload = json.dumps(json_data)

    r = requests.post(EMOTION_API_URL, headers=headers, data=payload)
    return r.json()


if __name__ == '__main__':
    # Example
    payload = {'url': 'https://lh5.googleusercontent.com/-Sv0q6lkSAGM/AAAAAAAAAAI/AAAAAAAAAZM/nLrSzTXJz0I/s0-c-k-no-ns/photo.jpg'}

    t = get_emotion(payload)
    print(t)



