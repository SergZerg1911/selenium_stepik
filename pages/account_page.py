from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    men_tab = '//a[@title="Мужчины"]'
    jeans_tab = '//li[@class="level3 catli-982"]'

    # Getters
    def get_men_tab(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.men_tab)))

    def get_jeans_tab(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.jeans_tab)))

    # Methods
    def go_to_men_jeans(self):
        self.actions().move_to_element(self.get_men_tab()).perform()
        self.get_jeans_tab().click()
        print('Click "Jeans" tab')
