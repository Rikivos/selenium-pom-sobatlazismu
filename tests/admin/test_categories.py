from pages.login_page import LoginPage
from pages.admin.categories_page import CategoriesPage
def test_add_beneficiaries_success(driver):
    login_page = LoginPage(driver)
    categories_page = CategoriesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    categories_page.dashboard_categories()
    categories_page.new_categories()
    
def test_edit_beneficiaries_success(driver):
    login_page = LoginPage(driver)
    categories_page = CategoriesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    categories_page.dashboard_categories()
    categories_page.edit_categories()
    
    