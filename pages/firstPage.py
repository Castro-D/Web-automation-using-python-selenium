class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.alumnos_button_xpath = "//a[contains(@href,'/alumnos')]"

    def click_alumnos(self):
        self.driver.find_element_by_xpath(self.alumnos_button_xpath).click()
