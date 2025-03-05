import time
from pages.base_page import BasePage
from locators.admin.posts_locators import PostsLocators
from locators.button_locators import ButtonLocators
from locators.general_locators import GeneralLocators
from utils.config import BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class PostsPage(BasePage):        
    def dashboard_posts(self):
        self.click(PostsLocators.POSTS_BUTTON)
        time.sleep(5)
        
    def new_posts(self):
        self.click(ButtonLocators.NEW_BUTTON)
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.IMAGE_INPUT)).send_keys("D:/test/icon-health.png")
        time.sleep(4)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.TITLE_INPUT)).send_keys("test")
        self.wait.until(EC.element_to_be_clickable(ButtonLocators.SAVE_BUTTON)).click()
        time.sleep(4)
        
    def edit_posts(self):
        self.click(ButtonLocators.EDIT_BUTTON)
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located(GeneralLocators.IMAGE_INPUT)).send_keys("D:/test/icon-health.png")
        time.sleep(4)
        name_input = self.wait.until(EC.visibility_of_element_located(GeneralLocators.TITLE_INPUT))
        name_input.send_keys(Keys.CONTROL + "a") 
        name_input.send_keys(Keys.DELETE)  
        name_input.send_keys("hola") 
        self.wait.until(EC.element_to_be_clickable(ButtonLocators.SAVE_BUTTON)).click()
        time.sleep(4)

