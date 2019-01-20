import unittest
import services.scrapper

class ScrapperTest(unittest.TestCase):

    #Test scrapp function

    def test_scrapp(self):
        app=services.scrapper.AppScrapper.Scrapp("https://facebook.fr.aptoide.com/")
        self.assertEqual(app.name, "Facebook")
        self.assertTrue(app.version != None)
        self.assertTrue(app.downloadsNumber != None)
        self.assertTrue(app.description != None)
        self.assertTrue(app.release != None)

if __name__ == '__main__':
    unittest.main()
