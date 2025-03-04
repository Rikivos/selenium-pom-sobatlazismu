from selenium.webdriver.common.by import By

class ButtonLocators:
    SAVE_BUTTON = (By.CSS_SELECTOR, '.mantine-Button-root:nth-of-type(2)')
    EDIT_BUTTON = (By.CSS_SELECTOR, '.m_4e7aa4fd:nth-child(1) > .m_4e7aa4ef .mantine-focus-auto:nth-child(1) .mantine-focus-auto')
    NEW_BUTTON = (By.CSS_SELECTOR, '.m_811560b9:nth-child(2) > .mantine-focus-auto')

