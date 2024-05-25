from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def click_elements_by_text_content(browser, text):
    wait_time = 10  # Wait time in seconds
    try:
        element = WebDriverWait(browser, wait_time).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
        )
        element.click()
    except TimeoutException:
        # If the text is not found, click on the next page
        print(f"Text '{text}' not found. Clicking on the next page.")
        browser.execute_script("document.querySelector('#nextPage > a').click()")
        # Wait for the page to load
        time.sleep(5)  # Adjust the wait time as needed
        # Recursively call the function to check for the text again
        click_elements_by_text_content(browser, text)

def click_back_button_after_delay(browser):
    time.sleep(5)
    print("navigating back")
    browser.back()
    print("navigated back")

# def click_element_by_exact_title(browser, title, timeout=10):
#   """Clicks a single element on the page with the exact title attribute.

#   Args:
#       browser: The WebDriver instance representing the browser.
#       title: The exact title attribute value of the element to click.
#       timeout: The maximum time in seconds to wait for the element to appear
#                 (default: 10 seconds).

#   Raises:
#       TimeoutException: If the element is not found within the specified timeout.
#   """
#   xpath = f"//*[@id='remarks' and @title='{title}']"  # More specific XPath

#   try:
#     wait = WebDriverWait(browser, timeout)
#     element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
#     element.click()
#   except TimeoutError as e:
#     print(f"Error: Element with title '{title}' not found after {timeout} seconds.")
#     raise e  # Re-raise the exception for further handling
def click_all_elements_by_exact_title(browser, title, timeout=10, max_clicks=7):
  """Clicks all elements on the page with the exact title attribute, up to a maximum number.

  Args:
      browser: The WebDriver instance representing the browser.
      title: The exact title attribute value of the elements to click.
      timeout: The maximum time in seconds to wait for elements to appear (default: 10 seconds).
      max_clicks: The maximum number of elements to click (default: 7).

  Raises:
      TimeoutException: If no elements are found within the specified timeout.
      NoSuchElementException: If an element with the provided title cannot be found.
  """
  original_window_handle = browser.current_window_handle  # Store the main window handle (optional)

  # Improved XPath (make sure it's accurate for your target elements)
  xpath = f"//*[@id='remarks' and @title='{title}']"

  try:
    wait = WebDriverWait(browser, timeout)
    download_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    # Click only up to max_clicks elements
    for i, element in enumerate(download_elements):
      if i >= max_clicks:
        browser.switch_to.window(original_window_handle)  # uncomment if needed
        break  # Exit the loop after clicking max_clicks elements
      element.click()
      # Switch back to the main window after each click (optional)
      browser.switch_to.window(original_window_handle)  # uncomment if needed

  except TimeoutException as e:
    print(f"Error: Elements with title '{title}' not found after {timeout} seconds.")
    raise e  # Re-raise the exception for further handling
  except NoSuchElementException as e:
    print(f"Error: Element with title '{title}' not found on the page.")
# Example usage

# def execute_script(browser):
#     try:
#         # Execute the provided functions in the browser's console
#         texts_to_click = ["SHS-44959","SHS-44957","SHS-44955","SHS-44910","SHS-43032","SHS-42809","SHS-42748","SHS-42722","SHS-42690","SHS-42663","SHS-42239","SHS-42193","SHS-39990","SHS-39977","SHS-39964","SHS-38586","SHS-38576","SHS-38569","SHS-38475","SHS-38468","SHS-38421","SHS-38414","SHS-38405","SHS-38346","SHS-38265","SHS-37954","SHS-37933","SHS-37896","SHS-37883","SHS-37748","SHS-37745","SHS-34802","SHS-34682","SHS-34600","SHS-34579","SHS-34555","SHS-34529","SHS-34180","SHS-34108","SHS-34059","SHS-33982","SHS-33966","SHS-33589","SHS-33580","SHS-33568","SHS-33251","SHS-33226","SHS-32445","SHS-32430","SHS-32128"]

#         for text in texts_to_click:
#             print("accessing this element:", text)
#             # browser.execute_script('alert("JS works");')
#             time.sleep(3)
#             click_elements_by_text_content(browser, text)
#             print("done operation in :", text)
            
#             print("scrolling down")
#             time.sleep(7)
#            # Scroll to the bottom of the page
#             # browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#             browser.execute_script("window.scrollBy(0, 10000)")  

#             print("Executing download contents code...")
#             time.sleep(7)
#             # Execute JavaScript to click on elements with specific titles
#             click_all_elements_by_exact_title(browser, "Download Document")

#             print("Finally navigating back...")
#             click_back_button_after_delay(browser)

#     except Exception as e:
#         print(f"An error occurred: {e}")
# def execute_script(browser):
#     try:
#         # Execute the provided functions in the browser's console

        # texts_to_click = ["SHS-37889","SHS-37738"]
#         for text in texts_to_click:
#             print("accessing this element:", text)
#             # Click on the element
#             click_elements_by_text_content(browser, text)
#             print("done operation in:", text)
            
#             # Wait for a moment for the page to update
#             time.sleep(3)
            
#             # Log the value and write it to the file
#             with open("result.txt", "a") as f:
#                 time.sleep(2)
#                 f.write("BDA: " + browser.execute_script('return document.querySelector("[id*=\'attrib_4\'] option:checked").textContent') + "\n")
            
#             # Navigate back
#             click_back_button_after_delay(browser)

#     except Exception as e:
#         print(f"An error occurred: {e}")
def execute_script(browser):
    try:
        # Execute the provided functions in the browser's console
        texts_to_click = ["SHS-32385"]

        # Define the headers for the table
        headers = [
            "BDA",
            "Technician",
            "Bill No",
            "Bill Date",
            "Panel Name",
            "Panel Model",
            "Panel Capacity",
            "Panel No",
            "Battery Name",
            "Battery Model",
            "Battery Capacity",
            "Battery No",
            "Name of User",
            "phone number",
            "citizenship NO",
            "citizenship district",
            "citizenship issue date",
            "citizenshup address",
            "husband/father name",
            "distrcit instl ",
            "localbody instl",
            "ward instl",
            "tole instl",
            "installation date",
            "installation type",
            "status"

        ]

        # Write headers to the file
        with open("result.txt", "a") as f:
            f.write("\t".join(headers) + "\n")

        for text in texts_to_click:
            print("accessing this element:", text)
            # Click on the element
            click_elements_by_text_content(browser, text)
            print("done operation in:", text)
            
            # Wait for a moment for the page to update
            time.sleep(6)
            
            # Log the values
            # Log the values
            values = [
                    browser.execute_script('return document.querySelector("[id*=\'attrib_4\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector("[id*=\'attrib_3\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.getElementById("attrib_59").value') + ",",
                    browser.execute_script('return document.getElementById("attrib_60").value') + ",",
                    browser.execute_script('return document.querySelector("[id*=\'attrib_12\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector("[id*=\'attrib_13\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.getElementById("attrib_15").value') + ",",
                    browser.execute_script('return document.getElementById("attrib_14").value') + ",",
                    browser.execute_script('return document.querySelector("[id*=\'attrib_17\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector("[id*=\'attrib_18\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.getElementById("attrib_21").value') + ",",
                    browser.execute_script('return document.getElementById("attrib_19").value') + ",",
                    browser.execute_script('return document.getElementById("projectNameEng").value') + ",",
                    browser.execute_script('return document.getElementById("txtOwnerPhone").value') + ",",
                    browser.execute_script('return document.querySelector(\'input[data-bind="value: Citizenship"]\').value') + ",",
                    browser.execute_script('return document.querySelector("[data-bind*=\'CitizenshipDistrict\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.getElementById("CIssuedDate").value') + ",",
                    browser.execute_script('return document.getElementById("ctzAddress").value') + ",",
                    browser.execute_script('return document.querySelector(\'input[data-bind="value: HusbandFatherName"]\').value') + ",",
                    browser.execute_script('return document.querySelector("[data-bind*=\'Districts\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector("[data-bind*=\'LocalBodys\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector("[data-bind*=\'Wards\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector("[data-bind*=\'Tole\']").value') + ",",
                    browser.execute_script('return document.getElementById("InstDate").value')+ ",",
                    browser.execute_script('return document.querySelector("[id*=\'ddltype\'] option:checked").textContent') + ",",
                    browser.execute_script('return document.querySelector(\'[data-bind="html: CardStatus"]\').textContent;')
                ]

            # Write values to the file
            with open("result.txt", "a") as f:
                time.sleep(2)
                f.write(","+"\t".join(values) + "\n")
            
            # Navigate back
            click_back_button_after_delay(browser)

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        # Create a Firefox webdriver instance
        options = Options()
        # options.add_argument("--headless")
        # options.headless = False  # Set headless mode
        browser = webdriver.Firefox(options=options)

        # Navigate to the webpage
        browser.get('https://AEPC_URL')

        # Wait for the login page to load
        wait = WebDriverWait(browser, 10)
        user_id_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#UserID')))
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Password')))

        # Fill in the UserID and Password fields
        user_id_field.send_keys('USER_NAME')
        password_field.send_keys('33228800Aa')

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login process to complete
        wait.until(EC.url_changes(browser.current_url))

        # Execute the provided script when triggered
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
        # Close the browser
        if 'browser' in locals():
            browser.quit()

if __name__ == "__main__":
    main()
