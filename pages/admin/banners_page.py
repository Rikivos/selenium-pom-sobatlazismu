import time
from pages.base_page import BasePage
from locators.button_locators import ButtonLocators
from locators.admin.banners_locators import BannersLocators
from locators.general_locators import GeneralLocators
from utils.config import BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BannersPage(BasePage):   
    def dashboard_banners(self):
        self.click(BannersLocators.BANNERS_BUTTON)
        time.sleep(12)
    def new_banners(self):
        self.click(ButtonLocators.NEW_BUTTON)
        time.sleep(12)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.IMAGE_INPUT)).send_keys("D:/test/icon-health.png")
        time.sleep(4)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.TITLE_INPUT)).send_keys("test")
        self.wait.until(EC.presence_of_element_located(GeneralLocators.INFORMATION_INPUT)).send_keys("test")
        self.wait.until(EC.element_to_be_clickable(ButtonLocators.SAVE_BUTTON)).click()
        time.sleep(4)
        
    def edit_banners(self):
        self.click(ButtonLocators.EDIT_BUTTON)
        time.sleep(12)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.IMAGE_INPUT)).send_keys("D:/test/icon-health.png")
        time.sleep(4)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.TITLE_INPUT)).clear().send_keys("hola")
        self.wait.until(EC.presence_of_element_located(GeneralLocators.INFORMATION_INPUT)).clear().send_keys("hola")
        self.wait.until(EC.element_to_be_clickable(ButtonLocators.SAVE_BUTTON)).click()
        time.sleep(4)

