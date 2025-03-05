from pages.login_page import LoginPage
from pages.admin.posts_page import PostsPage

def test_add_posts_success(driver):
    login_page = LoginPage(driver)
    posts_page = PostsPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    posts_page.dashboard_posts()
    posts_page.new_posts()
    
def test_edit_posts_success(driver):
    login_page = LoginPage(driver)
    posts_page = PostsPage(driver)
    login_page.open_login_page()
    login_page.login()
    login_page.dashboard()
    posts_page.dashboard_posts()
    posts_page.edit_posts()
    