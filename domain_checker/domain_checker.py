import whois
import datetime
import csv

now = datetime.datetime.now()
domain_list = []

headers = ['Domain','Registrar','Registrar URL','Status','Reg Name','Reg Type','Reg Street','Reg City','Reg Country','Created','Expiration','Updated']

with open('domain_results.csv', 'w', newline='') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(headers)
    

    # Read in the domains from the txt file into a list
    with open("domains.txt", "r") as domains:
        for row in domains:
            domain_list.append(row.strip('\n'))

    # Loop through the list and return the web page
    for domain in domain_list:
        try:
            res = whois.whois(domain)
            exp = res['expiration_date']
            expired = "it expired on " if exp < now else "it expires on "
            spamwriter.writerow([domain,res['registrar'],res['registrar_url'],res['status'],
            res['registrant_name'],res['registrant_type'],res['registrant_street'],res['registrant_city'],
            res['registrant_country'],res['creation_date'],res['expiration_date'],res['updated_date']])
        except:
            spamwriter.writerow([domain,'','','Available'])
