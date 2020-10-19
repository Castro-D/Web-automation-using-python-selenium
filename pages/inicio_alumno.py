from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Inicio:

    def __init__(self, driver):
        self.driver = driver
        self.tramites_button_xpath = "//a[contains(@href,'https://g3w.uns.edu.ar/guarani3w/consulta_estado_tramite')]"
        self.button_class = "dropdown-toggle"
        self.estado_class = "estado_actual" # this class changes when the actual state of my diploma changes.

    def click_egresados(self):
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_class_name(self.button_class)[7].click()


    def click_tramite(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.tramites_button_xpath))).click()

    def get_estado_actual(self):
        txt = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, self.estado_class))).text
        return txt
