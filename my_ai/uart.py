import requests

from library import *

url = 'https://tro-ly-ao-c6d33-default-rtdb.firebaseio.com/.json'
"""json = {
  "esp_get": {
    "blue": 0,
    "yellow": 0
  }
}"""
def get_h_t():
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        t = data['esp_patch']['temperature']
        h = data['esp_patch']['humidity']

    return [t, h]

if __name__ == '__main__':
    txt = get_h_t()