from bs4 import BeautifulSoup
from urllib.request import urlopen

class Akipress:
    url = "https://akipress.org"

    def open_page(url):
    	with urlopen(url) as page:
    		html = page.read().decode()
    		return html

    def search_tag(tag):
    	soup = BeautifulSoup(open_page(url), 'html.parser')
    	links = soup.find_all(tag)
    	return links

    def get_data(cls, tagTitle, tagText):
    		article_soup = BeautifulSoup(open_page(url), 'html.parser')
    		title = article_soup.find(tagTitle).get_text()
    		text = article_soup.find('div', class_ = cls).find_all(tagText)
    		article_text = [x.get_text() for x in text]
    		data = {
    			'title': title,
    			'text-parser': text
    			}
    		return data

    for link in search_tag('a'):
    	if 'tazabek.kg/news' in link.get('href'):
    		url = 'https://' + link.get('href').replace('http://', '').replace('//', '')

    		with open('tazabek.txt', 'a', encoding = 'utf-8') as file:
    			file.write(get_data('lenta-row', 'h2', 'p')['title'] + '\n')

    			for x in get_data('lenta-row', 'h2', 'p')['text-parser']:
    				file.write(x.get_text() +'\n')

    	elif 'turmush.kg/ru/news' in link.get('href'):
    		url = 'https://' + link.get('href').replace('http://', '').replace('//', '')

    		with open('turmush.txt', 'a', encoding = 'utf-8') as file:
    			file.write(get_data('colored-link-text', 'h1', 'p')['title'] + '\n')

    			for x in get_data('colored-link-text', 'h1', 'p')['text-parser']:
    				file.write(x.get_text() +'\n')
