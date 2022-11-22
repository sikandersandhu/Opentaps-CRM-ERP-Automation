from selenium.webdriver.common.by import By


class Menu:
    def __init__(self, browser):
        """Set the driver.

        keyword arguments:
        browser -- The driver for setup and tear down(Chrome driver until updated)
        """
        self.browser = browser

    def open(self, menu_name):
        """Open requested page from top menu.

        keyword arguments:
        menu_name -- Name of the page to open
        """
        css_selector_expression = "a[href='/crmsfa/control/" + menu_name + "']"
        self.browser.find_element(By.CSS_SELECTOR, css_selector_expression).click()
