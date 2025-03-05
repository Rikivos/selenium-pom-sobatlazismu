from selenium.webdriver.common.by import By

class LoginLocators:
    NOHP_INPUT = (By.CSS_SELECTOR, ".mantine-TextInput-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".m_811560b9.mantine-Button-label")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".mantine-focus-auto:nth-child(5) .mantine-focus-auto")
    DASHBOARD_BUTTON = (By.CSS_SELECTOR, ".tabler-icon:nth-child(3)")
    