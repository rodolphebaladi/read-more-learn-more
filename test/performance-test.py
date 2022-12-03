import unittest
import time

from src.topics import Topics
from src.user import User
from src.article import Article
from src.controller import get_all_articles, get_random

class PerformanceTests(unittest.TestCase):
    def test_web_scraping_time(self):
        t0 = time.time()
        get_all_articles(1, ext=True)
        t1 = time.time()
        total = t1-t0
        print ("1: " + str(total) + " ms")

        t0 = time.time()
        get_all_articles(2, ext=True)
        t1 = time.time()
        total2 = t1-t0
        print ("2: " + str(total2) + " ms")

        t0 = time.time()
        get_all_articles(3, ext=True)
        t1 = time.time()
        total3 = t1-t0
        print ("3: " + str(total3) + " ms")

        t0 = time.time()
        get_all_articles(4, ext=True)
        t1 = time.time()
        total4 = t1-t0
        print ("4: " + str(total4) + " ms")

        t0 = time.time()
        get_all_articles(5, ext=True)
        t1 = time.time()
        total5 = t1-t0
        print ("5: " + str(total5) + " ms")

        t0 = time.time()
        get_all_articles(6, ext=True)
        t1 = time.time()
        total6 = t1-t0
        print ("6: " + str(total6) + " ms")

        t0 = time.time()
        get_all_articles(7, ext=True)
        t1 = time.time()
        total7 = t1-t0
        print ("7: " + str(total7) + " ms")

        t0 = time.time()
        get_all_articles(8, ext=True)
        t1 = time.time()
        total8 = t1-t0
        print ("8: " + str(total8) + " ms")

        t0 = time.time()
        get_all_articles(9, ext=True)
        t1 = time.time()
        total9 = t1-t0
        print ("9: " + str(total9) + " ms")

        t0 = time.time()
        get_all_articles(10, ext=True)
        t1 = time.time()
        total10 = t1-t0
        print ("10: " + str(total10) + " ms")

        t0 = time.time()
        get_all_articles(11, ext=True)
        t1 = time.time()
        total11 = t1-t0
        print ("11: " + str(total11) + " ms")

        t0 = time.time()
        get_all_articles(12, ext=True)
        t1 = time.time()
        total12 = t1-t0
        print ("12: " + str(total12) + " ms")

        print ('Total Average Time:')
        total_all = (total+total2+total3+total4+total5+total6+total7+total8+total9+total10+total11+total12)/12
        print ("Average: " + str(total_all) + " ms")

