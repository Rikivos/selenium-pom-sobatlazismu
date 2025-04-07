from pages.login_page import LoginPage
from pages.admin.branches_page import BranchesPage
def test_add_beneficiaries_success(driver):
    login_page = LoginPage(driver)
    branches_page = BranchesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    branches_page.dashboard_branches()
    branches_page.open_branches_page()
