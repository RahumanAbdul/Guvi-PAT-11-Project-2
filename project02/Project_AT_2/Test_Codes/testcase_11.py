
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
        self.driver.implicitly_wait(20)
        yield
        self.driver.close()


    # Test Case ID: TC_PIM_11
    def test_updating_employeejobactivation(self, booting_function):      
        self.driver.get(data.Hrm_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_InputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_InputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PimModule_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EmployeeName_Inputbox).send_keys(data.Hrm_Data().EmployeeName)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Include_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EmployeeStatusPast_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SearchButton_Locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EditButton_Locator).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().JobActiveModule_Locator).click()
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ActivateEmploymentButton_Locator).click()
        assert self.driver.title == 'OrangeHRM'
        print("EMPLOYEE JOB ACTIVATION SUCCESSFULLY UPDATED")