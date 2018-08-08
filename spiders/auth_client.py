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




#-------------------------------钱包账户信息---------------------------
account_api = "/api/v2/account"
account_payload = "GET|/api/v2/account|access_key={}&currency=btc".format(api_key)
account_sign = hmac_sha256(account_payload, secret_key)
account_access_params = "access_key={}&currency=btc&signature={}".format(api_key, account_sign)
account_url = endpoint + account_api + account_access_params
account_resp = sess.get(account_url)
# print(account_resp)