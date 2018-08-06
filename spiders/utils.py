# -*- coding:utf-8 -*-
import requests
import pandas as pd
import json


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