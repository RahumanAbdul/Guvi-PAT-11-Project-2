from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_Abdul:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(25)
        yield
        self.driver.close()

    # Test Case ID: TC_PIM_05
    def test_updating_personaldetails(self, booting_function):              
        self.driver.get(data.Hrm_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_InputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_InputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PimModule_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EmployeePimName_Inputbox).send_keys(data.Hrm_Data().EmployeeName)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SearchPimButton_Locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EditPimButton_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().MiddleName_Inputbox).send_keys(data.Hrm_Data().MiddleName)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().OtherId_Inputbox).send_keys(data.Hrm_Data().OtherId)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SSNNumber_Inputbox).send_keys(data.Hrm_Data().SSNNumber)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SINNumber_Inputbox).send_keys(data.Hrm_Data().SINNumber)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().MaleRadio_Button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SmokerCheckbox_Locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Nationality_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Nationality_option).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().MilitaryService_Inputbox).send_keys(data.Hrm_Data().MilitaryService)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Marital_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Marital_option).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().DriverLicense_Inputbox).send_keys(data.Hrm_Data().DriverLicenseNumber)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().BloodType_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().BloodType_option).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SubmitButton_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PimModule_Locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EmployeePimName_Inputbox).send_keys(data.Hrm_Data().EmployeeName)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SearchPimButton_Locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EditPimButton_Locator).click()
        assert self.driver.title == 'OrangeHRM'
        print("EMPLOYEE PERSONAL DETAILS SUCCESSFULLY UPDATED")    