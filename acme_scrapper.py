import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',  
    filename="ACME_AUTOMATION_LOG_FILE.log",
    filemode="w",
)
username = os.getenv("ACME_USERNAME")
password = os.getenv("ACME_PASSWORD")

# Check if username and password are set
if not username or not password:
    logging.error(
        "Environment variables ACME_USERNAME and/or ACME_PASSWORD are not set."
    )
    raise ValueError(
        "Environment variables ACME_USERNAME and/or ACME_PASSWORD are not set."
    )

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://acme-test.uipath.com/login")

# Maximize the browser window
driver.maximize_window()

# Set the delay time
delay = 3

# Wait for the page to load
time.sleep(delay)

# ACME UI elements using XPath
username_xpath = '//*[@id="email"]'
password_xpath = '//*[@id="password"]'
login_button_xpath = "/html/body/div/div[2]/div/div/div/form/button"
workitems_xpath = '//*[@id="dashmenu"]/div[2]/a/button'
next_button_xpath = "/html/body/div/div[2]/div/nav/ul/li[13]/a"
table_xpath = "/html/body/div/div[2]/div/table"

# Find the elements and send keys
driver.find_element(By.XPATH, username_xpath).send_keys(username)
driver.find_element(By.XPATH, password_xpath).send_keys(password)
driver.find_element(By.XPATH, login_button_xpath).click()
time.sleep(delay)
logging.info("Logged in successfully")
driver.find_element(By.XPATH, workitems_xpath).click()
logging.info("Navigated to Work Items page")
# Locate the table using XPath
table_element = driver.find_element(By.XPATH, table_xpath)


# Initialize an empty DataFrame to store the scraped data
all_data = pd.DataFrame()

while True:
    # Locate the table using XPath
    table_element = driver.find_element(By.XPATH, table_xpath)

    # Scrape the table data
    soup = BeautifulSoup(table_element.get_attribute("outerHTML"), "html.parser")
    table = soup.find("table", {"class": "table"})

    # Parse the table data into a DataFrame
    df = pd.read_html(str(table))[0]

    # Append the data to the all_data DataFrame
    all_data = pd.concat([all_data, df], ignore_index=True)

    # Check if the "Next" button is enabled and click it
    try:
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        if not next_button.is_displayed():
            break
        next_button.click()
        time.sleep(delay)  # Wait for the next page to load
    except NoSuchElementException:
        logging.error(
            "No such element: Unable to locate the 'Next' button", exc_info=True
        )
        break
    except Exception as e:
        logging.error(f"An exception occurred: {str(e)}", exc_info=True)
        break

    if "13" in next_button_xpath:
        next_button_xpath = "/html/body/div/div[2]/div/nav/ul/li[14]/a"
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        next_button.click()


# Write the DataFrame to an Excel file
all_data.to_excel("scraped_data.xlsx", index=False)
logging.info("Number of rows scraped:", len(all_data))

# Close the browser after some time
driver.quit()
