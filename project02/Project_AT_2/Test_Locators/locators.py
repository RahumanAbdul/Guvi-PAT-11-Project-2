class Hrm_Locators:
    username_InputBox = 'username'
    password_InputBox = 'password'
    LoginButton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'


    #Locators For ADMIN module
    Admin_Locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    SearchBox_InputBox = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    StatusRadio_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'

    #Locators For ADMIN System Users
    Usermanagement_Locator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    UserButton_Locator = 'Users'
    UserName_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
    userrole_dropdown = '(//*[@class="oxd-select-text-input"])'
    Admin_option = '(//*[@class="oxd-select-text-input"])[1]'
    status_dropdown = '(//*[@class="oxd-select-text-input"])'
    Ess_option = '(//*[@class="oxd-select-text-input"])[1][1]'
    Enabled_option = '(//*[@class="oxd-select-text-input"])[2]'
    Disabled_option = '(//*[@class="oxd-select-text-input"])[2][1]'
    drop_down = "(//*[@role='listbox'])"
     
    #Locators For PIM Module
    PimModule_Locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    AddButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    FirstName_Inputbox = 'firstName'
    LastName_Inputbox = 'lastName'
    Employeeid_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    ToggleButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    UsernamePim_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    PasswordPim_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    Confirmpassword_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    SaveButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    NewEmployee_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[9]/div/button[2]'
    MiddleName_Inputbox = 'middleName'
    OtherId_Inputbox = '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]'
    SSNNumber_Inputbox = '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div[1]/div[1]/div[2]/input[1]'
    SINNumber_Inputbox = '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]'
    MaleRadio_Button = '//label[normalize-space()="Male"]'
    SmokerCheckbox_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span/i'
    Nationality_dropdown = '(//*[@class="oxd-select-text-input"])'
    Nationality_option = '(//*[@class="oxd-select-text-input"])[1]'
    MilitaryService_Inputbox = '//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]'
    BloodType_dropdown = '(//*[@class="oxd-select-text-input"])'
    BloodType_option = '(//*[@class="oxd-select-text-input"])[3][1]'
    Marital_dropdown = '(//*[@class="oxd-select-text-input"])'
    Marital_option = '(//*[@class="oxd-select-text-input"])[2][1]'
    DriverLicense_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    SubmitButton_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'


    # Locators For Employee Contact Details
    ContactDetailsMenu_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    Street1_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    Street2_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    City_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    State_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    PostalCode_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    Country_dropdown = '(//*[@class="oxd-select-text-input"])'
    CountrySelect_option ='(//*[@class="oxd-select-text-input"])[1]'
    HomePhone_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    Mobile_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    WorkPhone_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    WorkEmail_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    OtherEmail_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    ContactSaveButton_Locator = '(//*[@type="submit"])'

    # Locators For Emergency Contact Details
    EmergencyDetailsMenu_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a'
    AddEmerButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    NameEmer_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    Relationship_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    HomeTelephone_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    MobileEmer_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    WorkTelephone_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    SaveEmerButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    # Locators For Dependents Contact Details 
    DependentsDetailsMenu_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    AddDepenButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    NameDepen_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    Relationship_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    RelationshipSelectDepen_Option = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    PleaseSpecify_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    DOBdepen_Inputbox = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    SaveDepenButton_Locator = '(//*[@type="submit"])'

    # Locators For Job Details
    JobDetailsMenu_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    JoinedDate_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/i'
    JoinedDateSelect_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    JobTitle_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    JobTitleSelect_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    JobCategory_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    JobCategorySelect_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    SubUnit_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[2]/i'
    SubUnitSelect_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]'
    LocationJob_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i'
    LocationJobSelect_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    EmploymentStatusJob_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i'
    EmploymentStatusJobSelect_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]'
    ToggleEmploymentContract_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    ContractDate_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/i'
    ContractStartDate_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'
    ContractEnd_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/i'
    ContractEndDate_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'
    SaveContractButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    EmployeePimName_Inputbox = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    SearchPimButton_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    EditPimButton_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]'
    

    # Locators For Employee Termination
    TerminateEmployement_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    TerminationDate_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    TerminationReason_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[2]/i'
    TerminationReason_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]'
    SaveTermination_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'
    PersonalDetails_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'

    # Locators For Employee Activation
    ActivateEmployment_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    EmployeeName_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    Include_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    EmployeeStatusPast_dropdown = '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]'
    SearchButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    EditButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/button[2]'
    JobActiveModule_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    ActivateEmploymentButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    PastEmployeesOption_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'

    # Locators For Salary Details
    SalaryMenu_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    AddSalaryButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    SalaryComponent_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    PayGrade_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    PayGradeValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    PayFrequency_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i'
    PayFrequencyValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
    Currency_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    CurrencyValue_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    Amount_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    ToggleSalaryButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    AccountNumber_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    AccountType_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    AccountTypeValue_dropdown = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    RoutingNumber_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    AmountSalary_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    SaveSalaryButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'

    # Locators For Tax Exemptions
    TaxExemptionsMenu_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a'
    StatusTax_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i'
    StatusTaxValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    Exemptions1_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    StateIncomeTax_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[2]/i'
    StateIncomeTaxValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]'
    StatusIncome_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[2]/i'
    StatusIncomeValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]'
    Exemptions2_Inputbox = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    UnemploymentState_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i'
    UnemploymentStateValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]'
    WorkState_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[2]/i'
    WorkStateValue_dropdown = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]'
    SaveTaxButton_Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'







    
