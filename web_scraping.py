import requests
URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(URL)
print(page.content)