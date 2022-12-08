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

# -----Selenium-----
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#-----SQLite-----
import sqlite3

# When searching, we are going to load into a list, to go to a file and database.
# List for Software Engineer Jobs in the U.S.
softwareEngineerCompanies = []
softwareEngineerLocations = []
softwareEngineerTitles = []

# List for Estero Software Engineer Jobs in the U.S.
EsteroSoftwareEngineerCompanies = []
EsteroSoftwareEngineerLocations = []
EsteroSoftwareEngineerTitles = []

# List for general Microsoft Jobs
generalMicrosoftSearch = []
generalMicrosoftSearchLocations = []
generalMicrosoftSearchTitles = []

# Lists for Microsoft Engineer Jobs
MicrosoftEngineerSearch = []
MicrosoftEngineerLocations = []
MicrosoftEngineerTitles = []


# Searching for Software Engineer Job listings in the U.S
def getLinkedIn(query):
    # Loading in chrome but it needs to be in incognito or you will need to be signed in or create a automated process
    # to sign in
    driver = webdriver.ChromeOptions()
    driver.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    assert "Page not found" not in driver.page_source

    # XPath for Job title: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h3
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h3")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            softwareEngineerTitles.append(row_data.text)

    print(softwareEngineerTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            softwareEngineerCompanies.append(row_data.text)

    print(softwareEngineerCompanies)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span[1]")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            softwareEngineerLocations.append(row_data.text)

    driver.close()
    print(softwareEngineerLocations)

# Searching for Software Engineer Job listings in Estero
def getEsteroLinkedIn(query):
    # Loading in chrome but it needs to be in incognito or you will need to be signed in or create a automated process
    # to sign in
    driver = webdriver.ChromeOptions()
    driver.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Estero%2C%20Florida%2C%20United%20States&geoId=103774310&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    assert "Page not found" not in driver.page_source

    # XPath for Job title: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h3
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h3")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            EsteroSoftwareEngineerTitles.append(row_data.text)

    print(EsteroSoftwareEngineerTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            EsteroSoftwareEngineerCompanies.append(row_data.text)

    print(EsteroSoftwareEngineerCompanies)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span[1]")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            EsteroSoftwareEngineerLocations.append(row_data.text)

    driver.close()
    print(EsteroSoftwareEngineerLocations)


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
            generalMicrosoftSearchTitles.append(row_data.text)

    print(generalMicrosoftSearchTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            generalMicrosoftSearch.append(row_data.text)

    print(generalMicrosoftSearch)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span[1]")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            generalMicrosoftSearchLocations.append(row_data.text)

    driver.close()
    print(generalMicrosoftSearchLocations)


# Searching for Microsoft Software Engineer Jobs
def getLinkedInMircosoftEngineer(query):
    # Loading in chrome but it needs to be in incognito or you will need to be signed in or create a automated process
    # to sign in
    driver = webdriver.ChromeOptions()
    driver.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get(
        "https://www.linkedin.com/jobs/search?keywords=Microsoft%20Software%20Engineer&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    assert "Page not found" not in driver.page_source

    # XPath for Job title: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h3
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h3")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            MicrosoftEngineerTitles.append(row_data.text)

    print(MicrosoftEngineerTitles)

    # XPath for company: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/h4/a
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/h4")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            MicrosoftEngineerSearch.append(row_data.text)

    print(MicrosoftEngineerSearch)

    # Xpath for Location: Increment N starting from 1 to N
    # //*[@id="main-content"]/section[2]/ul/li[N]/div/div[2]/div/span
    for row in range(1, query):
        rows = driver.find_elements(By.XPATH,
                                    "//*[@id='main-content']/section[2]/ul/li[" + str(row) + "]/div/div[2]/div/span[1]")
        for row_data in rows:
            # print(f"\n=====row_data {row_data.text}=====\n")
            MicrosoftEngineerLocations.append(row_data.text)

    driver.close()
    print(MicrosoftEngineerLocations)


if __name__ == '__main__':
    query = int(input("How many results do you want?: "))
    query += 1
    print("------------------U.S. Software Engineering Jobs------------------")
    getLinkedIn(query)
    print("------------------Estero Software Engineering Jobs------------------")
    getEsteroLinkedIn(query)
    print("------------------General Microsoft Jobs------------------")
    getLinkedInMircosoft(query)
    print("------------------General Microsoft Engineering Jobs------------------")
    getLinkedInMircosoftEngineer(query)

    # Looping through the list to write to the file
    # U.S. software engineer search into a file
    f = open("SoftwareEngineerSearch.txt", "w")
    position = 0
    for x in range(len(softwareEngineerCompanies)):
        line = f"Company: {softwareEngineerCompanies[position]}      Location: {softwareEngineerLocations[x]}      Title: {softwareEngineerTitles[x]} \n"
        f.write(line)
        position += 1
    f.close()

    # Estero software engineer search into a file
    f = open("EsteroSoftwareEngineerSearch.txt", "w")
    position = 0
    for x in range(len(softwareEngineerCompanies)):
        line = f"Company: {EsteroSoftwareEngineerCompanies[position]}      Location: {EsteroSoftwareEngineerLocations[x]}      Title: {EsteroSoftwareEngineerTitles[x]} \n"
        f.write(line)
        position += 1
    f.close()

    # General Microsoft search into a file
    f = open("MicrosoftSearch.txt", "w")
    position = 0
    for x in range(len(softwareEngineerCompanies)):
        line = f"Company: {generalMicrosoftSearch[position]}      Location: {generalMicrosoftSearchLocations[x]}      Title: {generalMicrosoftSearchTitles[x]} \n"
        f.write(line)
        position += 1
    f.close()

    # General Microsoft engineering search into a file
    f = open("MicrosoftEngineeringSearch.txt", "w")
    position = 0
    for x in range(len(softwareEngineerCompanies)):
        line = f"Company: {MicrosoftEngineerSearch[position]}      Location: {MicrosoftEngineerLocations[x]}      Title: {MicrosoftEngineerTitles[x]} \n"
        f.write(line)
        position += 1
    f.close()

    # From the file we go to the database, aiming for mass row creation (or tuple)
def insertCareersIntoTable(list)
    try:
    
        sqliteCon = sqlite3.connect('CareerWebscraper')
        cursor = sqliteCon.cursor()
        #print ("Database connection is a go")
        
        #Defining the row 
        sqlite_insert_careers = """INSERT INTO job (Job Title, Location, Company)
        Values (?, ?, ?);"""

        cursor.executemany(sqlite_insert_careers, SoftwareEngineerCompanies)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records Put in")
        sqliteCon.commit()
        
    except sqlite3.Erroras error:
        print("Failed to insert multiple records into sqlitetable", error)
    finally:
            if sqliteCon:
                sqliteCon.close()
                print("SQLite Connection is closed, ready to go again")
                
InsertCareersIntoTable(SoftwareEngineeringCompanies)
 
