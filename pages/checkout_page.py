import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    delivery_checkbox = '//div[@class="selection"]'
    save_btn = '//button[@class="action tertiary"]'
    payment_checkbox = '//*[@id="checkout-container"]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/label'
    policy_checkbox = '//div[@class="field cms-agreement"]'
    confirm_btn = '//button[@class="action apply primary"]'
    back_to_shop = '//*[@id="maincontent"]/div[2]/div/div/div/div[2]/a'

    # Getters
    def get_delivery_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delivery_checkbox)))

    def get_save_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.save_btn)))

    def get_payment_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.payment_checkbox)))

    def get_policy_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.policy_checkbox)))

    def get_confirm_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm_btn)))

    def get_back_to_shop(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.back_to_shop)))

    # Methods
    def click_delivery_checkbox(self):
        self.get_delivery_checkbox().click()
        print('Click delivery checkbox')

    def click_save_btn(self):
        self.get_save_btn().click()
        print('Click save button')

    def click_payment_checkbox(self):
        self.get_payment_checkbox().click()
        print('Click payment button')

    def click_policy_checkbox(self):
        self.get_policy_checkbox().click()
        print('Click policy button')

    def click_confirm_btn(self):
        self.get_confirm_btn().click()
        print('Click confirm button')

    def click_back_to_shop(self):
        self.get_back_to_shop().click()
        print('Click back button')

    def proceed_to_checkout(self):
        # self.click_delivery_checkbox()
        # self.click_save_btn()
        self.click_payment_checkbox()
        self.click_policy_checkbox()
        self.click_confirm_btn()
        self.click_back_to_shop()
        time.sleep(3)