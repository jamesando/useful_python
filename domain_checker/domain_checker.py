import whois
import datetime
import csv

now = datetime.datetime.now()
domain_list = []

headers = ['Domain','Registrar','Registrar URL','Status','Reg Name','Reg Type','Reg Street','Reg City','Reg Country','Created','Expiration','Updated']

with open('domain_results.csv', 'w', newline='') as csvfile:

    # Read in the domains from the txt file into a list
    with open("domains.txt", "r") as domains:
        for row in domains:
            domain_list.append(row.strip('\n'))

    # Loop through the list and return the web page
    for domain in domain_list:
        try:
            res = whois.whois(domain)
            print(res)
            exp = res['expiration_date']
            expired = "it expired on " if exp < now else "it expires on "
        except:
            print(domain + " is available")
