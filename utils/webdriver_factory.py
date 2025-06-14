from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser tidak didukung: " + browser)
    
    driver.maximize_window()
    return driver
