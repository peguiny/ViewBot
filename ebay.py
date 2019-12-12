import requests
import random
import time

url1 = str(input("URL: "))
val1 = int(input("Number of views: "))
val = round(val1 / 5)

ip_addresses = [line.rstrip('\n') for line in open('proxies.txt')]

x = range(int(val))

for n in x:
    try:
        proxy_index = random.randint(0, len(ip_addresses) - 1)
        proxies = {"http": ip_addresses[proxy_index], "https": ip_addresses[proxy_index]}
        print("Trying ", proxies)
        r = requests.get(url1, proxies=proxies,verify=False, timeout=10)
        time.sleep(1)
        r = requests.get(url1, proxies=proxies,verify=False, timeout=10)
        time.sleep(1)
        r = requests.get(url1, proxies=proxies,verify=False, timeout=10)
        time.sleep(1)
        r = requests.get(url1, proxies=proxies,verify=False, timeout=10)
        time.sleep(1)
        r = requests.get(url1, proxies=proxies,verify=False, timeout=10)
        print(n)
        time.sleep(60)
    except:
        print("Invalid")
        del ip_addresses[proxy_index]


while True:
    sleep(0.1)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Pegu View Bot| Views done: {str(n)}")
