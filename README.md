Test automation assignment:                                                                          
Our team needs to figure out the quality and stability of a user journey flow in a web shop. The customer is either buying a specific object or is just browsing our shop. To get the quality of our delivery some basic flows needs to be scripted using python and selenium and the stakeholders of the result are our business unit and our management team.
(Choose any site that matches the description above, the test case/cases written is not the main focus here, it is rather the complete solution)

Things we would like to see in the code: 
1.	Test cases for the page (try to catch some user journey related flows) 
2.	Design patterns used in test automation
3.	Programming best practices 
4.	Parallel execution of tests
5.	Reporting of the results
6.	Documentation

====================================================SOLUTION===============================================

**Overview**
This project uses behave for Behavior-Driven Development (BDD) testing, Selenium WebDriver for browser automation, and Allure for generating test reports. 
It also includes a GitHub Actions workflow to automate the testing and reporting process.d informative `README.md` that helps users and contributors understand 
and work with your test automation suite. its based on POM design patter for cpaturing page based actions and locators.

**Test Cases:**
  1.User will be able to Login to shop successfully with credentials: login.feature,login.py:steps definition,LoginPage.py:page objects
  2. Clear the existing cart(as its added upon fresh login)
  3. Search a product Galaxy, add to cart and checkout
  4.Upon checkout asset warning message
Note: There has been multiple scenarios defined and step implementation are defined without any steps.

**Project Structure**:
my_project/
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── tests/
│   ├── features/
│       └── step_definitions/ 
│           └── steps.py
│       ├── environment.  py
│       └── features.feature
│    └── pages/
├── configuration/
│   └── behave.ini
├── requirements.txt
└── allure-results/

**Setup and Installation**:
1.1. Install Dependencies: pip install -r requirements.txt
1.2  Allure Reports: Navigate to tests directory
      sudo apt install nodejs npm
      npm install -g allure-commandline --save-dev
      For running report:
      behave -f allure_behave.formatter:AllureFormatter -o allure-results
      allure serve allure-results
**Workflow Breakdown**:
**Checkout Code:** Retrieves the code from the repository.
**Set up Python:** Configures Python for the environment.
**Install Dependencies:** Installs Python packages and Allure CLI.
**Run Behave Tests:** Executes BDD tests and generates Allure results.
**Generate Allure Report:** Converts results into a report.
**Upload Allure Report:** Uploads the report as an artifact.





