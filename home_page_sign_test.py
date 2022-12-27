import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://localhost:5000/signup'
CORRECT_EMAIL = 'user050@ya.ru'
CORRECT_PASSWORD = 'user050'

CYRILLIC_EMAIL = 'ваня@ya.ru'
EMPTY_EMAIL = ''
NO_AT_EMAIL = 'user04ya.ru'

EMPTY_PASSWORD = ''
EMAIL_FOR_SPACE_PASSWORD = 'user060@ya.ru'
SPACE_PASSWORD = '   '
SUCCESS = 'Login'


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestSignUpPage():
    def test_fail_sign_cyrillic_email(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(CYRILLIC_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(CORRECT_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h3').text
        assert SUCCESS == welcome_text, 'Регистрация не прошла'

    def test_fail_sign_no_at_email(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(NO_AT_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(CORRECT_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h3').text
        assert SUCCESS == welcome_text, 'Регистрация не прошла'

    def test_fail_sign_empty_email(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(EMPTY_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(CORRECT_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h3').text
        assert SUCCESS == welcome_text, 'Регистрация не прошла'

    def test_fail_sign_empty_password(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(CORRECT_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(EMPTY_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h3').text
        assert SUCCESS == welcome_text, 'Регистрация не прошла'

    def test_fail_sign_space_password(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(CORRECT_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(SPACE_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h3').text
        assert SUCCESS == welcome_text, 'Регистрация не прошла'

    def test_success_sign(self, driver):
        driver.get(URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]')))

        input_email = driver.find_element(By.NAME, 'email')
        input_email.send_keys(CORRECT_EMAIL)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(CORRECT_PASSWORD)

        submit_btn = driver.find_element(By.CLASS_NAME, 'button')
        submit_btn.click()

        welcome_text = driver.find_element(By.TAG_NAME, 'h3').text
        assert SUCCESS == welcome_text, 'Регистрация не прошла'

