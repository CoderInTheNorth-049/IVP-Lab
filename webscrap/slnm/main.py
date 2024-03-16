from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = 'https://www.adamchoi.co.uk/overs/detailed'
driver.get(website)

all_matches_button = driver.find_element(by='xpath', value='//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(by='id', value='country'))
dropdown.select_by_visible_text('Spain')
time.sleep(5)

hometeam = []
awayteam = []

matches = driver.find_elements(By.TAG_NAME, value='tr')
for match in matches:
    hometeam.append(match.find_element(by='xpath', value='./td[2]').text)
    awayteam.append(match.find_element(by='xpath', value='./td[4]').text)
driver.quit()
df = pd.DataFrame({'home':hometeam, 'away':awayteam})
df.to_csv('football.csv', index=False)

