from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from time import *

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
google_form = "https://forms.gle/WBAHyXn5mqNyPEgQ8"
response = requests.get(zillow_url, headers=headers).text

soup = BeautifulSoup(response, "html.parser")

price = [price.getText() for price in soup.select(".PropertyCardWrapper .PropertyCardWrapper__StyledPriceLine")]
link = [link.get("href") for link in soup.select(".property-card-link")]
address = [addr.getText().replace("/n", "").replace("\n", "").replace(" ", "") for addr in soup.find_all(name="address")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get(google_form)

for i in range(0, len(price)):
    for_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    for_address.send_keys(address[i])

    for_price = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    for_price.send_keys(price[i])

    for_link = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    for_link.send_keys(link[i])

    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_btn.click()
    sleep(0.5)
    back = driver.find_element(By.LINK_TEXT, "अन्य प्रतिक्रिया पेश गर्नुहोस्")
    back.click()
