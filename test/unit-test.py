import unittest

from src.topics import Topics
from src.user import User
from src.article import Article
from src.controller import get_all_articles, get_random

class UnitTests(unittest.TestCase):

# ---- TOPICS unit tests ---- #
    def test_get_topic_by_value_first(self):
        self.assertEqual(Topics(1).name, "ENTERTAINMENT_AND_POP_CULTURE")
    
    def test_get_topic_by_value_last(self):
        self.assertEqual(Topics(12).name, "WORLD_HISTORY")
    
    def test_get_topic_by_value_invalid(self):
        with self.assertRaises(ValueError):
            Topics(-1).name
    
# ---- USER unit tests ---- #
    def test_create_user_default_fields(self):
        user = User()
        self.assertTrue(len(user.get_articles_history()) == 0)
        self.assertTrue(len(user.get_favorite_topics()) == 0)

    def test_user_articles_history(self):
        user = User()
        test_article = Article(None, None, None)
        user.add_article_to_history(test_article)
        self.assertListEqual([test_article], user.get_articles_history())
    
    def test_user_articles_history_invalid_list(self):
        user = User()
        test_invalid_article_list = ["test_article"]
        with self.assertRaises(TypeError):
            user.add_article_to_history(test_invalid_article_list)
    
    def test_user_favorite_topics(self):
        user = User()
        test_topics_list = ["test_topic"]
        user.set_favorite_topics(test_topics_list)
        self.assertListEqual(test_topics_list, user.get_favorite_topics())

    def test_user_favorite_topics_invalid_not_list(self):
        user = User()
        test_invalid_topics_list = "test_topic"
        with self.assertRaises(TypeError):
            user.set_favorite_topics(test_invalid_topics_list)
    
# ---- ARTICLE unit tests ---- #
    def test_create_article(self):
        test_title = "test_title"
        test_topic = Topics(1)
        test_url = "test_url"
        article = Article(test_title, test_topic, test_url)

        self.assertEqual(test_title, article.get_title())
        self.assertEqual(test_topic, article.get_topic())
        self.assertEqual(test_url, article.get_url())

    def test_compare_same_articles(self):
        article1 = Article("test_title", Topics(1), "test_url")
        article2 = Article("test_title", Topics(1), "test_url")
        self.assertEqual(article1, article2)

    def test_compare_different_articles(self):
        article1 = Article("test_title1", Topics(1), "test_url")
        article2 = Article("test_title", Topics(12), "test_url2")
        self.assertNotEqual(article1, article2)

# ---- CONTROLLER unit tests ---- #
    def test_get_random(self):
        test_set = {1, 2, 3}
        backup = test_set.copy()
        random_result = get_random(test_set)
        self.assertIn(random_result, backup)
        self.assertNotIn(random_result, test_set)

    #TODO: 2 tests for get_all_articles(topic)