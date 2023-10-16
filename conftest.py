import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # цей код виконається після завершення всього тесту
    print("\nquit browser..")
    browser.quit()
