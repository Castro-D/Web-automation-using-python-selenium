from selenium import webdriver
import unittest
from seleniumProjects.UniAutomation.pages.firstPage import *
from seleniumProjects.UniAutomation.pages.secondPage import *
from seleniumProjects.UniAutomation.pages.guaraniPage import *
from seleniumProjects.UniAutomation.pages.inicio_alumno import *


class UniverTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/Diego Castro/PycharmProjects/HelloWorld/chromedriver.exe')
        self.driver.implicitly_wait(10)

    def test_web(self):
        # create this line just so i dont have to type self.driver every time
        driver = self.driver
        driver.get('http://uns.edu.ar/')

        homePage = HomePage(driver)
        homePage.click_alumnos()

        alumnosPage = AlumnosPage(driver)
        alumnosPage.click_access_button()

        # web created a new tab when clicking on access button, so we need to switch to that tab or else it wont find the elements.
        driver.switch_to.window(driver.window_handles[1])
        guaraPage = Guarani(driver)
        guaraPage.get_user_name("XXX")
        guaraPage.get_password('XXX')
        guaraPage.enter_guarani()

        inicio_page = Inicio(driver)
        inicio_page.click_egresados()
        inicio_page.click_tramite()
        print(inicio_page.get_estado_actual())
        # if assert fails, that means my diploma was legalized
        self.assertEqual(inicio_page.get_estado_actual(), 'Legalización Ministerio')

    def tearDown(self):
        self.driver.quit()
