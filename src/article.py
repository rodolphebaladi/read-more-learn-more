class Article:

    def __init__(self, title, topic, url):
        self.title = title
        self.topic = topic
        self.url = url
    
    def get_title(self):
        return self.title
    
    def get_topic(self):
        return self.topic
    
    def get_url(self):
        return self.url
    
    def __eq__(self, other):
        return (
            type(self) == type(other) 
            and self.title == other.title
            and self.topic == other.topic
            and self.url == other.url 
        )
    
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))