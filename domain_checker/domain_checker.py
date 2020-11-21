import os
import requests
from requests import get
import csv
from bs4 import BeautifulSoup

domain_list = []

# Read in the domains from the txt file into a list
with open("domains.txt", "r") as domains:
    for row in domains:
        domain_list.append(row.strip('\n'))

# Prepare the requests
url = "https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck="

# Loop through the list and return the web page
for domain in domain_list:
    request_url = url + domain
    response = get(request_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    mydivs = soup.findAll("div", {"class": "container"})
    print(mydivs)
