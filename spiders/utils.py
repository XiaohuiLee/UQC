# -*- coding:utf-8 -*-
import requests
import pandas as pd
import json
# from Crypto import HMAC, SHA256
import hashlib
import hmac
import base64




def loads_json(url):
  sess = requests.Session()
  response = sess.get(url)
  if response.status_code == 200:
    # pass
    jData = json.loads(response.content)
    for key in jData:
      print("This is the value for {}".format(key))
      print(jData[key])
  else:
    # pass
    print("sorry")
    print(response.status_code)




def hmac_sha256(payload, api_secret):
  # payload = bytes(payload).encode('utf-8')
  # api_secret = bytes(api_secret).encode('utf-8')
  payload = bytes(payload, 'utf-8')
  api_secret = bytes(api_secret, 'utf-8')
  signature = hmac.new(payload, api_secret,digestmod = hashlib.sha256).hexdigest()
  print(signature)
  return(signature)

