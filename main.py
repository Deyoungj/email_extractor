import requests, re
from bs4 import BeautifulSoup


class Extract:
    def __init__(self, url:list=[]):
        self.url = url
        self.email_rex = r'[\w\.]+@[\w\.]+'
    
    def get_email(self):
        pass

    def get_phone(self):
        pass
    
text = """ 
    Random Email Addresses:
RERUNOPTIONS


gospodin@live.com
heidrich@yahoo.ca
slanglois@aol.com
wkrebs@yahoo.com
improv@live.com
dialworld@hotmail.com
gravyface@mac.com
ramollin@comcast.net
tlinden@yahoo.ca
lbaxter@live.com
lbaxter@me.com
clkao@sbcglobal.net


names

"""

EMAIL_REX = r'[\w\.-]+@[\w\.-]+'
# https://www.randomlists.com/email-addresses

url = "https://stackoverflow.com/questions/70325910/extract-email-and-phone-numbers-from-website-using-python-and-scrapy"

# r = requests.get(url)
# print(r.status_code)

for mail in re.findall(EMAIL_REX, text):
    print(mail)


# print(BeautifulSoup(r.text).prettify())

