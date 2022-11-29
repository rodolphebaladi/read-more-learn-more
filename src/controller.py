import requests
from bs4 import BeautifulSoup

def get_user_input_topics():
    # List topics enumeration to user and ask to add to favorites
    return []


def get_all_articles(topic):
    topic.use()
    # Fetch all articles for topic (web scrape), returns a set

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
    return None


def get_random(articles):
    articles.use()
    # Select a random article from set and remove it from the set
    return 1
