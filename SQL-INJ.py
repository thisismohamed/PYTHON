import os
try:
    import pyfiglet
except ImportError:
    os.system('pip install pyfiglet')
    import pyfiglet
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    import webbrowser
try:
    from googlesearch import search
except ImportError:
    os.system('pip install google')
    from googlesearch import search

banner = pyfiglet.figlet_format("SQL INJ")
print(banner)

query_param = "php?id=1"
injection_test = "'"

for url in search(query_param, stop=100):
    try:
        req = requests.get(url+injection_test)
        error_msg = "your SQL"
        if error_msg in req.text:
            print("SQL Vulnrable Injection")
            print("SQL Vulnrable Injection URL: ", url)
            webbrowser.open(url)
            user_input = input("Do you compliet? Y/n: ").strip().lower()
            if user_input == 'y':
                break
        else:
            print("No SQL Vulnrability Injection found")
    except requests.exceptions.RequestException as error:
        print(error)
