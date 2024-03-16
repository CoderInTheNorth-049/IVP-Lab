from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website ='https://in.linkedin.com/'
driver.get(website)
driver.maximize_window()

username = driver.find_element(by='xpath', value='//input[contains(@autocomplete,"username")]')
password = driver.find_element(by='xpath', value='//input[contains(@autocomplete,"current-password")]')

username.send_keys('boomboomciao049@gmail.com')
password.send_keys('moneyheist@049')

button = driver.find_element(by='xpath', value='//button[contains(@data-id,"sign-in-form__submit-btn")]')
button.click()
time.sleep(5)

web = 'https://www.linkedin.com/feed/update/urn:li:activity:7163607837644972033/'
driver.get(web)
time.sleep(5)

for i in range(259):
    try:
        load = driver.find_element(by='xpath', value='//button[contains(@class, "comments-comments-list__load-more")]')
        load.click()
        time.sleep(2)
    except:
        break

raw_emails = driver.find_elements(By.XPATH, value='//a[contains(@href,"@")]')

data = []
for email in raw_emails:
    data.append(email.text)

df = pd.DataFrame({'emails': data})
df.to_csv('linkdein.csv',index=False)




