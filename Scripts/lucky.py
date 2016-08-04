#! python3
# lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4

print('Googling...')  # display test while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieves top search results links.
linkElems = bs4.BeautifulSoup(res.text).select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com/' + linkElems[i].get('href'))
