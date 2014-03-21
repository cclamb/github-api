__author__ = 'cclamb'

import requests

url = 'https://api.github.com/users/cclamb'

response = requests.get(url)
print(response.text)