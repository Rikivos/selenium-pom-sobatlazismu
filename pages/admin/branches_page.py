import time
from pages.base_page import BasePage
from locators.admin.branches_locators import BranchesLocators
from locators.button_locators import ButtonLocators
from locators.general_locators import GeneralLocators
from utils.config import BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class BranchesPage(BasePage):        
    def dashboard_branches(self):
        self.click(BranchesLocators.BRANCHES_BUTTON)
        time.sleep(12)
        
    def open_branches_page(self):
        self.wait.until(EC.element_to_be_clickable(BranchesLocators.OPEN_BRANCHES_BUTTON)).click()
