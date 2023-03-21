from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_Abdul:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Hrm_Data().url)
        self.wait = WebDriverWait(self.driver, 20)       

    # Test Case ID: TC_PIM_03
    def test_creation_newemployee(self, booting_function):
        try:
            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().username_InputBox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_InputBox).send_keys(data.Hrm_Data().username)

            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().password_InputBox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_InputBox).send_keys(data.Hrm_Data().password)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().LoginButton)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Admin_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PimModule_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PimModule_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().AddButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().AddButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().FirstName_Inputbox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().FirstName_Inputbox).send_keys(data.Hrm_Data().FirstName)

            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().LastName_Inputbox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().LastName_Inputbox).send_keys(data.Hrm_Data().LastName)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Employeeid_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Employeeid_Inputbox).send_keys(data.Hrm_Data().Employeeid)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().ToggleButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ToggleButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().UsernamePim_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().UsernamePim_Inputbox).send_keys(data.Hrm_Data().UsernamePim)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().StatusRadio_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().StatusRadio_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PasswordPim_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PasswordPim_Inputbox).send_keys(data.Hrm_Data().PasswordPim)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Confirmpassword_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Confirmpassword_Inputbox).send_keys(data.Hrm_Data().ConfirmPassword)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SaveButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SaveButton_Locator).click()
            assert self.driver.title == 'OrangeHRM'
            print("SUCCESSFULLY CREATED NEW EMPLOYEE-UNDER PIM")
        except NoSuchElementException:
            print('yes') 