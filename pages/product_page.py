import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    size_choose = '//*[@id="product-options-wrapper"]/div/div[2]/div/div/label[2]/span'
    add_to_cart_btn = '//button[@id="product-addtocart-button"]'
    go_to_cart_btn = '//a[@class="primary"]'
    to_checkout = '//*[@id="app"]/div[1]/div[2]/div[2]/button'

    # Getters
    def get_size_choose(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.size_choose)))

    def get_add_to_cart_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_btn)))

    def get_go_to_cart_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_btn)))

    def get_go_to_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.to_checkout)))

    # Methods
    def click_size_choose(self):
        self.get_size_choose().click()
        print('Click size button')

    def click_add_to_cart_btn(self):
        self.get_add_to_cart_btn().click()
        print('Click "Add to cart" button')

    def click_go_to_cart_btn(self):
        self.get_go_to_cart_btn().click()
        print('Click "Go to cart" button')

    def click_go_to_checkout(self):
        self.get_go_to_checkout().click()
        print('Click "Go to checkout"')

    def go_to_checkout(self):
        self.get_current_url()
        self.click_size_choose()
        self.click_add_to_cart_btn()
        self.click_go_to_cart_btn()
        self.click_go_to_checkout()