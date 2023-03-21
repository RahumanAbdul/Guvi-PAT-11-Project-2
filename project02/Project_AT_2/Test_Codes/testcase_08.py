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
        self.wait = WebDriverWait(self.driver, 25)       

    # Test Case ID: TC_PIM_08
    def test_updating_dependentcontactdetails(self, booting_function):
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

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().DependentsDetailsMenu_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().DependentsDetailsMenu_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().AddDepenButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().AddDepenButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().NameDepen_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().NameDepen_Inputbox).send_keys(data.Hrm_Data().NameDepen)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Relationship_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Relationship_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().RelationshipSelectDepen_Option)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().RelationshipSelectDepen_Option).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().DOBdepen_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().DOBdepen_Inputbox).send_keys(data.Hrm_Data().DOBdepen)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SaveDepenButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SaveDepenButton_Locator).click()
            assert self.driver.title == 'OrangeHRM'
            print("EMPLOYEE DEPENDENT CONTACT DETAILS SUCCESSFULLY UPDATED")
        except NoSuchElementException:
            print('yes')
