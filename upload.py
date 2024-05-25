            
    

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pyautogui
def click_elements_by_text_content(browser, text):
    time.sleep(1)
    elements = browser.find_elements(By.TAG_NAME, 'td')
    for element in elements:
        if element.text == text:
            element.click()
            break

    # Wait 2 seconds
    time.sleep(4)
    browser.execute_script("window.scrollBy(0, 10000)")  
    time.sleep(1)
    # Click the file upload input (7th one in this case)
    browser.execute_script('document.querySelectorAll(\'label.file-upload input[type="file"]\')[6].click();')
    time.sleep(2)  # Wait for the file upload dialog to open

    # Use PyAutoGUI to handle the file upload dialog
    
    pyautogui.write(r'D:\New folder\Local Government Recommendation Letter -29-pdf.pdf')
    pyautogui.press('enter')

    # Wait for the file to upload, if necessary
    time.sleep(5)

    # Navigate back
    browser.back()

def click_back_button_after_delay(browser):
    time.sleep(5)
    print("navigating back")
    browser.back()
    print("navigated back")

def click_all_elements_by_exact_title(browser, title, timeout=10, max_clicks=7):
    original_window_handle = browser.current_window_handle  # Store the main window handle (optional)

    xpath = f"//*[@id='remarks' and @title='{title}']"

    try:
        wait = WebDriverWait(browser, timeout)
        download_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

        for i, element in enumerate(download_elements):
            if i >= max_clicks:
                browser.switch_to.window(original_window_handle)  # Uncomment if needed
                break
            element.click()
            browser.switch_to.window(original_window_handle)  # Uncomment if needed

    except TimeoutException as e:
        print(f"Error: Elements with title '{title}' not found after {timeout} seconds.")
        raise e
    except NoSuchElementException as e:
        print(f"Error: Element with title '{title}' not found on the page.")
 
def execute_script(browser):
    try:
        texts_to_click = ["SHS-44968"]

        for text in texts_to_click:
            print("accessing this element:", text)
            time.sleep(1)
            
            time.sleep(3)
            click_elements_by_text_content(browser, text)
            print("done operation in :", text)

            print("scrolling down")
            time.sleep(7)
            browser.execute_script("window.scrollBy(0, 10000)")  

            print("Executing download contents code...")
            time.sleep(7)
            # click_all_elements_by_exact_title(browser, "Download Document")

            print("Finally navigating back...")
            click_back_button_after_delay(browser)

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        options = Options()
        browser = webdriver.Firefox(options=options)

        browser.get('https://AEPC_URL')

        wait = WebDriverWait(browser, 10)
        user_id_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#UserID')))
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Password')))

        user_id_field.send_keys('USER_NAME')
        password_field.send_keys('33228800Aa')

        password_field.send_keys(Keys.RETURN)

        wait.until(EC.url_changes(browser.current_url))

        while True:
            command = input("Enter a command: ")
            if command.strip() == "aa":
                execute_script(browser)
            elif command.strip() == "exit":
                break
            else:
                print("Invalid command. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'browser' in locals():
            browser.quit()

if __name__ == "__main__":
    main()
