# allows for utilizing webdriver to operate browsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
chrome_browser = webdriver.Chrome()

# Maximize the browser window for better visibility
chrome_browser.maximize_window()

# Navigate to ESPN's website
chrome_browser.get('https://www.espn.com')

# Commented out: This part would handle the popup if it appears on the page
# It waits for 2 seconds before looking for the close button of the lightbox popup
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()

# Locate the "NCAAF" link using XPath, which will be part of the navigation to the college football section
ncaa_link = chrome_browser.find_element(
	By.XPATH, "//a[contains(@href, '/college-football/')]//span[contains(text(),'NCAAF')]")

# Create an action chain to perform mouse movements and clicks in the browser
action = ActionChains(chrome_browser)

# Move the mouse pointer over the "NCAAF" link to show the dropdown menu (hover action)
action.move_to_element(ncaa_link).perform()

# Sleep for 1 second to give the page time to update after the hover
time.sleep(1)

# Wait until the "Scores" submenu item is visible and clickable before proceeding
scores_item = WebDriverWait(chrome_browser, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, "//a[contains(@href, '/college-football/scoreboard')]//span[contains(text(),'Scores')]"))
)

# Re-find the "Scores" menu item after waiting to ensure it's ready for interaction
scores_item = chrome_browser.find_element(
    By.XPATH, "//a[contains(@href, '/college-football/scoreboard')]//span[contains(text(),'Scores')]"
)

# Move the mouse pointer to the "Scores" menu item and click it to navigate
action.move_to_element(scores_item).click().perform()

# Alternatively, use JavaScript to click the "Scores" element (could be useful if the action chain fails)
chrome_browser.execute_script("arguments[0].click();", scores_item)

# Sleep for 2 seconds to give the browser time to load the new page
time.sleep(2)

# Assert that the page title now matches the expected title for the College Football Scores page
assert 'College Football Scores - 2024 Season - ESPN' in chrome_browser.title

# Wait for user input before closing the browser (this gives the user a chance to check the result)
input("press enter to close browser")






# Example of working with the ChromeDriver service:
# service = Service(".\\chromedriver.exe")
# chrome_browser = webdriver.Chrome(service=service)
#
# print(chrome_browser)
# chrome_browser.get("https://www.google.com")
# print(f"Current URL: {chrome_browser.current_url}")
# input("press enter to close browser")
# chrome_browser.quit()

# Example of interacting with the Python.org website using Selenium
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# input("press enter to close browser")
# driver.close()
