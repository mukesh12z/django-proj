from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pyvirtualdisplay import Display
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        display = Display(visible=0, size=(1024, 768))

        display.start()
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        options = Options()
                
        #options.set_headless(headless=True)
        binary = FirefoxBinary('/mnt/c/Program Files/Mozilla Firefox/firefox.exe')
        options.binary = binary
        self.browser = webdriver.Firefox(firefox_options=options, capabilities=cap, firefox_binary=binary)
       # self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
        #self.browser.get('http://selenium.org/')
        print(self.browser.title)
    
    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)
    
    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_oof_css_property("color"), "rgbs(200, 50, 255, 1")

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
    
#if __name__ == "__main__":
#    unittest.main(warnings='ignore')