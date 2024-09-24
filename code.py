import csv
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

driver = None

try:
    # Set up Firefox driver
    firefox_path = GeckoDriverManager().install()
    options = FirefoxOptions()
    driver = webdriver.Firefox(service=FirefoxService(firefox_path), options=options)
except Exception as e:
    logging.warning("Firefox web driver not found, switching to Chrome. Error: %s", e)
    chrome_path = ChromeDriverManager().install()
    chrome_options = ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(chrome_path), options=chrome_options)

driver.get('https://www.iexindia.com/marketdata/market_snapshot.aspx')

def extract_table_data(table_selector):
    try:
        logging.info("Waiting for table: %s", table_selector)
        WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, table_selector)))
        table = driver.find_element(By.CSS_SELECTOR, table_selector)
        
        if not table:
            logging.error("Table not found.")
            return []
        
        logging.info("Table found, extracting data...")
        rows = table.find_elements(By.TAG_NAME, 'tr')
        table_data = []
        
        for row in rows:
            row_data = []
            cells = row.find_elements(By.TAG_NAME, 'td')
            for cell in cells:
                cell_text = ''.join(div.text.replace(',', '').strip() for div in cell.find_elements(By.TAG_NAME, 'div')) or cell.text.replace(',', '').strip()
                row_data.append(cell_text)
            if row_data:
                table_data.append(row_data)

        if not table_data:
            logging.warning("No data extracted from the first table.")
        
        return table_data

    except Exception as e:
        logging.error("Error extracting first table data: %s", e)
        return []

def extract_second_page_data():
    try:
        logging.info("Waiting for second table...")
        driver.implicitly_wait(1) 
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table[cols="9"]')))
        table = driver.find_element(By.CSS_SELECTOR, 'table[cols="9"]')
        
        if not table:
            logging.error("Second table not found.")
            return []

        logging.info("Second table found, extracting data...")
        table_data = []
        rows = table.find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            row_data = []
            cells = row.find_elements(By.TAG_NAME, 'td')
            for cell in cells:
                cell_text = ''
                divs = cell.find_elements(By.TAG_NAME, 'div')
                if divs:
                    cell_text = ''.join(div.text.replace(',', '').strip() for div in divs)
                else:
                    cell_text = cell.text.replace(',', '').strip()
                row_data.append(cell_text.strip())
            if row_data:
                table_data.append(row_data)

        if not table_data:
            logging.warning("No data extracted from the second table.")
        
        return table_data

    except Exception as e:
        logging.error("Error extracting second table data: %s", e)
        return []

selected_cells_first_page = extract_table_data('table[cols="10"]')

if selected_cells_first_page:
    logging.info("Data extracted moving to the next page...")
    driver.find_element(By.CSS_SELECTOR, 'input[title="Next Page"]').click()
    driver.implicitly_wait(1)  
    # time.sleep(2)
    selected_cells_second_page = extract_second_page_data()
else:
    logging.error("No data extracted")
    driver.quit()
    exit()

driver.quit()

# Combine data from both pages
selected_cells = selected_cells_first_page + selected_cells_second_page

if selected_cells:
    logging.info("Extracted elements from tables:")
    for cell in selected_cells:
        logging.info(cell)
else:
    logging.info("No elements in the tables.")


if selected_cells:
    max_columns = max(len(row) for row in selected_cells)
    with open('scrapped_row_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in selected_cells:
            if len(row) < max_columns:
                row = [''] * (max_columns - len(row)) + row
                logging.info(row)

            writer.writerow(row)
else:
    logging.info("error - no data available")
