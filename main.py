import requests, re
from bs4 import BeautifulSoup
from collections import deque


def get_url(url: str ):
    
    if url.startswith("https://"):
        url = url
    else:
        url = "https://"+url
    
    try:
        response = requests.get(url)
    except:
        pass
    print(response.status_code)
    return response


def parse_html(url: str):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup


def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()

    # emails extracted
    emails = set()

    # url = "https://www.google.com/search?q=business+emails+in+the+united+kindom&oq=business+emails+in+the+united+kindom&aqs=chrome..69i57j33i10i160l3.34218j0j7&sourceid=chrome&ie=UTF-8"


    try:
        r = requests.get(url)
    except:
        pass
    print(r.status_code)


    soup = BeautifulSoup(r.text, "html.parser")
    
    links = soup.find_all('a', href=True)

    link_list = set([link["href"] for link in links if link["href"] and link["href"].startswith("https://")])

    print(len(link_list))


    # for link in link_list:
    #     print(link["href"])
    # print(soup.prettify())

    # for mail in re.findall(EMAIL_REX, r.text):

    #     print(mail)

main("https://miet.ac.in/")








