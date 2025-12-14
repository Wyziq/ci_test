import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.testing = True
        self.client = tested_app.app.test_client()

    def test_calc_success_add_positive(self):
        r = self.client.get('/calc?op=add&a=5&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'8.0')
    
    def test_calc_success_add_negative(self):
        r = self.client.get('/calc?op=add&a=-5&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'-2.0')
    
    def test_calc_success_sub_positive(self):
        r = self.client.get('/calc?op=sub&a=5&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'2.0')
    
    def test_calc_success_sub_negative(self):
        r = self.client.get('/calc?op=sub&a=-5&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'-8.0')

if __name__ == '__main__':
    unittest.main()