import unittest

from src.topics import Topics
from src.user import User
from src.article import Article
from src.controller import get_all_articles, get_random

class IntegrationTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 1)
    
    #TODO: a few integration tests (2-3) that use multiple classes and functions