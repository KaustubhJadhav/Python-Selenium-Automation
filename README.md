# Python-Selenium-Automation

## Overview
This is an automation suite for testing the **SwagLabs** website using **Selenium**, **PyTest**, and **Allure** for reporting. The suite includes tests for the following functionalities:

1. Login and homepage load verification
2. Product filtering (low to high price)
3. Cart operations (add to cart)
4. Checkout process

The tests use **data-driven testing** to validate multiple login credentials and ensure the system behaves as expected.

## Tech Stack Used
- **Programming Language**: Python 3.12
- **Test Automation Framework**: Selenium
- **Test Runner**: PyTest
- **Test Reporting**: Allure
- **Test Data Management**: Excel (`openpyxl` library)
- **Version Control**: Git & GitHub
- **Browser**: Google Chrome with ChromeDriver

## Prerequisites and How to Run

1. **Install Python 3.x** (if not installed already) from [python.org](https://www.python.org/downloads/).
   
2. **Install the necessary packages** globally using pip:
   
   ```bash
   pip install selenium pytest allure-pytest openpyxl
   ```

3. **ChromeDriver:**
    Download and install ChromeDriver that matches your Chrome version.

4. **Running the Tests:**
    To run all tests and generate the Allure report:

    ```bash
    pytest tests/ --alluredir=reports
    allure generate reports -o allure-report --clean
    ```

    To view the Allure report in your browser:
    ```bash
    allure serve reports
    ```
    Or
    ```bash
    allure serve allure-report
    ```
    This will open the report in your default browser with details on each test execution (Pass/Fail, Screenshots, and Logs).

5. **Test Data:**
   
    ***login_data.xlsx*** : file containing multiple sets of login credentials ***(standard_user, locked_out_user, etc.)***

## Screenshots:

1. **Login Test Case**: Locked Out User

   ![image](https://github.com/user-attachments/assets/220b1801-1c7a-4637-88c1-1fd13d4cb25a)

3. **Login Test Case**: Correct User and Password

    ![image](https://github.com/user-attachments/assets/8020bc82-7706-4040-aa00-88ed59729b6c)

5. **Login Test Case**: Invalid User 

    ![image](https://github.com/user-attachments/assets/78b04a8f-044b-46d0-aac5-763ac1576f0d)

7. **Checkout Test Case**: 

    ![image](https://github.com/user-attachments/assets/384b8d2f-b285-4ad5-acce-3104cd2a0220)

8. **Cart Operations Test Case**: 

    ![image](https://github.com/user-attachments/assets/15e051b7-9900-44d3-a16e-90fd8f1278f7)

10. **Product Filtering Test Case**: ***(low-high)***

     ![image](https://github.com/user-attachments/assets/1862c5d0-11c8-43cb-966c-562d4ca26512)


## Project Structure

```
├── pages/            # Page Object Models
├── tests/            # Test cases
├── utils/            # Helper functions or config
├── reports/          # Allure reports output
├── conftest.py       # PyTest fixtures and setup
└── requirements.txt  # Dependencies
```


## Notes

- This suite currently supports testing only on Chromium-based browsers.
- Product filtering validation may vary slightly based on inventory updates on the demo site.
- The site occasionally resets session data, which can affect cart and checkout test consistency.
- Make sure to use stable internet connection to avoid flakiness in Selenium actions.


