from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path, getcwd


class TestHemsida(TestCase):

    # settings for how the tests are run
    stangintebrowsern = True  # if True browser stays open after tests are run, otherwise browser closes
    gomfonstret = False  # if False shows browser while tests run

    # setUpClass runs BEFORE FIRST test
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.stangintebrowsern:
            chr_options.add_experimental_option("detach", True)

        if cls.gomfonstret:
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


    # TESTS START HERE
    def testCompanyName(self):
        # opens the file index.html in project root directory
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Rafiki", self.browser.page_source)

    def testSlogan(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("--- Äkta Napoliansk Pizza Sedan 2017 ---", self.browser.page_source)

    def testTitle(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Pizzeria Rafiki", self.browser.title)

# exists to ensure tests run if file is run as a normal python-program
if __name__ == '__main__':
    main(verbosity=2)