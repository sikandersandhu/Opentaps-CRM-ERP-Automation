from selenium.webdriver.common.by import By


class LoginPage:
    url = 'http://leaftaps.com/crmsfa/control/logout'

    def __init__(self, browser):
        self.browser = browser

    username_input = (By.NAME, "USERNAME")
    password_input = (By.NAME, "PASSWORD")
    login_btn = (By.CSS_SELECTOR, "input.loginButton")

    def load(self):
        self.browser.get(self.url)

    def enter_username(self, username):
        user_name = self.browser.find_element(*self.username_input)
        user_name.send_keys(username)

    def enter_password(self, password):
        passwd = self.browser.find_element(*self.password_input)
        passwd.send_keys(password)

    def login(self):
        self.browser.find_element(*self.login_btn).click()

    def assert_title(self, title):
        assert self.browser.title == title
