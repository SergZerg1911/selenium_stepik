import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.account_page import AccountPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.men_jeans_page import MenJeansPage
from pages.product_page import ProductPage


def test_product_purchase():

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(15)
    driver.delete_all_cookies()
    print(driver.get_cookies())

    """User authorization"""
    main_page = MainPage(driver)
    main_page.auth()

    """Go to men jeans page"""
    acc_page = AccountPage(driver)
    acc_page.go_to_men_jeans()

    """Choose product"""
    men_jeans_page = MenJeansPage(driver)
    men_jeans_page.choose_product()

    """Go to checkout"""
    product_page = ProductPage(driver)
    product_page.go_to_checkout()

    """Proceed to checkout"""
    checkout_page = CheckoutPage(driver)
    checkout_page.proceed_to_checkout()
