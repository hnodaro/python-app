from Home import *
import unittest

class HomeTest(unittest.TestCase):

    # Ensure function isUrl is working
    def test_isUrl(self):
        test_false=isUrl("sgdfhks")
        test_true=isUrl("https://nest.fr.aptoide.com/")
        self.assertEqual(test_false, False)
        self.assertEqual(test_true, True)
        
    # Ensure function isUp is working
    def test_isUp(self):
        test_false=isUp("https://nesfhgft.fr.aptoide.com/")
        test_true=isUp("https://nest.fr.aptoide.com/")
        self.assertEqual(test_false, False)
        self.assertEqual(test_true, True)

    # Ensure error when incorrect url
    def test_incorrect_url(self):
        tester=app.test_client(self)
        response=tester.post(
            '/',
            data=dict(url="wrongUrl")
        )
        self.assertIn(b'Please submit a valid aptoide URL', response.data)

    # Ensure error when website doesn't respond
    def test_up_site(self):
        tester=app.test_client(self)
        response=tester.post(
            '/',
            data=dict(url="https://negfdgst.fr.aptoide.com/")
        )
        self.assertIn(b'Error: Url', response.data)

    # Ensure behavior when good url
    def test_good_url(self):
        tester=app.test_client(self)
        response=tester.post(
            '/',
            data=dict(url="https://facebook.fr.aptoide.com/")
        )
        self.assertIn(b'Version', response.data)
        self.assertIn(b'Number of downloads', response.data)
        self.assertIn(b'Release date', response.data)
        self.assertIn(b'Description', response.data)

if __name__ == '__main__':
    unittest.main()
