import my_app
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        my_app.app.config['TESTING'] = True
        self.client = my_app.app.test_client()

    def test_hi(self):
        response = self.client.get('/hi/')
        self.assertEqual(response.data, 'Hi there')

if __name__ == '__main__':
    unittest.main()
