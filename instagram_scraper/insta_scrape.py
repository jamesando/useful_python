import requests
from bs4 import BeautifulSoup


url = "https://www.instagram.com/"

# Enter the list of accounts you want to monitor here
accounts = ['instagram']

for account in accounts:
    r = requests.get(url + account).text

    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'
    followers= r[r.find(start)+len(start):r.rfind(end)]

    start = '"edge_follow":{"count":'
    end = '},"follows_viewer"'
    following= r[r.find(start)+len(start):r.rfind(end)]

    start = '"edge_owner_to_timeline_media":{"count":'
    end = ',"page_info":{"has_next_page"'
    posts = r[r.find(start)+len(start):r.rfind(end)]
    posts = posts.split(',')[0]

    # Do what you want with the data from each account here..
    print(followers, following, posts)
