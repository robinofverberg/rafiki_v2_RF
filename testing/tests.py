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
        self.browser.maximize_window()

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

    def testMenuButton(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.ID, "menuButton").click()
        self.assertIn("#meny", self.browser.current_url)

    def testMenuPizza(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        menu = self.browser.find_element(By.ID, "meny")
        self.assertIn("Tomatsås och ost ingår i alla pizzor", menu.text)
        self.assertIn("Margherita", menu.text)
        self.assertIn("Vesuvio", menu.text)
        self.assertIn("Calzone", menu.text)
        self.assertIn("Capricciosa", menu.text)
        self.assertIn("Hawaii", menu.text)
        self.assertIn("Pompei", menu.text)
        self.assertIn("La Casa", menu.text)

    def testMenuIngredients(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        menu = self.browser.find_element(By.ID, "meny")
        self.assertIn("Mozzarella", menu.text)
        self.assertIn("Ost, skinka", menu.text)
        self.assertIn("Inbakad med skinka", menu.text)
        self.assertIn("Skinka, champinjoner", menu.text)
        self.assertIn("Skinka, ananas", menu.text)
        self.assertIn("Bacon, rödlök, ägg, curry", menu.text)
        self.assertIn("Champinjoner, räkor, skinka", menu.text)

    def testMenuPrices(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        menu = self.browser.find_element(By.ID, "meny")
        self.assertIn("80 kr", menu.text)
        self.assertIn("85 kr", menu.text)
        self.assertIn("90 kr", menu.text)
        self.assertIn("95 kr", menu.text)

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
        self.assertIn("Hem", footer.text)
        self.assertIn("Öppettider", footer.text)
        self.assertIn("Meny", footer.text)
        self.assertIn("Hitta oss", footer.text)

    def testHomePage(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.find_element(By.ID, "nav-Logo").click()
        self.assertIn("#", self.browser.current_url)

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
        self.browser.get_screenshot_as_file("testIMG/googleMapIMG.jpeg")

    def testResSite1920(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.set_window_size(1920, 1080, self.browser.window_handles[0])
        self.browser.find_element(By.ID, "openHoursButton").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/1080P/OPENHOURS1080pIMG.jpeg")
        self.browser.find_element(By.ID, "findUsButton").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/1080P/FINDUS1080pIMG.jpeg")
        self.browser.find_element(By.ID, "nav-Logo").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/1080P/HOMEPAGE1080pIMG.jpeg")
        self.browser.find_element(By.ID, "menuButton").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/1080P/MENU1080pIMG.jpeg")

    def testResSite4k(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.set_window_size(2560, 1440, self.browser.window_handles[0])
        self.browser.find_element(By.ID, "openHoursButton").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/4K/OPENHOURS_4K_IMG.jpeg")
        self.browser.find_element(By.ID, "findUsButton").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/4K/FINDUS_4K_IMG.jpeg")
        self.browser.find_element(By.ID, "nav-Logo").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/4K/HOMEPAGE_4K_IMG.jpeg")
        self.browser.find_element(By.ID, "menuButton").click()
        sleep(1)
        self.browser.get_screenshot_as_file("testIMG/4K/MENU_4K_IMG.jpeg")

    def testResSiteIphone(self):
        self.browser.get(path.join(getcwd(), "index.html"))
        self.browser.set_window_size(390, 844, self.browser.window_handles[0])
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.browser.find_element(By.ID, "findUsFooter").click()
        sleep(2)
        self.browser.get_screenshot_as_file("testIMG/Phone/FINDUS_iPhone_IMG.jpeg")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.browser.find_element(By.ID, "openHoursFooter").click()
        sleep(2)
        self.browser.get_screenshot_as_file("testIMG/Phone/OPENHOURS_iPhone_IMG.jpeg")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.browser.find_element(By.ID, "homePageFooter").click()
        sleep(2)
        self.browser.get_screenshot_as_file("testIMG/Phone/HOME_iPhone_IMG.jpeg")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.browser.find_element(By.ID, "menuFooter").click()
        sleep(2)
        self.browser.get_screenshot_as_file("testIMG/Phone/menu_iPhone_IMG.jpeg")

    def testValidatorHTML(self):
        self.browser.get("https://validator.w3.org/#validate_by_upload")
        self.browser.find_element(By.ID, "uploaded_file").send_keys(
            path.join(getcwd(), "index.html")
        )
        self.browser.find_element(
            By.XPATH, '//*[@id="validate-by-upload"]/form/p[3]/a'
        ).click()
        self.assertIn("No errors or warnings to show", self.browser.page_source)

    def testValidatorCSS(self):
        self.browser.get("https://jigsaw.w3.org/css-validator/#validate_by_upload")
        self.browser.find_element(By.ID, "file").send_keys(
            path.join(getcwd(), "index.css")
        )
        self.browser.find_element(
            By.XPATH, '//*[@id="validate-by-upload"]/form/p[3]/label/a/span'
        ).click()
        self.assertIn("Gratulerar! Inga fel har hittats", self.browser.page_source)


# exists to ensure tests run if file is run as a normal python-program
if __name__ == "__main__":
    main(verbosity=2)
