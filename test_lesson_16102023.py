"""
Маркування тестів
"""

import pytest
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"

# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # цей код виконається після завершення всього тесту
#     print("\nquit browser..")
#     browser.quit()

class TestPage1():
    # викликаємо фікстуру в тесті, передавши її як параметр
    @pytest.mark.smoke
    def test_is_button_search(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    @pytest.mark.regression
    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")
        print("Шукаємо лінк на корзину")

    @pytest.mark.chrome_117
    @pytest.mark.regression
    def test_is_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class = 'top_bar_user']/a[@href = 'user/login']")


# pytest -s -v test_lesson_16102023.py
# pytest -s -v --browser_mode=gui test_lesson_16102023.py
# pytest -s -v -m "regression" test_lesson_16102023.py
# -m mark "smoke" "regression" "chrome_117"
# -m mark "not smoke" "not regression"


