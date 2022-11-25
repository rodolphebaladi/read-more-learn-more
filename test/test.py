import unittest
class SomeTests(unittest.TestCase):

    def setUp(self):
        pass # runs before all test cases

    def tearDown(self):
        pass # runs after all test cases

    def test_case_1_one_equals_one(self):
        self.assertEqual(1, 1)
        
    def test_case_2_None_is_None(self):
        '''This comment will appear in the test output'''
        self.assertIsNone(None)

    def test_case_3_raise_and_catch_error(self):
        with self.assertRaises(ValueError):
            raise ValueError('This is an error message')




if __name__ == '__main__':
    # unitest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTests)
    unittest.TextTestRunner(verbosity=2).run(suite)