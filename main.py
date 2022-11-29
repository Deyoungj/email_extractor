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


def extract_email(links: list):

    # unprocessed_nested urls
    unprocessed_urls = deque(links)

    processed_links = set()

    # emails extracted
    emails = set()



    while len(unprocessed_urls) > 0:
        url = unprocessed_urls.popleft()
        processed_links.add(url)
        
        try:
          response = requests.get(url)
        except:

          continue

        new_email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I)
        for mail in new_email:

            print(new_email)
        # emails.add(new_email)

    return processed_links, emails



def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()

    

    # url = "https://www.google.com/search?q=business+emails+in+the+united+kindom&oq=business+emails+in+the+united+kindom&aqs=chrome..69i57j33i10i160l3.34218j0j7&sourceid=chrome&ie=UTF-8"

    response = get_url(url)
    soup = parse_html(response)
    links = get_links(soup)
    filtered = filter_links(links)
    unprocessed_urls.extend(filtered)
    unprocessed_urls.appendleft(url)
    print(len(unprocessed_urls))
    new_email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I)
    print(new_email)
    # for mail in new_email:

    #     print(new_email)
    
    # while unprocessed_urls:
    #     pass



    # for link in link_list:
    #     print(link["href"])
    # print(soup.prettify())

    # for mail in re.findall(EMAIL_REX, r.text):

    #     print(mail)

main("https://www.google.com/search?q=construction+paint+company+Illinois+%40hotmail.com&biw=1280&bih=667&sxsrf=ALiCzsYXIBI32sS0XVFcDctLfoV5sLwRxA%3A1669734883330&ei=4yGGY9DjE6LosAf30IGoAQ&ved=0ahUKEwiQ4duU19P7AhUiNOwKHXdoABUQ4dUDCBE&uact=5&oq=construction+paint+company+Illinois+%40hotmail.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgcIABAeEKIEOggIABCiBBCwAzoKCAAQHhCiBBCwA0oECEEYAUoECEYYAFCgEljlFWDgH2gCcAB4AIAB-QOIAbQHkgEFNC0xLjGYAQCgAQGgAQLIAQPAAQE&sclient=gws-wiz-serp")







