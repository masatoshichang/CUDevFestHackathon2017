import requests
import urllib
from urlparse import urlparse
import urlparse
import json

EMOTION_API_URL = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
EMOTION_API_KEY = 'e51cfa3722484ea3adc0fb7967c4ad51'

FACE_API_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
FACE_API_KEY = 'f8e991096c734d30ac6806fbc5e1547e'


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


def get_face(json_data):
    """
    Call Face API
    :json_data: send url data {'url': 'www.example.com/abc.jpg'}

    :return: JSON data
    """
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': FACE_API_KEY,
    }

    payload = json.dumps(json_data)

    params = urllib.urlencode({
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'true',
        'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,headPose',
    })

    r = requests.post(FACE_API_URL + '?' + params, headers=headers, data=payload)
    return r.json()


if __name__ == '__main__':
    # Example
    payload = {'url': 'https://lh5.googleusercontent.com/-Sv0q6lkSAGM/AAAAAAAAAAI/AAAAAAAAAZM/nLrSzTXJz0I/s0-c-k-no-ns/photo.jpg'}

    t = get_emotion(payload)
    print(t)

    t = get_face(payload)
    print(t)




