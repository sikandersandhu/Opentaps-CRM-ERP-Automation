from selenium.webdriver.common.by import By


class Menu:

    def __init__(self, browser):
        self.browser = browser

    def open(self, menu_name):
        css_selector_expression = "a[href='/crmsfa/control/" + menu_name + "']"
        self.browser.find_element(By.CSS_SELECTOR, css_selector_expression).click()
