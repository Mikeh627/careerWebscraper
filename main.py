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

linksFromSearch = {}
# sys allows us to grab arguments.
# to install Beautiful Soup: File-->Settings-->Project Interpreter and "add package"

# ----------REALLY BIG NOTE: When using terminal don't use Python3 just use py when doing commands----------
# response.content = content returned from the browser
# response.text = How requests changes it over to a string

if __name__ == '__main__':
    for url in sys.argv[1:]:
        # This will add https:// to the beginning of our links when we begin our search with 'www.'
        if not url.lower().startswith('http'):
            url = f'https://{url}'
        try:
            response = requests.get(url)
            response.raise_for_status()

        # Using HTTP error allows us to get the status code and its description:
        #   As in 404: Not found
        except HTTPError as httperr:
            print(f'HTTP error: {httperr}')
            sys.exit(1)
        except Exception as err:
            print(f'Something went really wrong!: {err}')
            sys.exit(1)

        # Open our page with beautiful soup to parse it and find information
        soup = BeautifulSoup(response.text, 'html.parser')

        # For Companies
        for link in soup.findAll("a", class_='hidden-nested-link'):
            print("wow!")
        # For Location
        for link in soup.findAll("span", class_='job-search-card__location'):
            text = link.string
            text.replace('\n', '')
            text.replace(' ', '')
            text.strip()
            with open("results.txt", "a") as namesfile:
                namesfile.write(text)
            print(text)

            # Command:  py main.py 'https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
