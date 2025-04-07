from pages.login_page import LoginPage
from pages.admin.beneficiaries_page import BeneficiariesPage

def test_add_beneficiaries_success(driver):
    login_page = LoginPage(driver)
    beneficiaries_page = BeneficiariesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    beneficiaries_page.dashboard_beneficiaries()
    beneficiaries_page.new_beneficiaries()
    
def test_edit_beneficiaries_success(driver):
    login_page = LoginPage(driver)
    beneficiaries_page = BeneficiariesPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    beneficiaries_page.dashboard_beneficiaries()
    beneficiaries_page.edit_beneficiaries()
    
