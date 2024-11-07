import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            links = soup.find_all('a')
            link_urls = [link.get('href') for link in links]

            return link_urls
        else:
            raise requests.exceptions.RequestException(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as error:
        raise requests.exceptions.RequestException(f"Error: {str(error)}")

if __name__ == "__main__":
    url = "https://python.org"
    links = extract_links(url)
    if links:
        print(f"Links found on {url}")
        for link in links:
            print(link)
    else:
        print("No links found on the given url")
