import requests
import json
url = "http://search.twitter.com/search.json?q=python%20pandas"
response = requests.get(url)

data = json.loads(response.text)

