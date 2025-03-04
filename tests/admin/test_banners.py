from pages.login_page import LoginPage
from pages.admin.banners_page import BannersPage

def test_add_banners_success(driver):
    login_page = LoginPage(driver)
    banners_page = BannersPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    banners_page.dashboard_banners()
    banners_page.new_banners()
    
def test_edit_banners_success(driver):
    login_page = LoginPage(driver)
    banners_page = BannersPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    banners_page.dashboard_banners()
    banners_page.edit_banners()

    