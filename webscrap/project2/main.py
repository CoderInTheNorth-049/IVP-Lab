from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

options = Options()
options.headless = False
#options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
website ='https://www.audible.in/search'
driver.get(website)
driver.maximize_window()


container = driver.find_element(By.CLASS_NAME, value="adbl-impression-container")
products = container.find_elements(By.XPATH, value='.//li[contains(@class, "productListItem")]')

title = []
author = []
length = []

for product in products:
    title.append(product.find_element(by='xpath', value='.//h3[contains(@class,"bc-heading")]').text)
    author.append(product.find_element(by='xpath', value='.//li[contains(@class,"authorLabel")]').text)
    length.append(product.find_element(by='xpath', value='.//li[contains(@class,"runtimeLabel")]').text)
driver.quit()

df = pd.DataFrame({'Title': title, 'Author': author, 'Runtime': length})
df.to_csv('audible.csv', index=False)
