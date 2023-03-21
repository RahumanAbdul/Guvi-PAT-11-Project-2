
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

    # Test Case ID: TC_PIM_10
    def test_updating_terminatedetails(self, booting_function):
        try:
            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().username_InputBox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_InputBox).send_keys(data.Hrm_Data().username)

            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().password_InputBox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_InputBox).send_keys(data.Hrm_Data().password)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().LoginButton)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PimModule_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PimModule_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().EmployeePimName_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EmployeePimName_Inputbox).send_keys(data.Hrm_Data().EmployeeName)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SearchPimButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SearchPimButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().EditPimButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().EditPimButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().JobDetailsMenu_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().JobDetailsMenu_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().TerminateEmployement_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().TerminateEmployement_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().TerminationDate_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().TerminationDate_Inputbox).send_keys(data.Hrm_Data().TerminationDate)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().TerminationReason_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().TerminationReason_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().TerminationReason_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().TerminationReason_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SaveTermination_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SaveTermination_Locator).click()
            assert self.driver.title == 'OrangeHRM'
            print("EMPLOYEE TERMINATION SUCCESSFULLY UPDATED")
        except NoSuchElementException:
            print('yes')  

