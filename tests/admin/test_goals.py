from pages.login_page import LoginPage
from pages.admin.goals_page import GoalsPage

def test_add_goals_success(driver):
    login_page = LoginPage(driver)
    goals_page = GoalsPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    goals_page.dashboard_goals()
    goals_page.new_goals()
    
def test_edit_goals_success(driver):
    login_page = LoginPage(driver)
    goals_page = GoalsPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    goals_page.dashboard_goals()
    goals_page.edit_goals()
    