import requests
import time

url = "http://localhost:8000/hostname"
while True:
    r = requests.get(url)
    print()
    print(r.text + "\n")
    time.sleep(0.001)
