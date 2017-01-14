import requests
import base64
import json


def to_b_64(name):
    with open(name + '.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


img_str = to_b_64('messi')


def post_image(image_str):
    url = "https://the-skywalkers-anderson1564-1.c9users.io/api/v1/image"
    data = {'id': 'abc123', 'base64': image_str}
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data, headers).content
    str_json = json.dumps(response)
    return str_json


print post_image(img_str)
