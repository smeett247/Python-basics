import requests
import time
from fake_useragent import UserAgent


url = "https://www.jpmorganchase.com/"


session = requests.Session()

headers = {
    "User-Agent": UserAgent().random,
    "Acceot-language" : "en-US, en;q=0.9",
    "Accept-Encoding" : "gzip,deflate,br",
    "Connection" : "keep-alive",
    "Referer": "http://www.google.com"

}

time.sleep(2)  # delay for 2 seconds to simulate real-world conditions

r = session.get(url)

print(r.text)

with open("file.md", "w") as f:
    f.write(r.text)