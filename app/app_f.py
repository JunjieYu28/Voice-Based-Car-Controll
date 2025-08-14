from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver
options = Options()
options.headless = False  # Set True to run without opening the browser
driver_path = "D:/Program Files (AC)/Google/Google/Chrome/Application/chromedriver.exe"  # Update with your ChromeDriver path

driver = webdriver.Chrome(executable_path=driver_path, options=options)

# URL of the page
url = 'https://studio.edgeimpulse.com/studio/584185/impulse/1/classification?sampleId=1531598925'
driver.get(url)

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))

# Function to extract the classification results
def get_classification_result():
    try:
        # Locate the <tbody> element
        tbody = driver.find_element(By.XPATH, "//tbody")
        
        # Get all rows (<tr>) within the <tbody>
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        
        # Extract data from each row and filter out the rows with status '1'
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")  # Get all <td> in the row
            category = columns[0].text.strip()  # First column: Category name
            count = columns[1].text.strip()    # Second column: Count value

            if count == '1':  # Only return the category with count '1'
                return category, count

    except Exception as e:
        print("Error while extracting classification result:", e)
        return None

# Variable to store the last category value
last_category = None

# Sample periodically
try:
    while True:
        result = get_classification_result()
        if result:
            category, count = result
            
            # Check if the new category is the same as the last one
            if category != last_category:
                print(category)
                last_category = category  # Update the last category to the new one

        # Wait for a short interval before the next sample
        time.sleep(2)  # You can adjust this delay to fit your sampling needs

finally:
    driver.quit()
