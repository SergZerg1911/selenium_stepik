import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenJeansPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    text_to_assert = '//span[@data-ui-id="page-title-wrapper"]'
    filter = '//a[@class="filter-open js-filters-open"]'
    color_attribute = '//a[@data-attributevalue="Серый"]'
    season_attribute = '//a[@data-attributevalue="Осень"]'
    size_attribute = '//div[@data-option-label="42"]'
    discount_attribute = '//label[@for="tdy_discount_rangeFilter_option_6"]'
    price_slider_1 = '//a[@style="left: 0%;"]'
    price_slider_2 = '//a[@style="left: 100%;"]'
    apply_btn = '//button[@id="doApplyFilter"]'
    close_btn = '//div[@id="popuphomepage"]'
    product_tab = '//li[@id="productitemid-576428"]'

    # Getters
    def get_text_to_assert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.text_to_assert)))

    def get_filter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter)))

    def get_color_attribute(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.color_attribute)))

    def get_season_attribute(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.season_attribute)))

    def get_size_attribute(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.size_attribute)))

    def get_discount_attribute(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.discount_attribute)))

    def get_price_slider_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_1)))

    def get_price_slider_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_2)))

    def get_apply_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.apply_btn)))

    def get_product_tab(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_tab)))

    def get_close_btn(self):
        return WebDriverWait(self.driver, 3600).until(EC.element_to_be_clickable((By.XPATH, self.close_btn)))

    # Methods
    def click_filter(self):
        self.get_filter().click()
        print('Click "Filter" button')

    def choose_color_attribute(self):
        self.get_color_attribute().click()
        print('Click "Grey" checkbox')

    def choose_season_attribute(self):
        self.get_season_attribute().click()
        print('Click "Autumn" button')

    def choose_size_attribute(self):
        self.get_size_attribute().click()
        print('Click 42 size')

    def choose_discount_attribute(self):
        self.get_discount_attribute().click()
        print('Click "0-9%" discount')

    def slide_price_1(self):
        self.actions().move_to_element(self.get_price_slider_1()).click_and_hold().move_by_offset(10,
                                                                                                  0).release().perform()
        print('Slide price 1')

    def slide_price_2(self):
        self.actions().move_to_element(self.get_price_slider_2()).click_and_hold().move_by_offset(-10,
                                                                                                  0).release().perform()
        print('Slide price 2')

    def click_apply_btn(self):
        self.get_apply_btn().click()
        print('Click "Apply" button')

    def click_close_btn(self):
        self.get_close_btn().click()
        print('Click "Close" button')

    def click_product_tab(self):
        self.actions().move_to_element(self.get_product_tab())
        self.get_product_tab().click()
        print('Click on product tab')

    def choose_product(self):
        self.get_current_url()
        self.assert_text(self.get_text_to_assert(), 'Джинсы - Мужчины')
        self.click_filter()
        self.choose_color_attribute()
        self.choose_season_attribute()
        self.choose_size_attribute()
        self.choose_discount_attribute()
        self.actions().scroll_to_element(self.get_price_slider_1()).perform()
        self.slide_price_1()
        self.slide_price_2()
        # self.click_apply_btn()
        # self.click_close_btn()
        try:
            self.click_apply_btn()
            time.sleep(3)
        except StaleElementReferenceException:
            self.click_close_btn()
        self.click_product_tab()
        time.sleep(3)
