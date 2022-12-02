import requests, re
from bs4 import BeautifulSoup
from collections import deque
import urllib

def process_links(url: str , length: int = 100, email_type: str = ".") -> list:
    
    unprocessed_links = deque([url])

    processed_url = []
    emails  = set()

    count = 0

    
    while unprocessed_links:
        count += 1
        if count == length:
            break

        url = unprocessed_links.popleft()
        processed_url.append(url)
        # print("urls: %s" %url)

        parts = urllib.parse.urlsplit(url)
        base = f"{parts.scheme}://{parts.netloc}"
        path = url[:url.rfind("/")+1] if "/" in parts.path else url
        print(path)
        
        if url.startswith("https://"):
            url = url
        else:
            url = "https://"+url

        try:
            response = requests.get(url, timeout=10)
        except:
            pass

        print(f"[{count}]**  processing link: [{url}] **status: [{response.status_code}] ")


        new_email = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
        emails.update(new_email)

        soup = BeautifulSoup(response.text, "html.parser")


        for anchor in soup.find_all("a"):
            link =  anchor.attrs["href"] if "href" in anchor.attrs else ""
            if link.startswith("/"):
                link = base + link
            if not link.startswith("http"):
                link = path + link
            if not link in unprocessed_links or not link in processed_url:
                if "youtube" in link or "payments" in link or "myaccount.google.com" in link or "support.google.com" in link or "policies" in link or "payments" in link:
                    pass
                else:
                    unprocessed_links.append(link)
                

    return emails



def main(url: str):

    

    # queue of urls to be crawled
    unprocessed_urls = deque([])

    # set of already crawled urls for email
    processed_urls = set()

    mail = process_links(url)
    print(mail)



main("https://www.google.com/search?q=company+real+estate+washington+%40hotmail.com&sxsrf=ALiCzsZ7w7ytJXycC2WcdNXH_C7_RwAnLQ%3A1669986008415&ei=2PaJY5nvGK3P7_UPvfSJ8AY&oq=com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgQIIxAnMgQIIxAnMgQIIxAnMgQIABBDMgsIABCABBCxAxCDATIRCC4QgAQQsQMQgwEQxwEQ0QMyEQguEIAEELEDEIMBEMcBENEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCAguEIAEELEDOgcIIxDqAhAnOgUIABCABDoICC4QsQMQgwFKBAhBGABKBAhGGABQAFjjJGDXQ2gBcAF4AIAB-gWIAbsQkgEFNS0xLjKYAQCgAQGwAQrAAQE&sclient=gws-wiz-serp")







