# -*- coding:utf-8 -*-
import requests
import pandas as pd
import json
from utils import loads_json,hmac_sha256
endpoint = "https://bb.otcbtc.com"




#-------------------------------个人账户信息---------------------------
api_key = "KPDoOixz1hgzx9DDn4728A4Sg3oTXMUvVWkApWfx"
secret_key = "UAlDxhkbK38CH50vJHHQmFnyKHmGtrHJJnoPnZNO"
payload = "GET|/api/v2/users/me|access_key={}".format(api_key)

signature = hmac_sha256(payload, secret_key)
user_api = "/api/v2/users/me"
access_params = "?access_key={}&signature={}".format(api_key, signature)

user_info_url = endpoint + user_api + access_params
sess = requests.session()
resp = sess.get(user_info_url)
print(resp.content)


