class User:

    def __init__(self):
        self.favorite_topics = []
        self.articles_history = []

    def set_favorite_topics(self, topics):
        if not isinstance(topics, list):
            raise TypeError("topics argument expected to be instance of List.")
        self.favorite_topics = topics

    def add_article_to_history(self, article):
        if isinstance(article, list):
            raise TypeError("article argument does not expect a List.")
        self.articles_history.append(article)

    def get_favorite_topics(self):
        return self.favorite_topics

    def get_articles_history(self):
        return self.articles_history
