import requests, re
from bs4 import BeautifulSoup
from collections import deque


def process_links(url: str , length: int = 10):
    
    unprocessed_links = deque([])

    processed_url = []
    emails  = set()

    count = 0

    

    while unprocessed_links:
        count += 1
        if count == length:
            break

        url = unprocessed_links.popleft()
        processed_url.append(url)
        
        if url.startswith("https://"):
            url = url
        else:
            url = "https://"+url

        try:
            response = requests.get(url)
        except:
            pass

        print(f"[{count}]**  processing link: [{url}] **status: [{response.status_code}] ")


        new_email = re.findall(r"[\w\.-]+@[\w\.-]+", response.text, re.I)
        emails.update(new_email)

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        link_list = set([link["href"] for link in links if link["href"] and link["href"].startswith("https://")])
        link_list = [link for link in link_list if not link.endswith('.pdf') or not link.endswith('.png') or not link.endswith('.jpg')] 

        for link in link_list:
            unprocessed_links.append(link)

        



def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()


main("https://www.google.com/search?q=construction+paint+company+Illinois+%40hotmail.com&biw=1280&bih=667&sxsrf=ALiCzsYXIBI32sS0XVFcDctLfoV5sLwRxA%3A1669734883330&ei=4yGGY9DjE6LosAf30IGoAQ&ved=0ahUKEwiQ4duU19P7AhUiNOwKHXdoABUQ4dUDCBE&uact=5&oq=construction+paint+company+Illinois+%40hotmail.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgcIABAeEKIEOggIABCiBBCwAzoKCAAQHhCiBBCwA0oECEEYAUoECEYYAFCgEljlFWDgH2gCcAB4AIAB-QOIAbQHkgEFNC0xLjGYAQCgAQGgAQLIAQPAAQE&sclient=gws-wiz-serp")







