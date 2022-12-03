import requests, re
from bs4 import BeautifulSoup
from collections import deque
import urllib

def process_links(url: str , length: int = 10, email_type: str = ".") -> list:
    
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

    mails = process_links(url)

    for mail in mails :
        with open("mails.txt", "a") as f:
            f.write(mail+"\n")
    
    print("files has been added to mail.txt")
    



main("https://www.google.com/search?q=truck+contract+of+kent+email+%22%40hotmail.com%22+%40outlook.com%22-issuu+-scam&oq=truck+contract+of+kent+email+%22%40hotmail.com%22+%40outlook.com%22-issuu+-scam&aqs=chrome..69i57.120518j0j7&sourceid=chrome&ie=UTF-8")







