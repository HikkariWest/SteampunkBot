from requests import get
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = get('https://www.playground.ru/news').content
soup = BeautifulSoup(url, 'html.parser')
div = soup.find_all("div", {"class":"post-title"})
a = []
for link in div:
	a.append(link.find('a')["href"])

for i in range(int(len(a))):
    url = get(a[i]).content
	soup = BeautifulSoup(url, 'html.parser')
	h1=soup.h1.text
	p=soup.p.text
    # сохранить файл
	file_1 = open(f"playgroundnews{str(i)}.txt", "w",encoding="utf-8")
	file_1.write(h1+"\n \n"+p)
	file_1.close()

print("Работа заверщена , все данные сохраненены в txt фалы ")
