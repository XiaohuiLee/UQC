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
  signature = hmac.new(
      bytes(api_secret, 'ascii'), 
      bytes(payload, 'ascii'),
      digestmod = hashlib.sha256).hexdigest()
  return(signature)

