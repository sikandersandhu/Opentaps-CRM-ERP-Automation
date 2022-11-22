import pytest
from selenium.webdriver import Chrome
from ui.login_page import LoginPage
from ui.menu import Menu
from utility.constants import MainMenu


@pytest.fixture
def browser():
    """Configure the driver for setup and tear down."""
    url = 'http://leaftaps.com/crmsfa/control/logout'
    driver = Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(browser):
    login(browser)


def test_main_menus(browser):
    login(browser)

    menu = Menu(browser)
    menu.open(MainMenu.LEADS)
    menu.open(MainMenu.ACCOUNTS)
    menu.open(MainMenu.ACTIVITIES)
    menu.open(MainMenu.CASES)
    menu.open(MainMenu.CONTACTS)
    menu.open(MainMenu.FORECASTS)
    menu.open(MainMenu.MARKETING)
    menu.open(MainMenu.MY_HOME)
    menu.open(MainMenu.OPPORTUNITIES)
    menu.open(MainMenu.ORDERS)
    menu.open(MainMenu.PARTNERS)
    menu.open(MainMenu.QUOTES)
    menu.open(MainMenu.REPORTS)
    menu.open(MainMenu.TEAMS)
    

def login(browser):
    loginpage = LoginPage(browser)
    title_logingpg = 'opentaps CRM'
    title_homepg = 'My Home | opentaps CRM'

    # assert
    loginpage.assert_title(title_logingpg)

    # act
    loginpage.enter_username('demosalesmanager')
    loginpage.enter_password('crmsfa')
    loginpage.login()

    # assert
    loginpage.assert_title(title_homepg)
