import requests
import json

# Getting stock data from https://www.alphavantage.co/
# API key for test@test.com account

api_key = '5V5OEOEN5K98E697'

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey={api_key}'

response = requests.get(url)

response_json = response.json()

print(response_json)

