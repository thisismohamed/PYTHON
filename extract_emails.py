import http.client
import re
import sys

def extract_emails(domain):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", "/")
    response = conn.getresponse()
    html_content = response.read().decode('utf-8')

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, html_content)

    return sorted(set(emails), key=str.lower)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_emails.py <domain>")
        sys.exit(1)
    domain = sys.argv[1]
    results = extract_emails(domain)
    if results:
        print("\nEmails found on %s\n" % domain)
        for email in results:
            print(email)
    else:
        print("\nNo emails found on the given domain")
