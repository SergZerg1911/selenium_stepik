import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    continue_button = '//span[text()="Продолжить"]'
    cookie_agree_btn = '//a[@aria-label="dismiss cookie message"]'
    account_icon = '//div[@class="btn-account-notlogged"]'
    email_field = '//input[@id="email"]'
    password_field = '//input[@id="pass"]'
    enter_btn = '//button[@id="send2"]'
    text_to_assert = '//div[@class="block-title"]'

    # Getters
    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_cookie_agree_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookie_agree_btn)))

    def get_account_icon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.account_icon)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_enter_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_btn)))

    def get_text_to_assert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.text_to_assert)))

    # Methods
    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click "Continue" button')

    def click_cookie_agree_btn(self):
        self.get_cookie_agree_btn().click()
        print('Click "Cookie" button')

    def click_account_icon(self):
        self.get_account_icon().click()
        print('Click "Account" icon')

    def fillout_email(self, email):
        self.get_email_field().send_keys(email)
        print('Fill out email')

    def fillout_password(self, password):
        self.get_password_field().send_keys(password)
        print('Fillout password')

    def click_enter_btn(self):
        self.get_enter_btn().click()
        print('Click "Enter" button')

    def auth(self):
        self.driver.get('https://www.terranovastyle.ru/ru_ru/')
        self.driver.maximize_window()
        self.get_current_url()
        self.click_continue_button()
        self.click_cookie_agree_btn()
        self.click_account_icon()
        self.fillout_email('frigerator@bk.ru')
        self.fillout_password('Zth46cy!')
        self.click_enter_btn()
        self.assert_text(self.get_text_to_assert(), 'Здравствуйте, Mike!')

