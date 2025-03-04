import pytest
from utils.webdriver_factory import get_driver
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
