import time
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.admin.banners_locators import BannersLocators
from locators.button_locators import ButtonLocators
from utils.config import BASE_URL
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{BASE_URL}/account/login"

    def open_login_page(self):
        self.open(self.url)

    def login(self):
        self.enter_text(LoginLocators.NOHP_INPUT, "0859106652296")
        self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)).click()
        time.sleep(4)
    
    def dashboard(self):
        self.wait.until(EC.element_to_be_clickable(LoginLocators.ACCOUNT_BUTTON)).click()
        self.click(LoginLocators.DASHBOARD_BUTTON)
        time.sleep(12)
    
    # def dashboard_banners(self):
    #     self.click(BannersLocators.BANNERS_BUTTON)
    #     time.sleep(12)
    #     self.click(ButtonLocators.NEW_BUTTON)
    #     time.sleep(12)
    



