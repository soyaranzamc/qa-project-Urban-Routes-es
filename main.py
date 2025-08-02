import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data
from utils import UrbanRoutesPage, retrieve_phone_code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(5)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_set_phone(self):
        self.driver.get(data.urban_routes_url)
        self.page.set_route(data.address_from, data.address_to)
        self.page.set_flash()
        self.page.taxi_order()
        self.page.set_comfort()
        self.page.open_pop_up()
        self.page.set_phone_number()
        code = retrieve_phone_code(self.driver)
        self.page.set_code(code)

    def test_add_card(self):
        self.page.select_add_payment()
        self.page.assert_card_number(data.expected_card_text)

    def test_set_driver_message(self):
        self.page.set_driver_message()
        assert self.page.get_driver_message() == data.message_for_driver

    def test_blanket_and_icecream(self):
        self.page.order_blanket_and_tissues()
        self.page.add_ice_cream()

    @classmethod
    def teardown_class(cls):
        time.sleep(3)
        cls.driver.quit()

