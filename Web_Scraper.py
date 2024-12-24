import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:/Users/cirey/OneDrive/YearUp/Class 37/MOD 3/CIS 403/chromedriver-win32/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs='title'):
    name = element.find('a')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')