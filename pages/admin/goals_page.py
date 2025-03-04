import time
from pages.base_page import BasePage
from locators.admin.goals_locators import GoalsLocators
from locators.button_locators import ButtonLocators
from locators.general_locators import GeneralLocators
from utils.config import BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class GoalsPage(BasePage):        
    def dashboard_goals(self):
        self.click(GoalsLocators.GOALS_BUTTON)
        time.sleep(5)
        
    def new_goals(self):
        self.click(ButtonLocators.NEW_BUTTON)
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.IMAGE_INPUT)).send_keys("D:/test/icon-health.png")
        time.sleep(4)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.NAME_INPUT)).send_keys("test")
        self.wait.until(EC.element_to_be_clickable(ButtonLocators.SAVE_BUTTON)).click()
        time.sleep(4)
        
    def edit_goals(self):
        self.click(ButtonLocators.EDIT_BUTTON)
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.IMAGE_INPUT)).send_keys("D:/test/icon-health.png")
        time.sleep(4)
        name_input = self.wait.until(EC.visibility_of_element_located(GeneralLocators.NAME_INPUT))
        name_input.send_keys(Keys.CONTROL + "a") 
        name_input.send_keys(Keys.DELETE)  
        name_input.send_keys("hola") 
        self.wait.until(EC.element_to_be_clickable(ButtonLocators.SAVE_BUTTON)).click()
        time.sleep(4)


