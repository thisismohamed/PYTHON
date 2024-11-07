import requests
from bs4 import BeautifulSoup

url = "https://python.org"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
