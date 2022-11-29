'''Docstrings'''
import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://www.britannica.com/browse/Entertainment-Pop-Culture", timeout='10s'
)
soup = BeautifulSoup(response.content, 'html.parser')
for a in soup.find_all('a', href=True):
    isStory = a['href'].startswith('/story/') or a['href'].startswith('/list/')
    if isStory:
        title = a.text
        if title is not None:
            # if title.contains(' '):
            #     print ('nothing')
            print (title.strip())
