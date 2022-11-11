import requests, re
from bs4 import BeautifulSoup



EMAIL_REX = r'[\w\.]+@[\w\.]+'

url = ''

r = requests.get("https://www.google.com/search?q=requests+hhas+no+attribute+status&oq=requests+hhas+no+attribute+status&aqs=chrome..69i57j0i22i30l4.38788j0j4&sourceid=chrome&ie=UTF-8")


print(BeautifulSoup(r.text).prettify())