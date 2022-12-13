from selenium.webdriver.common.action_chains import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Get current URL method"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current URL: ' + get_url)

    """Text assertion method"""
    def assert_text(self, text, result):
        text_value = text.text
        assert text_value == result
        print('Text assertion PASSED')

    """ActionChains"""
    def actions(self):
        actions = ActionChains(self.driver)
        return actions
