import requests
import urllib
from urlparse import urlparse
import urlparse
import json

EMOTION_API_URL = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
EMOTION_API_KEY = '186c5e37fa44403286396f8f9907b709'

FACE_API_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
FACE_API_KEY = 'dc7ab2e1c4da4414be3d29bb476dcac8'


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

    json_data = {'url': json_data}

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

    json_data = {'url': json_data}

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
    payload = 'https://lh5.googleusercontent.com/-Sv0q6lkSAGM/AAAAAAAAAAI/AAAAAAAAAZM/nLrSzTXJz0I/s0-c-k-no-ns/photo.jpg'

    t = get_emotion(payload)
    print(t)

    t = get_face(payload)
    print(t)

    # No face
    payload = 'https://lh3.googleusercontent.com/-4LORSEgp28U/AAAAAAAAAAI/AAAAAAAAErY/W4Ug6i3Vc64/s0-c-k-no-ns/photo.jpg'
    t = get_emotion(payload)
    print(t)

    t = get_face(payload)
    print(t)



