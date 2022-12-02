import sys
import unittest
import sys
import os

from src.topics import Topics

class UnitTests(unittest.TestCase):

    def setUp(self):
        pass # runs before all test cases

    def tearDown(self):
        pass # runs after all test cases

    # ---- TOPICS unit tests ---- #
    def test_get_topic_by_value(self):
        self.assertEqual(Topics(1), Topics.ENTERTAINMENT_AND_POP_CULTURE)
    
    def test_get_topic_by_value2(self):
        self.assertEqual(Topics(1), None)

    def test_get_topic_by_value3(self):
        self.assertEqual(1, 1)

    # ---- USER unit tests ---- #

    # ---- ARTICLE unit tests ---- #

    # ---- CONTROLLER unit tests ---- #
