import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_summary(url):
    # Configure the webdriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver_path = 'chromedriver.exe'  # Change this to your webdriver path

    with webdriver.Chrome(driver_path, options=chrome_options) as driver:
        driver.get(url)
        content = driver.page_source

        # Extract text content using Beautiful Soup
        soup = BeautifulSoup(content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])

    return content

info = get_summary('https://www.mightymastery.com/education')
print(info)