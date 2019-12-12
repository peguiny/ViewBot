import hashlib
import requests
import random
import time
import ctypes
from time import sleep
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ctypes.windll.kernel32.SetConsoleTitleW(f"Pegu's View Bot")


def proxy(x,sleep_interval,url1):
    ip_addresses = [line.rstrip('\n') for line in open('proxies.txt')]
    views = 0
    headers= {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
    ip_addresses = [line.rstrip('\n') for line in open('proxies.txt')]

    for n in x:
        try:
            proxy_index = random.randint(0, len(ip_addresses) - 1)
            proxies = {"http": ip_addresses[proxy_index], "https": ip_addresses[proxy_index]}
            print("Trying ", proxies)
            r = requests.get(url1, proxies=proxies,headers = headers,verify=False, timeout=10)
            time.sleep(sleep_interval)

            views += 1
            print("View count: " + str(views))
        except:
            print("Invalid proxy")
            del ip_addresses[proxy_index]

def no_proxy(x,sleep_interval,url1):
    headers= {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
    views = 0
    for n in x:
        #try:
        r = requests.get(url1,headers = headers,verify=False, timeout=10)
        time.sleep(sleep_interval)

        views += 1
        print("View count: " + str(views))
        #except:
            #print("Timed out")

print("Use Proxies? (HTTPS)")
use_proxy = input("[1]Yes \n[2]No\n")
if use_proxy == "1":
    print("Using Proxies(HTTPS)\n")
elif use_proxy == "2":
    print("Not using Proxies\n")
else:
    print("Wrong Input!")
    time.sleep(3)
    exit()
    
url1 = str(input("URL: "))
val = int(input("Number of views: "))
sleep_interval = int(input("Time between each view: (Seconds)\n"))

x = range(val)

if use_proxy == "1":
    proxy(x,sleep_interval,url1)
elif use_proxy == "2":
    no_proxy(x,sleep_interval,url1)
else:
    exit()

