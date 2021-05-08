# Project 2: Web scraping using Beautiful Soup 4 and Requests libraries
import requests
from bs4 import BeautifulSoup
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type = int)
parser.add_argument("--dbname", help="Enter the name of database", type = str)
args = parser.parse_args()

url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence="
page_num_MAX = args.page_num_max
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    job_url = url + str(page_num) + '&startPage=1'
    print("GET Request for " + job_url)
    req = requests.get(job_url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("li", {"class": "clearfix job-bx wht-shd-bx"})

    for job in jobs:
        company_name = job.find("h3", {"class": "joblist-comp-name"}).text.replace(" ", "")
        skills = job.find("span", {'class': "srp-skills"}).text.replace(" ", "")
        more_info = job.header.h2.a["href"]

        connect.insert_into_table(args.dbname, tuple(values)
        #print(f"Company name: {company_name.strip()}")
        #print(f"Required skills: {skills.strip()}")
        #print(f"More Info: {more_info}")
        #print('')

connect.get_job_info(args.dbname)
