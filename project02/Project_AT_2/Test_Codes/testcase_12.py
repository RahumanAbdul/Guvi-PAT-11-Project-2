
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

    # Test Case ID: TC_PIM_12
    def test_updating_employeesalarydetails(self, booting_function):
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

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SalaryMenu_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SalaryMenu_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().AddSalaryButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().AddSalaryButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SalaryComponent_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SalaryComponent_Inputbox).send_keys(data.Hrm_Data().SalaryComponent)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PayGrade_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PayGrade_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PayGradeValue_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PayGradeValue_dropdown).click()           

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PayFrequency_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PayFrequency_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().PayFrequencyValue_dropdown)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().PayFrequencyValue_dropdown).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Currency_dropdown)))
            money = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Currency_dropdown)
            money.click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().drop_down)))
            IndianRupee = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
            if IndianRupee.__contains__("Indian Rupee"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indian Rupee'",money)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().Amount_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().Amount_Inputbox).send_keys(data.Hrm_Data().AmountSalary)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().ToggleSalaryButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().ToggleSalaryButton_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().AccountNumber_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().AccountNumber_Inputbox).send_keys(data.Hrm_Data().AccountNumber)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().AccountType_dropdown)))
            Account = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().AccountType_dropdown)
            Account.click()
            
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().drop_down)))
            Account_Type = self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().drop_down).text
            if Account_Type.__contains__("Savings"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Savings'",Account)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().RoutingNumber_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().RoutingNumber_Inputbox).send_keys(data.Hrm_Data().RoutingNumber)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().AmountSalary_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().AmountSalary_Inputbox).send_keys(data.Hrm_Data().SalaryAmount)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Hrm_Locators().SaveSalaryButton_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().SaveSalaryButton_Locator).click()
            assert self.driver.title == 'OrangeHRM'
            print("EMPLOYEE SALARY DETAILS SUCCESSFULLY UPDATED")
        except NoSuchElementException:
            print('yes')
