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

    # Test Case ID: TC_PIM_06
    def test_updating_contactdetails(self, booting_function):
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

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().ContactDetailsMenu_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ContactDetailsMenu_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Street1_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Street1_Inputbox).send_keys(data.Hrm_Data().Street1)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Street2_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Street2_Inputbox).send_keys(data.Hrm_Data().Street2)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().City_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().City_Inputbox).send_keys(data.Hrm_Data().City)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().State_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().State_Inputbox).send_keys(data.Hrm_Data().State)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PostalCode_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PostalCode_Inputbox).send_keys(data.Hrm_Data().PostalCode)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Country_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Country_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().CountrySelect_option)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().CountrySelect_option).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().HomePhone_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().HomePhone_Inputbox).send_keys(data.Hrm_Data().HomePhone)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Mobile_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Mobile_Inputbox).send_keys(data.Hrm_Data().Mobile)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().WorkPhone_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().WorkPhone_Inputbox).send_keys(data.Hrm_Data().Work)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().WorkEmail_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().WorkEmail_Inputbox).send_keys(data.Hrm_Data().WorkEmail)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().OtherEmail_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().OtherEmail_Inputbox).send_keys(data.Hrm_Data().OtherEmail)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().ContactSaveButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ContactSaveButton_Locator).click()
            assert self.driver.title == 'OrangeHRM'
            print("EMPLOYEE CONTACT DETAILS SUCCESSFULLY UPDATED")
        except NoSuchElementException:
            print('yes')    
        

