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


job_request = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=software+engineering&txtLocation=united+states').text

soup = BeautifulSoup(job_request, 'lxml')
jobsList = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')


print(jobsList)

