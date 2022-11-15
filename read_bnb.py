from bs4 import BeautifulSoup
from selenium import webdriver
import requests


a = "https://www.airbnb.com/rooms/51817665"

def scrape_page(page_url):
    answer = requests.get(page_url)
    content = answer.content
    soup = BeautifulSoup(content, features='html.parser')

    return soup

def extract_listing(page_url):
    page_soup = scrape_page(page_url)
    name = page_soup.find('div',{'class':'6gi1qsw notranslate'}.get('data-testid'))
    return name

print(extract_listing(a))




#driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#driver.get(url)
#soup = BeautifulSoup(driver.page_source,"html.parser") # <----- here was your issue

#print(soup.select(".data-testid"))

#driver.close()
