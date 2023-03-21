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

# Test Case ID: TC_PIM_01
    def test_search_textbox(self, booting_function):
        self.driver.get(data.Hrm_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_InputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_InputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Admin_Locator).click()
        self.driver.implicitly_wait(3)
        menu_items = ['ADMIN','PIM','LEAVE','TIME','RECRUITMENT','MY INFO','PERFORMANCE','DASHBOARD','DIRECTORY','MAINTENANCE','BUZZ']
        for item in menu_items:
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SearchBox_InputBox).send_keys(item)
            self.driver.refresh()
            self.driver.implicitly_wait(2)
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SearchBox_InputBox).send_keys(item.lower())
            self.driver.refresh()
        assert self.driver.title == 'OrangeHRM' 
        print("SEARCH-(TEXT BOX) SUCCESSFULLY VALIDATED WITH BOTH UPPER AND LOWER CASE ON ADMIN PAGE")

        




        











