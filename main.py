import requests, re
from bs4 import BeautifulSoup
from collections import deque


# get url response
def get_url(url: str ):

    if url.startswith("https://"):
        url = url
    else:
        url = "https://"+url
    
    try:
        response = requests.get(url)
    except:
        pass
    

    return response


def filter_links(links: list) -> set:
    link_list = set([link["href"] for link in links if link["href"] and link["href"].startswith("https://")])
    link_list = [link for link in link_list if not link.endswith('.pdf') or not link.endswith('.png') or not link.endswith('.jpg')] 

    return link_list



def parse_html(response):
    soup = BeautifulSoup(response.text, "html.parser")
    return soup



def get_links(soup):
    links = soup.find_all("a")
    return links



def process_nested_links(links: list):

    # unprocessed_nested urls
    unprocessed_urls = deque(links)


    while len(unprocessed_urls) > 0:
        pass



def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()

    # emails extracted
    emails = set()

    # url = "https://www.google.com/search?q=business+emails+in+the+united+kindom&oq=business+emails+in+the+united+kindom&aqs=chrome..69i57j33i10i160l3.34218j0j7&sourceid=chrome&ie=UTF-8"

    response = get_url(url)
    soup = parse_html(response)
    links = get_links(soup)
    filtered = filter_links(links)
    unprocessed_urls.extend(filtered)
    
    # while unprocessed_urls:
    #     pass
    print(unprocessed_urls)



    print('status code : ',response.status_code)


    # for link in link_list:
    #     print(link["href"])
    # print(soup.prettify())

    # for mail in re.findall(EMAIL_REX, r.text):

    #     print(mail)

main("https://miet.ac.in/")








