import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from datetime import datetime
import os
import pandas as pd

current_date = datetime.now()


formatted_date = current_date.strftime("%d_%m_%Y_%I_%M%p").lower()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
nameoffile = "no_name"
logging.info("Opening the URL...")
driver.get('https://www.iexindia.com/marketdata/market_snapshot.aspx')

def wait_for_element(css_selector, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def get_user_selection():

    
    print("executing input extraction function")
  
    
try:
    interval_options = {
        '1': '15-Minute Block',
        '2': 'Hourly',
        '3': 'Daily',
        '4': 'Weekly',
        '5': 'Monthly',
        '6': 'Yearly'
    }
    delivery_period_options = {
        '-1': 'Yesterday',
        '0': 'Today',
        '1': 'Tomorrow',
        '-7': 'Last 8 Days',
        '-30': 'Last 31 Days',
        'SR': '-Select Range-'
    }
    delivery_period_for_hourly = {
        '-1': 'Yesterday',
        '0': 'Today',
        '1': 'Tomorrow',
        '-7': 'Last 8 Days',
        '-30': 'Last 31 Days',
        'SR': '-Select Range-'
    }
    delivery_period_for_fifteen = {
        '-1': 'Yesterday',
        '0': 'Today',
        '1': 'Tomorrow',
        '-7': 'Last 8 Days',
        '-30': 'Last 31 Days',
        'SR': '-Select Range-'
    }
    delivery_period_for_daily = {
        
        '-7': 'Last 8 Days',
        '-30': 'Last 31 Days',
        'SR': '-Select Range-'
    }


    from_which_month = { "1":'Jan', 
    "2":'Feb', 
    "3":'Mar', 
    "4":'Apr', 
    "5":'May', 
    "6":'Jun', 
    "7":'Jul', 
    "8":'Aug', 
    "9":'Sep', 
    "10":'Oct', 
    "11":'Nov', 
    "12":'Dec'}
    to_which_month={ "1":'Jan', 
    "2":'Feb', 
    "3":'Mar', 
    "4":'Apr', 
    "5":'May', 
    "6":'Jun', 
    "7":'Jul', 
    "8":'Aug', 
    "9":'Sep', 
    "10":'Oct', 
    "11":'Nov', 
    "12":'Dec',}
    Delivery_period_year= {"-1":'All', 
    "2024":'2024', 
    "2023":'2023', 
    "2022":'2022', 
    "2021":'2021', 
    "2020":'2020', 
    "2019":'2019', 
    "2018":'2018', 
    "2017":'2017', 
    "2016":'2016', 
    "2015":'2015', 
    "2014":'2014', 
    "2013":'2013', 
    "2012":'2012', 
    "2011":'2011', 
    "2010":'2010', 
    "2009":'2009', 
    "2008":'2008',}
    
    dvperiodyeartype={
         "CAL":'Calendar Year',
        "FIN":'Financial Year'
            }

    from_which_week = {
         "1":'1',
    "2":'2',
    "3":'3',
    "4":'4',
    "5":'5',
    "6":'6',
    "7":'7',
    "8":'8',
    "9":'9',
    "10":'10',
    "11":'11',
    "12":'12',
    "13":'13',
    "14":'14',
    "15":'15',
    "16":'16',
    "17":'17',
    "18":'18',
    "19":'19',
    "20":'20',
    "21":'21',
    "22":'22',
    "23":'23',
    "24":'24',
    "25":'25',
    "26":'26',
    "27":'27',
    "28":'28',
    "29":'29',
    "30":'30',
    "31":'31',
    "32":'32',
    "33":'33',
    "34":'34',
    "35":'35',
    "36":'36',
    "37":'37',
    "38":'38',
        "39":'39',
    "40":'40',
    "41":'41',
    "42":'42',
    "43":'43',
    "44":'44',
    "45":'45',
    "46":'46',
    "47":'47',
    "48":'48',
    "49":'49',
    "50":'50',
    "51":'51',
    "52":'52',
    "53":'53',
    }
    to_which_week = {
            "1":'1',
    "2":'2',
    "3":'3',
    "4":'4',
    "5":'5',
    "6":'6',
    "7":'7',
    "8":'8',
    "9":'9',
    "10":'10',
    "11":'11',
    "12":'12',
    "13":'13',
    "14":'14',
    "15":'15',
    "16":'16',
    "17":'17',
    "18":'18',
    "19":'19',
    "20":'20',
    "21":'21',
    "22":'22',
    "23":'23',
    "24":'24',
    "25":'25',
    "26":'26',
    "27":'27',
    "28":'28',
    "29":'29',
    "30":'30',
    "31":'31',
    "32":'32',
    "33":'33',
    "34":'34',
    "35":'35',
    "36":'36',
    "37":'37',
    "38":'38',
        "39":'39',
    "40":'40',
    "41":'41',
    "42":'42',
    "43":'43',
    "44":'44',
    "45":'45',
    "46":'46',
    "47":'47',
    "48":'48',
    "49":'49',
    "50":'50',
    "51":'51',
    "52":'52',
    "53":'53',
    }


 
    print("Select an interval:")
    for key, value in interval_options.items():
        print(f"{key}: {value}")
        
    interval_choice = input("Enter the number corresponding to your delivery period choice: ")  
    logging.info(f"Selecting interval: {interval_choice}")
    
    interval_dropdown = wait_for_element('#ctl00_InnerContent_ddlInterval')
    interval_dropdown.find_element(By.XPATH, f'//option[@value="{interval_choice}"]').click()
    driver.implicitly_wait(3)
    time.sleep(3)
    
    if interval_choice == '1':
        print("\nSelect a delivery period for 15 minutes:")
        for key, value in delivery_period_for_fifteen.items():
            print(f"{key}: {value}")
        delivery_period_choice = input("Enter the key value for delivery period: ")
        logging.info(f"Selecting delivery period: {delivery_period_choice}")
        
        delivery_period_dropdown = wait_for_element('#ctl00_InnerContent_ddlPeriod')

        delivery_period_dropdown.find_element(By.XPATH, f'//option[@value="{delivery_period_choice}"]').click()
        nameoffile = '15_minutes_record_of_'+ delivery_period_for_fifteen[str(delivery_period_choice)] + '_extracted_in_' + formatted_date
    
    elif interval_choice == '2':
        print("\nSelect a delivery period for Hourly:")
        for key, value in delivery_period_for_hourly.items():
            print(f"{key}: {value}")
        delivery_period_choice = input("Enter the key value for delivery period: ")
        logging.info(f"Selecting delivery period for Hourly: {delivery_period_choice}")
        
        nameoffile = 'Hourly_record_of_'+ delivery_period_for_hourly[str(delivery_period_choice)] + '_extracted_in_' + formatted_date
        delivery_period_dropdown = wait_for_element('#ctl00_InnerContent_ddlPeriod')
        delivery_period_dropdown.find_element(By.XPATH, f'//option[@value="{delivery_period_choice}"]').click()

    elif interval_choice == '3':
        print("\nSelect a delivery period for Daily:")
        for key, value in delivery_period_for_daily.items():
            print(f"{key}: {value}")
        delivery_period_choice = input("Enter the key value for delivery period: ")
        nameoffile = 'Daily_record_of_'+ delivery_period_for_daily[str(delivery_period_choice)] + '_extracted_in_' + formatted_date
        logging.info(f"Selecting delivery period for Daily: {delivery_period_choice}")
        
        delivery_period_dropdown = wait_for_element('#ctl00_InnerContent_ddlPeriod')
        delivery_period_dropdown.find_element(By.XPATH, f'//option[@value="{delivery_period_choice}"]').click()

    elif interval_choice == '4':
        print("\nFrom which week?")
        for key, value in from_which_week.items():
            print(f"{key}: {value}")
        from_week = int(input("Enter the start week: ")) -1 
        
        print("\nTo which week?")
        for key, value in to_which_week.items():
            print(f"{key}: {value}")
        to_week = int(input("Enter the end week: ")) -1 
        
        print("\nFor which year?")
        for key, value in Delivery_period_year.items():
            print(f"{key}: {value}")
        year = input("Enter the year: ")
        
        nameoffile = 'Weekly_record_from_'+from_which_week[str(from_week)]+'_to_'+to_which_week[str(to_week)]+'_of_year_'+Delivery_period_year[str(year)] +'_extracted_in' + formatted_date
        logging.info(f"Selecting delivery period for Weekly: From {from_week} To {to_week}, Year: {year}")
        
        from_dropdown = wait_for_element('#ctl00_InnerContent_ddlFrom')
        Select(from_dropdown).select_by_index(from_week)
        to_dropdown = wait_for_element('#ctl00_InnerContent_ddlTo')
        Select(to_dropdown).select_by_index(to_week)
        
        year_dropdown = wait_for_element('#ctl00_InnerContent_ddlPeriod')
        year_dropdown.find_element(By.XPATH, f'//option[@value="{year}"]').click()

    elif interval_choice == '5':
        print("\nFrom which month?")
        for key, value in from_which_month.items():
            print(f"{key}: {value}")
        from_month = int(input("Enter the start month: ")) -1 
        from_month_dropdown = wait_for_element('#ctl00_InnerContent_ddlFrom')
        Select(from_month_dropdown).select_by_index(from_month)


        time.sleep(3)
        update_report_buttons = wait_for_element('#ctl00_InnerContent_btnUpdateReport', timeout=10)
        update_report_buttons.click()
        
        print("\nTo which month?")
        for key, value in to_which_month.items():
            print(f"{key}: {value}")
        to_month = int(input("Enter the end month: ")) -1 
        to_month_dropdown = wait_for_element('#ctl00_InnerContent_ddlTo')
        Select(to_month_dropdown).select_by_index(to_month)
        time.sleep(5)
        
        print("\nFor which year?")
        for key, value in Delivery_period_year.items():
            print(f"{key}: {value}")
        year = input("Enter the year: ")
        
        logging.info(f"Selecting delivery period for Monthly: From {from_month} To {to_month}, Year: {year}")
        nameoffile = 'Monthly_record_from_'+from_which_month[str(from_month)]+'_to_'+to_which_month[str(to_month)]+'_of_year_'+Delivery_period_year[str(year)] +'_extracted_in' + formatted_date
        
       
        

        
        year_dropdown = wait_for_element('#ctl00_InnerContent_ddlPeriod')
        year_dropdown.find_element(By.XPATH, f'//option[@value="{year}"]').click()
        time.sleep(5)

    else:
        print("\nSelect a delivery period for Yearly:")
        for key, value in Delivery_period_year.items():
            print(f"{key}: {value}")
        year = input("Enter the year: ")
        
        print("\nSelect the delivery period type:")
        for key, value in dvperiodyeartype.items():
            print(f"{key}: {value}")
        period_type = input("Enter the key value for delivery period type: ")
        
        logging.info(f"Selecting delivery period for Yearly: Year: {year}, Type: {period_type}")
        nameoffile = 'Yearly_record_of_'+Delivery_period_year[str(year)]+'_type_'+dvperiodyeartype[str(period_type)] +'_extracted_in' + formatted_date
        
        year_dropdown = wait_for_element('#ctl00_InnerContent_ddlTo')
        year_dropdown.find_element(By.XPATH, f'//option[@value="{year}"]').click()
        
        type_dropdown = wait_for_element('#ctl00_InnerContent_ddlPeriod')
        type_dropdown.find_element(By.XPATH, f'//option[@value="{period_type}"]').click()

    driver.implicitly_wait(2)
    update_report_button = wait_for_element('#ctl00_InnerContent_btnUpdateReport', timeout=10)
    update_report_button.click()

    wait_for_element('table[cols]')
    
except Exception as e:
    logging.error(f"Error during interval/delivery period selection: {e}")
    driver.quit()
    exit()

def extract_data():
    script = """
    let tableData = [];
    let tables = document.querySelectorAll('table[cols]');
    
    // Set to track unique rows
    let uniqueRows = new Set();
    
    // Loop through all tables
    tables.forEach(table => {
        // Extract data from the current table
        table.querySelectorAll('tr').forEach(tr => {
            let rowData = [];
            tr.querySelectorAll('td').forEach(cell => {
                let cellText = '';
                
                // Handle divs inside the cell
                const divs = cell.querySelectorAll('div');
                if (divs.length > 0) {
                    divs.forEach(div => {
                        cellText += div.innerText.replace(/,/g, '').trim() + ' ';
                    });
                } else {
                    // Directly take the inner text of the cell
                    cellText = cell.innerText.replace(/,/g, '').trim();
                }
                
                rowData.push(cellText.trim());
            });

            // Convert rowData to a string to use as a unique identifier
            let rowIdentifier = rowData.join('|');

            // Only push rowData to tableData if it contains more than 2 columns
            // and it is unique
            if (rowData.length > 2 && !uniqueRows.has(rowIdentifier)) {
                uniqueRows.add(rowIdentifier);
                tableData.push(rowData);
            }
        });
    });

    return tableData.length > 0 ? tableData : null;
    """
    return driver.execute_script(script)

def scrape_data(data_array):
    logging.info("Extracting data from the current page...")
    page_data = extract_data()
    driver.implicitly_wait(1)
    data_array.extend(page_data)
    
    try:
        
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[title="Next Page"]')))
        if next_button:
            next_button.click()
            time.sleep(2)  
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table[cols]')))
            driver.implicitly_wait(1)
            return scrape_data(data_array)  
    except Exception as e:
        logging.warning("No more pages or error navigating to the next page.")

    return data_array


selected_cells = scrape_data([])


if selected_cells:
    max_columns = max(len(row) for row in selected_cells)
    with open(f'{nameoffile}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in selected_cells:
            if len(row) < max_columns:
                row = [''] * (max_columns - len(row)) + row
            writer.writerow(row)

    logging.info(f"Selected <td> data has been saved to '{nameoffile}.csv'.")
else:
    logging.info(f"No data was saved to '{nameoffile}.csv' because no <td> elements were found.")

logging.info("Closing the WebDriver...")
driver.quit()


input_file = f'{nameoffile}.csv'  
output_file =  f'{nameoffile}_output.csv'   
   


data = pd.read_csv(input_file, header=None)


def identify_unique_tables(data):
    unique_tables = []
    current_table = []

    for row in data.values:
        
        row_str = [str(cell) if pd.notna(cell) else '' for cell in row]
        
        if 'Date | Hour Block' in row_str:
            if current_table:
                
                if current_table not in unique_tables:
                    unique_tables.append(current_table)
            current_table = [row_str]  
        else:
            current_table.append(row_str)  

    
    if current_table and current_table not in unique_tables:
        unique_tables.append(current_table)

    return unique_tables


unique_tables = identify_unique_tables(data)


cleaned_data = []

for table in unique_tables:
    cleaned_data.extend(table)  


cleaned_df = pd.DataFrame(cleaned_data)


cleaned_df.to_csv(output_file, index=False, header=False)

print(f"Cleaned data saved to {output_file}")



try: os.remove(nameoffile + '.csv');
except FileNotFoundError: pass
