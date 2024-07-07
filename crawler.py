import requests
from bs4 import BeautifulSoup

url = 'https://example.com/jobs/'

response  = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', class_='job-listing')

    for job in job_listings:
        title = job.find('h2', class_='job-title').text
        company = job.find('div', class_='company').text
        location = job.find('div', class_='location').text
        print(f"Job Title: {title}, Company:{company}, Location: {location}")
    else: print(f'Failed to retrieve page: {response.status_code}')