import requests
import pandas as pd

proxies = {
  "http": "http://txp-01.tencent.com:8080",
  
}
sess = requests.Session()
url = "http://www.baidu.com"
response = sess.get(url, proxies = proxies)
print(response.status_code)
print(response.content)