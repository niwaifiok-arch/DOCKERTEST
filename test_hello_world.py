import unittest
from hello_world import app

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_greeting_endpoint(self):
        response = self.app.get('/greeting')
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()