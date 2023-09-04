from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path, getcwd
from selenium.webdriver.common.by import By

class TestWebsite(TestCase):

    # settings for how the tests are run
    dontclosebrowser = True  # if True browser stays open after tests are run, otherwise browser closes
    hidewindow = False  # if False shows browser while tests run

    # setUpClass runs BEFORE FIRST test
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.dontclosebrowser:
            chr_options.add_experimental_option("detach", True)

        if cls.hidewindow:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    # tearDownClass runs AFTER LAST TEST
    @classmethod
    def tearDownClass(cls):
        pass  # does nothing

    # setUp runs BEFORE EVERY TEST
    def setUp(self):
        pass  # does nothing

    # tearDown runs AFTER EVERY TEST
    def tearDown(self):
        self.browser.get('about:blank')  # goes to an empty page to avoid earlier tests affecting current test

    # tests start here
    def testCompanyName(self):
        # opens the file index.html in project root directory
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Rafiki", self.browser.page_source)

    def testSlogan(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("--- Äkta napolitansk pizza sedan 2017 ---", self.browser.page_source)

    def testTitle(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Pizzeria Rafiki", self.browser.title)

    def testPhoneNumber(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("0630-555-555", self.browser.page_source)

    def testMail(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("info@ntig-uppsala.github.io", self.browser.page_source)

    def testAddress(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Kungsvägen 2B 642 34 Flen", self.browser.page_source)

    def testFacebook(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("https://www.facebook.com/ntiuppsala/", self.browser.page_source)

    def testInstagram(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("https://www.instagram.com/ntiuppsala/", self.browser.page_source)

    def testTwitter(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("https://twitter.com/ntiuppsala", self.browser.page_source)

    def testOpenHoursButton(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.browser.find_element(By.ID, 'openHoursButton').click()
        self.assertIn("#oppettider", self.browser.current_url)

    def testFindUs(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.browser.find_element(By.ID, 'findUsButton').click()
        self.assertIn("#hittaoss", self.browser.current_url)

    def testOpenHours(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        paragraph = self.browser.find_element(By.ID, 'openHoursInfo')
        self.assertIn("Mån - Tors 10-22", paragraph.text)
        self.assertIn("Fredagar 10-23", paragraph.text)
        self.assertIn("Lördagar 12-23", paragraph.text)
        self.assertIn("Söndagar 12-20", paragraph.text)

# exists to ensure tests run if file is run as a normal python-program
if __name__ == '__main__':
    main(verbosity=2)