import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

def download_extract(url):
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        soup=BeautifulSoup(response.text,'html.parser')
        return {urljoin(url,a['href'])for a in soup.find_all('a',href=True)}
        
    except requests.RequestException as e:
        print(f"Error downloading{url}:{e}")
        return None

if __name__=="__main__":
    url="https://google.com"
    links=download_extract(url)
    print(f"Found {len(links)} links in {url}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        results=list(executor.map(download_extract,links))
    print(f"Downloaded: {sum(1 for r in results if r)}")

