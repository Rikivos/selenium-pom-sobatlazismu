from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import TIMEOUT  # Menggunakan timeout dari config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def open(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=TIMEOUT):
        """Menunggu elemen sampai muncul di halaman"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Menunggu elemen bisa diklik, lalu klik"""
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Menunggu input field muncul, lalu mengetikkan teks"""
        element = self.wait_for_element(locator)
        element.send_keys(text)
