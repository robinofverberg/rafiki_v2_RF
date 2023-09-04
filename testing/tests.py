from os import getcwd, path
from time import sleep
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWebsite(TestCase):
    # settings for how the tests are run
    dontclosebrowser = (
        True  # if True browser stays open after tests are run, otherwise browser closes
    )
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
        self.browser.get(
            "about:blank"
        )  # goes to an empty page to avoid earlier tests affecting current test

    # tests start here
    def testCompanyName(self):
        # opens the file index.html in project root directory
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Rafiki", self.browser.page_source)

    def testSlogan(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn(
            "--- Äkta napolitansk pizza sedan 2017 ---", self.browser.page_source
        )

    def testTitle(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Pizzeria Rafiki", self.browser.title)

    def testPhoneNumber(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("0630-555-555", self.browser.page_source)

    def testMail(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("info@ntig-uppsala.github.io", self.browser.page_source)

    def testAddress(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("Kungsvägen 2B 642 34 Flen", self.browser.page_source)

    def testFacebook(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("https://www.facebook.com/ntiuppsala/", self.browser.page_source)

    def testInstagram(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("https://www.instagram.com/ntiuppsala/", self.browser.page_source)

    def testTwitter(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn("https://twitter.com/ntiuppsala", self.browser.page_source)

    def testOpenHoursButton(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.ID, "openHoursButton").click()
        self.assertIn("#oppettider", self.browser.current_url)

    def testFindUs(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.ID, "findUsButton").click()
        self.assertIn("#hittaoss", self.browser.current_url)

    def testOpenHours(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        paragraph = self.browser.find_element(By.ID, "openHoursInfo")
        self.assertIn("Mån - Tors 10-22", paragraph.text)
        self.assertIn("Fredagar 10-23", paragraph.text)
        self.assertIn("Lördagar 12-23", paragraph.text)
        self.assertIn("Söndagar 12-20", paragraph.text)

    def testFooterLinks(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        footer = self.browser.find_element(By.CLASS_NAME, "footer")
        self.assertIn("Öppettider", footer.text)
        self.assertIn("Hitta oss", footer.text)
        self.assertIn("Rafiki", footer.text)

    def testHomePage(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.ID, "nav-Logo").click()
        self.assertIn("#home", self.browser.current_url)

    def testFooterDesc(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        footer = self.browser.find_element(By.CLASS_NAME, "footer")
        self.assertIn(
            "Sedan 2017 har vi gjort lyxiga napolitanska pizzor i hjärtat av Flen.",
            footer.text,
        )
        self.assertIn("PIZZERIA RAFIKI", footer.text)
        self.assertIn("KONTAKTA OSS", footer.text)

    def testFooterContactInfo(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        footer = self.browser.find_element(By.CLASS_NAME, "footer")
        self.assertIn("Kungsvägen 2B 642 34 Flen", footer.text)
        self.assertIn("0630-555-555", footer.text)
        self.assertIn("info@ntig-uppsala.github.io", footer.text)

    def testGoogleMaps(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.assertIn(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2051.931861647693!2d16.591982477839476!3d59.04985333335932!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x465ec4abc74e82c5%3A0x4642c0225f90c202!2sKungsv%C3%A4gen%202%2C%20642%2034%20Flen!5e0!3m2!1ssv!2sse!4v1693307415845!5m2!1ssv!2sse",
            self.browser.page_source,
        )
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        self.browser.get_screenshot_as_file("images/googleMapIMG.jpeg")


# exists to ensure tests run if file is run as a normal python-program
if __name__ == "__main__":
    main(verbosity=2)
