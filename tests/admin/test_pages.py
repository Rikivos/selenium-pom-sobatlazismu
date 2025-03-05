from pages.login_page import LoginPage
from pages.admin.pages_page import PagesPage

def test_add_pages_success(driver):
    login_page = LoginPage(driver)
    pages_page = PagesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    pages_page.dashboard_pages()
    pages_page.new_pages()
    
def test_edit_pages_success(driver):
    login_page = LoginPage(driver)
    pages_page = PagesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    pages_page.dashboard_pages()
    pages_page.edit_pages()
    