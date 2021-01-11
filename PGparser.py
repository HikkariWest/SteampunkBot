from requests import get
from bs4 import BeautifulSoup
from urllib.request import urlopen

# def get_html(url):
# 	r = requests.get(url)
# 	return r.text

# def get_all_links(html):
# 	soup = BeautifulSoup(html, 'lxml')
# 	divs = soup.find('div', class_="post-content").find_all('div', class_="post-title")
# 	links = []

# 	for div in divs:
# 		a = div.find('a').get('href')
# 		links.append(a)

# 	return links


# def main():
# 	url = 'https://www.playground.ru/news'

# 	all_links = get_all_links(get_html(url))

# 	for i in all_links:
# 		print(i)


# get_html('https://www.playground.ru/news')
# main()

url = get('https://www.playground.ru/news').content
soup = BeautifulSoup(url, 'html.parser')
# div = soup.find_all('div', class_='post-title')
div = soup.find_all("div", {"class":"post-title"})
a = []
for link in div:
	# url_links = link.find('a').attrs['href']
	a.append(link.find('a')["href"])

for i in range(int(len(a))):
	url = get(a[i]).content
	soup = BeautifulSoup(url, 'html.parser')
	h1=soup.h1.text
	p=soup.p.text
    # сохранить файл
	file_1 = open(f"playground/playgroundnews{str(i)}.txt", "w",encoding="utf-8")
	file_1.write(h1+"\n \n"+p)
	file_1.close()

print("Работа заверщена , все данные сохраненены в txt фалы ")



# for links_news in list_links:
# 	with urlopen(links_news) as page:
# 		links_news = page.read().decode()

# article_soup = BeautifulSoup(links_news, 'html.parser')
# name = article_soup.find('h1').text.strip()
# paragraph1 = article_soup.find('div', class_ = "article-content js-post-item-content").find_all('p')
# article_text = [x.get_text() for x in paragraph1['p']]
# data = {'name' : name,'paragraph1' : paragraph1}


# i = 0
# for site in list_links:
# 	f_name = "playgroundnews" + str(i)
# 	i+=1
# 	with open(f'playground/{f_name}.txt', 'w', encoding = 'utf-8') as file:
# 		file.write(data['name'] + '\n')
# 		for x in data['paragraph1']:
# 			file.write('\n' + x.get_text())

