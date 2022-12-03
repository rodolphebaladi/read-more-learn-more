import unittest
import validators

from src.topics import Topics
from src.user import User
from src.article import Article
from src.controller import get_all_articles, get_random

class IntegrationTests(unittest.TestCase):
    
    # Each topic should fetch at least 3 articles in that topic on average
    def test_fetching_of_articles_from_all_topics (self):
        articles = set()
        articles.update(get_all_articles(1, ext=True))
        articles.update(get_all_articles(2, ext=True))
        articles.update(get_all_articles(3, ext=True))
        articles.update(get_all_articles(4, ext=True))
        articles.update(get_all_articles(5, ext=True))
        articles.update(get_all_articles(6, ext=True))
        articles.update(get_all_articles(7, ext=True))
        articles.update(get_all_articles(8, ext=True))
        articles.update(get_all_articles(9, ext=True))
        articles.update(get_all_articles(10, ext=True))
        articles.update(get_all_articles(11, ext=True))
        articles.update(get_all_articles(12, ext=True))
        self.assertGreater(len(articles), 36)

    def test_validity_of_article_url(self):
        articles = get_all_articles(1, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_2(self):
        articles = get_all_articles(2, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_3(self):
        articles = get_all_articles(3, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_4(self):
        articles = get_all_articles(4, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))
    
    def test_validity_of_article_url_5(self):
        articles = get_all_articles(5, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))
    
    def test_validity_of_article_url_6(self):
        articles = get_all_articles(6, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_7(self):
        articles = get_all_articles(7, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_8(self):
        articles = get_all_articles(8, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_9(self):
        articles = get_all_articles(9, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_10(self):
        articles = get_all_articles(10, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_11(self):
        articles = get_all_articles(11, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))

    def test_validity_of_article_url_12(self):
        articles = get_all_articles(12, ext=True)
        article = get_random(articles)
        self.assertTrue(validators.url(article.get_url()))        