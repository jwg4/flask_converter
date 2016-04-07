import my_app
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        my_app.app.config['TESTING'] = True
        self.client = flaskr.app.test_client()

    def test_hi(self):
        response = self.client.get('/hi/')
        assertIsEqual(response.data, 'Hi there')

if __name__ == '__main__':
    unittest.main()
