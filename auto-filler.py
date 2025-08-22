import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def fill_form():
    # Read the dataset
    # USER: Ensure the 'file.csv' file is in the same directory as this script.
    # The delimiter is currently set to ';'. Change it if your CSV uses a different delimiter (e.g., ',').
    data = pd.read_csv('', delimiter=';')
    total = data.shape[0]

    # Setup the driver once
    # USER: Provide the path to your chromedriver.exe executable.
    # Example: service = Service('C:/path/to/your/chromedriver.exe')
    service = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    for i in range(total):
        print(f"Processing entry {i+1}/{total}")
        # USER: Insert the URL of your Google Form here.
        # Example: driver.get('https://docs.google.com/forms/d/e/1FAIpQLS...')
        driver.get('//')
        time.sleep(1.5)

        # Input name (initials)
        name = data.iloc[i]['nama'] 
        # USER: Insert the correct XPath for the name input field.
        # You can find this by inspecting the form element in your browser.
        inputName = driver.find_element(By.XPATH, '//*')
        inputName.send_keys(name)
        time.sleep(0.3)

        # Input comments
        komentar = data.iloc[i]['komentar']
        # USER: Insert the correct XPath for the comments input field.
        inputKomentar = driver.find_element(By.XPATH, '//*')
        inputKomentar.send_keys(komentar)
        time.sleep(0.3)

        # Submit form
        # USER: Insert the correct XPath for the form submit button.
        submit = driver.find_element(By.XPATH, '//*')
        submit.click()
        time.sleep(1)

        # Click "submit another response" (optional)
        try:
            # USER: Insert the correct XPath for the "Submit another response" button.
            backForm = driver.find_element(By.XPATH, '//')
            backForm.click()
            time.sleep(1)
        except:
            print(f"The form did not show the 'Submit another response' link after entry {i+1}.")

    driver.quit()

fill_form()