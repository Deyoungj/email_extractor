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
    print('status code : ',response.status_code)

    return response


def filter_links(links: list) -> set:
    link_list = set([link["href"] for link in links if link["href"] and link["href"].startswith("https://")])

    return link_list



def parse_html(response: requests):
    soup = BeautifulSoup(response.text, "html.parser")
    return soup



def get_links(soup: BeautifulSoup):
    links = soup.find_all("a", html=True)
    return links



def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()

    # emails extracted
    emails = set()

    # url = "https://www.google.com/search?q=business+emails+in+the+united+kindom&oq=business+emails+in+the+united+kindom&aqs=chrome..69i57j33i10i160l3.34218j0j7&sourceid=chrome&ie=UTF-8"

    url = get_url(url)

    parsed_html = parse_html(url)

    links = get_links(parsed_html)

    print(links)
    filtered_links = filter_links(links)
    print(filtered_links)

    # for link in link_list:
    #     print(link["href"])
    # print(soup.prettify())

    # for mail in re.findall(EMAIL_REX, r.text):

    #     print(mail)

main("https://miet.ac.in/")








