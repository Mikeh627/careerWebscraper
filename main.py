#   Webscraper for Networking Project
#   CNT 4104
#   Bailey Lewis, Michael Householder, Joshua Cowin

#   A webscraper to take in information and to upload them to a local database,
#   to then finally be uploaded to a website.

#   Links:
#   LinkedIn Software Engineering Job Listings.
#   Format:: Company: Position: Location
#   https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0

#   Microsoft LinkedIn Job Listings:
#   Format:: Company: Position: Location: Pay
#   https://www.linkedin.com/jobs/microsoft-software-engineer-jobs?position=1&pageNum=0

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys

#-----Selenium-----
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


listOfCompanies = []
listOfLocations = []
listOfJobTitles = []

def makeRows(row):
    words = ""

    for i, letter in enumerate(row):
        if not letter.isdigit():
            words += letter
        else:
            return [words.strip(), *row[i:].split(" ")]
def getLinkedIn():
    # Loading in chrome but it needs to be in incognito or you will need to be signed in or create a automated process
    # to sign in
    driver = webdriver.ChromeOptions()
    driver.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get("https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    assert "Page not found" not in driver.page_source

    # XPath for Job title: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h3
    for row in range(1, 5):
        rows = driver.find_elements(By.XPATH, "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h3")
        for row_data in rows:
            #print(f"\n=====row_data {row_data.text}=====\n")
            listOfJobTitles.append(row_data.text)

    print(listOfJobTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, 5):
        rows = driver.find_elements(By.XPATH, "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            #print(f"\n=====row_data {row_data.text}=====\n")
            listOfCompanies.append(row_data.text)

    print(listOfCompanies)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, 5):
        rows = driver.find_elements(By.XPATH, "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span")
        for row_data in rows:
            #print(f"\n=====row_data {row_data.text}=====\n")
            listOfLocations.append(row_data.text)

    driver.close()
    print(listOfLocations)

if __name__ == '__main__':
    getLinkedIn()
