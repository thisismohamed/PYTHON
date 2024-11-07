import requests
from bs4 import BeautifulSoup
import re

def extract_emails(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = set(re.findall(email_regex, str(soup)))

    return sorted(list(emails), key=str.lower)

if __name__ == "__main__":
    url = "https://tryhackme.com"
    results = extract_emails(url)
    if results:
        print("Emails found on %s" % url)
        for email in results:
            print(email)
    else:
        print("No emails found on the given url")
