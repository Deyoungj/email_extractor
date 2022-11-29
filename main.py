import requests, re
from bs4 import BeautifulSoup
from collections import deque




def process_links(url: str , length: int = 5):
    
    unprocessed_links = deque()

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

        new_email = re.findall(r"[\w\.-]+@[\w\.-]+", response.text, re.I)
        emails.update(new_email)

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        link_list = set([link["href"] for link in links if link["href"] and link["href"].startswith("https://")])
        link_list = [link for link in link_list if not link.endswith('.pdf') or not link.endswith('.png') or not link.endswith('.jpg')] 

        for link in link_list:
            unprocessed_links.append(link)

        










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

        new_email = re.findall(r"[\w\.-]+@[\w\.-]+", response.text, re.I)
        # emails.add(new_email)

    return processed_links, emails



def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()

    

    # url = "https://www.google.com/search?q=business+emails+in+the+united+kindom&oq=business+emails+in+the+united+kindom&aqs=chrome..69i57j33i10i160l3.34218j0j7&sourceid=chrome&ie=UTF-8"

    response = get_url(url)
    # soup = parse_html(response)
    # links = get_links(soup)
    # filtered = filter_links(links)
    # unprocessed_urls.extend(filtered)
    # unprocessed_urls.appendleft(url)
    # print(len(unprocessed_urls))
    # # new_email = re.findall(r"[\w\.-]+@[\w\.-]+", response.text, re.I)
    # # print(new_email)
    # extract_email(filtered)
    print(response.text)

main("https://www.google.com/search?q=construction+paint+company+Illinois+%40hotmail.com&biw=1280&bih=667&sxsrf=ALiCzsYXIBI32sS0XVFcDctLfoV5sLwRxA%3A1669734883330&ei=4yGGY9DjE6LosAf30IGoAQ&ved=0ahUKEwiQ4duU19P7AhUiNOwKHXdoABUQ4dUDCBE&uact=5&oq=construction+paint+company+Illinois+%40hotmail.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgcIABAeEKIEOggIABCiBBCwAzoKCAAQHhCiBBCwA0oECEEYAUoECEYYAFCgEljlFWDgH2gCcAB4AIAB-QOIAbQHkgEFNC0xLjGYAQCgAQGgAQLIAQPAAQE&sclient=gws-wiz-serp")







