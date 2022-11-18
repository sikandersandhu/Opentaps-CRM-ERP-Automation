import pytest
from selenium.webdriver import Chrome
from ui.login_page import LoginPage


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(browser):
    # setup
    loginpage = LoginPage(browser)
    logingpage_title = 'opentaps CRM'
    homepage_title = 'My Home | opentaps CRM'

    # assert
    loginpage.load()
    loginpage.assert_title(logingpage_title)

    # act
    loginpage.enter_username('demosalesmanager')
    loginpage.enter_password('crmsfa')
    loginpage.login()

    # assert
    loginpage.assert_title(homepage_title)

