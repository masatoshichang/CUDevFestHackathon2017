from PIL import Image, ImageDraw
import requests
from io import BytesIO

from microsoft.microsoft_api import *


def draw_rect_at_face(image, coord):
    im = Image.open(image)
    box_coord = [coord['top'], coord['left'], coord['top'] + coord['height'], coord['left'] + coord['width']]

    draw = ImageDraw.Draw(im)
    draw.rectangle(box_coord)

    im.show()


if __name__ == '__main__':
    payload = {'url': 'https://lh5.googleusercontent.com/-Sv0q6lkSAGM/AAAAAAAAAAI/AAAAAAAAAZM/nLrSzTXJz0I/s0-c-k-no-ns/photo.jpg'}

    emotion_data = get_emotion(payload)
    coord = emotion_data[0]['faceRectangle']

    r = requests.get(payload['url'], stream=True)
    r.raw.decode_content = True

    draw_rect_at_face(r.raw, coord)

