from selenium.webdriver.firefox.webdriver import WebDriver

from django.test import LiveServerTestCase

import sys


class MyTestCase(LiveServerTestCase):
    """ """
    fixtures = [
        'auth_User.json',
        'human_res.json',
    ]

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        cls.driver.implicitly_wait(3)
        super(MyTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(MyTestCase, cls).tearDownClass()
