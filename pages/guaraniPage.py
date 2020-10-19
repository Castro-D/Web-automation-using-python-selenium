from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Guarani:

    def __init__(self, driver):
        self.driver = driver

        self.user_box_id = 'usuario'
        self.pw_box_id = 'password'
        self.login_button_name = 'login'

    def get_user_name(self, user):
        self.driver.find_element_by_id(self.user_box_id).clear()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, self.user_box_id))).send_keys(user)

    def get_password(self, password):
        self.driver.find_element_by_id(self.pw_box_id).clear()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, self.pw_box_id))).send_keys(password)

    def enter_guarani(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.NAME, self.login_button_name)))
        element.click()
