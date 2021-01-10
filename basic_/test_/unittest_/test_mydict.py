import unittest

from basic_.test_.src import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        # a test case
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        # a test case
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    @unittest.skip("this test case will be skipped")
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        # run before every test case
        print("setup test case")

    def tearDown(self):
        # run after every test case
        print("teardown test case")

    @classmethod
    def setUpClass(cls):
        # run before all test cases
        print("setUp prerequisite data...")

    @classmethod
    def tearDownClass(cls):
        # run after all test cases
        print("tearDown prerequisite data...")


if __name__ == '__main__':
    unittest.main()
