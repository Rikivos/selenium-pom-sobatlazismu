from selenium.webdriver.common.by import By
class GeneralLocators:
    IMAGE_INPUT = (By.CSS_SELECTOR, 'input[name="image_url"]')
    ICON_INPUT = (By.CSS_SELECTOR, 'input[name="icon_url"]')
    TITLE_INPUT = (By.CSS_SELECTOR, '.m_8fb7ebe7.mantine-Input-input.mantine-TextInput-input[placeholder="Judul"]')
    NAME_INPUT = (By.CSS_SELECTOR, '.m_8fb7ebe7.mantine-Input-input.mantine-TextInput-input[placeholder="Nama"]')
    INFORMATION_INPUT = (By.CSS_SELECTOR, '.m_8fb7ebe7.mantine-Input-input.mantine-TextInput-input[placeholder="Keterangan"]')