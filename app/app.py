
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Set up Selenium WebDriver
options = Options()
options.headless = False  # Set True to run without opening the browser
driver_path = "D:\Program Files (AC)\Google\Google\Chrome\Application\chromedriver.exe"  # Update with your ChromeDriver path

driver = webdriver.Chrome(executable_path=driver_path, options=options)

# URL of the page
url = 'https://studio.edgeimpulse.com/studio/584185/impulse/1/classification?sampleId=1531598925'
driver.get(url)

# Wait for the page to load
sleep(5)  # Adjust this if necessary

try:
    # Locate the <tbody> element
    tbody = driver.find_element(By.XPATH, "//tbody")
    
    # Get all rows (<tr>) within the <tbody>
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    
    # Extract data from each row
    table_data = []
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")  # Get all <td> in the row
        category = columns[0].text.strip()  # First column: Category name
        count = columns[1].text.strip()    # Second column: Count value
        table_data.append((category, count))
    
    # Print the extracted data
    print("=== Classification Result Table ===")
    for category, count in table_data:
        print(f"Category: {category}, Count: {count}")
    print("===================================")
finally:
    driver.quit()
