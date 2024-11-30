# allows for utilizing webdriver to operate browsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://www.espn.com')
 
# # This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()

ncaa_link = chrome_browser.find_element(
	By.XPATH, "//a[contains(@href, '/college-football/')]//span[contains(text(),'NCAAF')]")

action = ActionChains(chrome_browser)
action.move_to_element(ncaa_link).perform()
time.sleep(1)

# Wait until the "Scores" submenu item is both visible and clickable
scores_item = WebDriverWait(chrome_browser, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, "//a[contains(@href, '/college-football/scoreboard')]//span[contains(text(),'Scores')]"))
)

# Refind the element in case it was updated or changed
scores_item = chrome_browser.find_element(
    By.XPATH, "//a[contains(@href, '/college-football/scoreboard')]//span[contains(text(),'Scores')]"
)

action.move_to_element(scores_item).click().perform()
chrome_browser.execute_script("arguments[0].click();", scores_item)
time.sleep(2)
assert 'College Football Scores - 2024 Season - ESPN' in chrome_browser.title
input("press enter to close browser")


# chrome_browser = webdriver.Chrome()
# chrome_browser.maximize_window()
# chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
 
# # This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()
 
 
 
# user_message = chrome_browser.find_element(By.ID, 'user-message')
# user_message.clear()
# user_message.send_keys('I AM EXTRA COOOOL')
 
# time.sleep(2)
# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# show_message_button.click()
 
# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text


# service = Service(".\\chromedriver.exe")
# chrome_browser = webdriver.Chrome(service=service)
#
# print(chrome_browser)
# chrome_browser.get("https://www.google.com")
# print(f"Current URL: {chrome_browser.current_url}")
# input("press enter to close browser")
# chrome_browser.quit()

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