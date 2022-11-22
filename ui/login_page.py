from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        """Set the driver.

        keyword arguments:
        browser -- The driver for setup and tear down(Chrome driver until updated)
        """
        self.browser = browser

    username_input = (By.NAME, "USERNAME")
    password_input = (By.NAME, "PASSWORD")
    login_btn = (By.CSS_SELECTOR, "input.loginButton")

    def enter_username(self, username):
        """Enter username.

        keyword arguments:
        username -- the username for login
        """
        user_name = self.browser.find_element(*self.username_input)
        user_name.send_keys(username)

    def enter_password(self, password):
        """Enter password.

        keyword argument:
        password -- the password for login
        """
        passwd = self.browser.find_element(*self.password_input)
        passwd.send_keys(password)

    def login(self):
        """Click on login button."""
        self.browser.find_element(*self.login_btn).click()

    def assert_title(self, title):
        """Assert the title.

        keyword arguments:
        The string to assert title with
        """
        assert self.browser.title == title


