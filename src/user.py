class User:

    def __init__(self):
        self.favorite_topics = []
        self.articles_history = []

    def set_favorite_topics(self, topics):
        self.favorite_topics = topics
    
    def add_article_to_history(self, article):
        self.articles_history.append(article)
    
    def get_favorite_topics(self):
        return self.favorite_topics
    
    def get_articles_history(self):
        return self.articles_history
