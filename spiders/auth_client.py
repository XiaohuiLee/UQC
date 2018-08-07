# -*- coding:utf-8 -*-
import requests
import pandas as pd
import json
from utils import loads_json,hmac_sha256
endpoint = "https://bb.otcbtc.com"

api_key = "FakhM90LN0PnVxC2IfLM2XVJKsCYtXeDwRix6d3f"
secret_key = "8Lu7PxgA9xJIJGVdkh2atEjDgFUXwBPLIDjdn4Kf"
payload = "GET|/api/v2/users/me|access_key={}".format(api_key)

signature = hmac_sha256(payload, secret_key)
user_api = "/api/v2/users/me"
access_params = "?access_key={}&signature={}".format(api_key, signature)

user_info_url = endpoint + user_api + access_params
sess = requests.session()
resp = sess.get(user_info_url)
print(resp.content)

# e626221f8fe98601b7ebdb68215b085e55992ebc8ee466545c1cb71c2fd9e336
f334b82ee6d3801fa7e2ff7259166c3f76c8d4d4855d322a3bfc93ab11c31b73