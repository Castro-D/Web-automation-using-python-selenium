class AlumnosPage:

    def __init__(self, driver):
        self.driver = driver

        self.access_button_id = 'acceso-guarrani'

    def click_access_button(self):
        self.driver.find_element_by_id(self.access_button_id).click()
