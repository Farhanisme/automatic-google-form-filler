# Automatic Google Form Filler

This Python script is designed to automatically fill out a Google Form by reading data from a CSV file. It leverages the Selenium library to automate browser interactions.

## Features

  - **Automated Data Entry**: Reads data from a `.csv` file and inputs it into specified fields on a Google Form.
  - **Customizable**: Easily adaptable to any Google Form by changing the form URL and XPath locators.
  - **Scalable**: Capable of processing a large number of entries from a single dataset.

## Prerequisites

Before running this script, ensure you have the following installed:

1.  **Python**: Make sure you have Python 3.x installed.
2.  **pip**: Python's package installer.

## How to Set Up

### Step 1: Install Necessary Libraries

Open your terminal or command prompt and run the following command to install Selenium and Pandas:

```bash
pip install selenium pandas
```

### Step 2: Download ChromeDriver

This script requires a WebDriver to control the browser. We'll use ChromeDriver for Google Chrome.

1.  Check your Chrome browser version by going to `chrome://version` in the address bar.
2.  Go to the [official ChromeDriver website](https://chromedriver.chromium.org/downloads) and download the version that matches your Chrome version.
3.  Place the `chromedriver.exe` file in the same directory as your Python script.

### Step 3: Prepare the Data File

The script reads data from a CSV file.

1.  Create a CSV file named `dataset_review.csv` in the same directory as the script.
2.  Ensure your CSV file has a header row with columns named **`nama`** and **`komentar`**. The script is configured to read these specific column names.
    **Note**: The current script uses a semicolon (`;`) as a delimiter. If your file uses a comma (`,`), you need to change the `delimiter=';'` part of the code to `delimiter=','`.

<!-- end list -->

```csv
nama;komentar
Budi;Bagus sekali!
Rina;Sangat membantu.
```

## How to Use

Follow these steps to customize and run the script for your specific Google Form.

### 1\. Update the Chrome Driver Path

In the code, update the `Service` path to point to your `chromedriver.exe` file.

```python
# USER: Provide the path to your chromedriver.exe executable.
service = Service('chromedriver.exe')
```

### 2\. Update the Google Form URL

Insert the URL of your Google Form in the `driver.get()` line.

```python
# USER: Insert the URL of your Google Form here.
driver.get('https://docs.google.com/forms/d/e/1FAIpQLS.../viewform')
```

### 3\. Find and Copy the XPath

The script uses XPath to find and interact with form elements. You need to find the correct XPath for each input field and the submit button.

1.  Open your Google Form in the Chrome browser.
2.  Right-click on an input field (e.g., the name field) and select **"Inspect"**.
3.  In the Elements panel, right-click on the highlighted HTML element, go to **`Copy`**, and select **`Copy XPath`**.
4.  Paste the copied XPath into the corresponding line in the Python script.

Here are the lines you need to update:

```python
# USER: Insert the correct XPath for the name input field.
inputName = driver.find_element(By.XPATH, 'PASTE_YOUR_XPATH_HERE')

# USER: Insert the correct XPath for the comments input field.
inputKomentar = driver.find_element(By.XPATH, 'PASTE_YOUR_XPATH_HERE')

# USER: Insert the correct XPath for the form submit button.
submit = driver.find_element(By.XPATH, 'PASTE_YOUR_XPATH_HERE')

# USER: Insert the correct XPath for the "Submit another response" button (optional).
backForm = driver.find_element(By.XPATH, 'PASTE_YOUR_XPATH_HERE')
```

### 4\. Run the Script

Once all paths and XPaths have been updated, save the file and run it from your terminal:

```bash
python auto-filler.py
```

The script will open a Chrome browser window and begin filling out the form automatically.
