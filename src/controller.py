import requests
from bs4 import BeautifulSoup
from topics import Topics

# List topics enumeration to user and ask to add to favorites
def get_user_input_topics():
    # TODO: make sure two topics are not repeated
    exists_input = True
    list_of_topics = []
    prompt_topic = str("Please enter a topic (number) you are interested in from the selection below:\n" + 
                    "1. ENTERTAINMENT AND POP CULTURE\n" +
                    "2. GEOGRAPHY AND TRAVEL\n" +
                    "3. HEALTH AND MEDICINE\n" +
                    "4. LIFESTYLES AND SOCIAL ISSUES\n" +
                    "5. LITERATURE\n" +
                    "6. PHILOSOPHY AND RELIGION\n" +
                    "7. POLITICS, LAW AND GOVERNMENT\n" +
                    "8. SCIENCE\n" +
                    "9. SPORTS AND RECREATION\n" +
                    "10. TECHNOLOGY\n" +
                    "11. VISUAL ARTS\n" +
                    "12. WORLD HISTORY\n" +
                    "Enter a number: ")
    while (exists_input):
        topic = input(prompt_topic)
        if (not topic.isnumeric()):
            print("\nPlease provide a number!\n") 
        elif (int(topic) < 1 or int(topic) > 13):
            print("\nInvalid number, please provide a number between 1 and 13!\n")
        else:
            list_of_topics.append(int(topic))
            more_input = input("Would you like to provide another topic? (yes/no) ")
            if (more_input != 'yes'):
                exists_input = False
    return list_of_topics


def get_all_articles(topic):
    articles = set()

    topic_string = Topics(topic)
    str0 = str(topic_string).lower()
    str1 = str0[7:]
    str2 = str1.replace("_", " ")
    str3 = str2.replace("and ", "")
    str4 = str3.title()
    endpoint = str4.replace(" ", "-")
    print (endpoint)

    # Fetch all articles for topic (web scrape), returns a set

    response = requests.get(
        url="https://www.britannica.com/browse/" + endpoint, timeout=10
    )
    
    soup = BeautifulSoup(response.content, 'html.parser')
    for a in soup.find_all('a', href=True):
        is_story = a['href'].startswith('/story/') or a['href'].startswith('/list/')
        if is_story:
            title = a.text
            if title is not None:
                title = title.strip()
                if (title != "" and title != "Lists"):
                    articles.add(title)
    
    print(articles)
    return None


def get_random(articles):
    articles.use()
    # Select a random article from set and remove it from the set
    return 1
