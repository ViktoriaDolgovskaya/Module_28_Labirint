import pytest
from selenium import webdriver
import time


@pytest.fixture(autouse=True)
def testing():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.implicitly_wait(5)
    print('\nOpen browser for test...')
    time.sleep(2)

    yield driver

    print('\nQuit browser...')
    driver.quit()