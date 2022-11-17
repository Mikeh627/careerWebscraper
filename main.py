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
#   https://www.linkedin.com/jobs/search?keywords=Microsoft&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0

# Blocking warning because its annoying
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#-----Selenium-----
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# When searching, we are going to load into a list, to go to a file and database.
listOfCompanies = []
listOfLocations = []
listOfJobTitles = []

listOfMicroCompanies = []
listOfMicroLocations = []
listOfMicroJobTitles = []

# Searching for Software Engineer Job listings in the U.S
def getLinkedIn(query):
    # Loading in chrome but it needs to be in incognito or you will need to be signed in or create a automated process
    # to sign in
    driver = webdriver.ChromeOptions()
    driver.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get("https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    assert "Page not found" not in driver.page_source

    # XPath for Job title: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h3
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH, "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h3")
        for row_data in rows:
            #print(f"\n=====row_data {row_data.text}=====\n")
            listOfJobTitles.append(row_data.text)

    print(listOfJobTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH, "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            #print(f"\n=====row_data {row_data.text}=====\n")
            listOfCompanies.append(row_data.text)

    print(listOfCompanies)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH, "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span")
        for row_data in rows:
            #print(f"\n=====row_data {row_data.text}=====\n")
            listOfLocations.append(row_data.text)

    driver.close()
    print(listOfLocations)

# Searching for Microsoft Job listings in the U.S.
def getLinkedInMircosoft(query):
    # Loading in chrome but it needs to be in incognito or you will need to be signed in or create a automated process
    # to sign in
    driver = webdriver.ChromeOptions()
    driver.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=Microsoft&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    assert "Page not found" not in driver.page_source

    # XPath for Job title: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h3
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h3")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            listOfMicroJobTitles.append(row_data.text)

    print(listOfMicroJobTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            listOfMicroCompanies.append(row_data.text)

    print(listOfMicroCompanies)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            listOfMicroLocations.append(row_data.text)

    driver.close()
    print(listOfMicroLocations)

# Main
if __name__ == '__main__':
    query = int(input("How many results do you want?: "))
    query += 1
    getLinkedIn(query)
    print("------------------Loading next function------------------")
    getLinkedInMircosoft(query)

    # Looping through the list to write to the file


    # From the file we go to the database
