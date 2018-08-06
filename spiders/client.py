# -*- coding:utf-8 -*-
import requests
import pandas as pd


endpoint = "https://bb.otcbtc.com"
pub_api = "https://bb.otcbtc.com/api/v2/tickers"
url = endpoint + pub_api
proxies = {
  "http": "http://txp-01.tencent.com:8080",
  
}

sess = requests.Session()

response = sess.get(pub_api, proxies = proxies)
print(response.status_code)
print(response.content[1:100])
