import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'http://localhost:5000/login'
CORRECT_EMAIL = 'email1@ya.ru'
CORRECT_PASSWORD = 'password'
SUCCESS = 'Welcome, !'

WRONG_EMAIL = 'qwerty@ya.ru'
WRONG_PASSWORD = 'password'


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestLoginPage():
    def test_success_login(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(CORRECT_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(CORRECT_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h1').text
        assert SUCCESS == welcome_text, 'Авторизация не прошла'

    def test_fail_login_by_email(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(WRONG_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(CORRECT_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h1').text
        assert SUCCESS == welcome_text, 'Авторизация не прошла'

    def test_fail_login_by_password(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(WRONG_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(WRONG_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h1').text
        assert SUCCESS == welcome_text, 'Авторизация не прошла'

