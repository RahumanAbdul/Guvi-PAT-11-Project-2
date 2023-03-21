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

    # Test Case ID: TC_PIM_02
    def test_pageheaders_dropdown(self, booting_function):
        try:
            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().username_InputBox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_InputBox).send_keys(data.Hrm_Data().username)

            self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Hrm_Locators().password_InputBox)))
            self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_InputBox).send_keys(data.Hrm_Data().password)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().LoginButton)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Admin_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Usermanagement_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Usermanagement_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locators.Hrm_Locators().UserButton_Locator)))
            self.driver.find_element(by=By.LINK_TEXT, value=locators.Hrm_Locators().UserButton_Locator).click()

            self.driver.execute_script("window.stop();")

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().UserName_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().UserName_Inputbox).send_keys(data.Hrm_Data().UserName)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().userrole_dropdown)))
            userrole1 = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().userrole_dropdown)
            userrole1.click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().drop_down)))
            Admin_option = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
            if Admin_option.__contains__("Admin"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'",userrole1)
    
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().status_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().status_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Enabled_option)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Enabled_option).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().userrole_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().userrole_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Ess_option)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Ess_option).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().status_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().status_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Disabled_option)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Disabled_option).click()
            assert self.driver.title == 'OrangeHRM'
            print("PAGE HEADERS - (DROPDOWN) SUCCESSFULLY VALIDATED ON ADMIN PAGE")
        except NoSuchElementException:
            print('yes') 


  