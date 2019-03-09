from bs4 import BeautifulSoup
import urllib.request


soup = BeautifulSoup(urllib.request.urlopen('https://en.wikipedia.org/wiki/Google'), features="html.parser")

for script in soup.find_all('script'):
    script.extract()


i = soup.find_all('p')
for p in i:
    print(p.get_text(strip=True), file=open("output.txt", "a"))

