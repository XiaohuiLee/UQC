# -*- coding:utf-8 -*-
import requests
import pandas as pd
import json
from utils import loads_json,hmac_sha256
endpoint = "https://bb.otcbtc.com"

api_key = "o7ZbYSkXTJLkx9TJo6xDsSkNh3kPgJlQPk38UBdX"
secret_key = "qwF240N8HrbYraFL0cWV1dCGk5pbtuIRBCh3buL6"
payload = "GET|/api/v2/users/me|access_key={}".format(api_key)

signature = hmac_sha256(payload, secret_key)
user_api = "/api/v2/users/me"
access_params = "?access_key={}&signature={}".format(api_key, signature)

user_info_url = endpoint + user_api + access_params
sess = requests.session()
resp = sess.get(user_info_url)
if resp.status_code == 200:
    print(resp.content)
else:
    print(resp.content)

