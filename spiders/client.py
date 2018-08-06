# -*- coding:utf-8 -*-
import requests
import pandas as pd
import json
from utils import loads_json

endpoint = "https://bb.otcbtc.com"

# proxies = {
#   "http": "http://txp-01.tencent.com:8080",
# }

# #____________tickers的获取情况______________
tickers_api = "/api/v2/tickers"
tickers_url = endpoint + tickers_api
# loads_json(tickers_url)


# #____________markets的获取情况______________
# markets_api = "/api/v2/markets"
# markets_url = endpoint + markets_api
# loads_json(markets_url)


#____________markets的获取情况______________

market_api = "/octeos"
market_url = tickers_url + market_api
# loads_json(market_url)

#____________某个特定市场交易行情的获取情况______________
depth_api = "/api/v2/depth"
get_params = "?market={}&limit={}"

# loads_json(endpoint + depth_api + get_params.format("octeth", 5))

#____________某个特定市场交易的获取情况______________

trade_api = "/api/v2/trades"
trade_url = endpoint + trade_api + get_params.format("octeth", 4)
response = requests.get(trade_url)
if response.status_code == 200:
  # pass
  print(response.content)
else:
  # pass
  print("sorry, something's wrong")


