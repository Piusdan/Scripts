#! python3
# downloadXkcd.py - 'http://xkcd.com'   # starting url
import requests
import os
import bs4

url = 'http://xkcd.com'
try:
    os.makedirs('xkcd')  # store comics in ./xkcd
except:
    pass
while not url.endswith('#'):
    # Download the page.
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the url of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find the comic image...')
    else:
        comicUrl = comicElem[0].get('src')
        # Download the comic image
        print('Downloading the comic image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd
        imageFile = open(os.path.join(
            'xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the prev button's url
    buttonElems = soup.select('a[rel="prev"]')[0]
    url ='http://xkcd.com' + buttonElems.get('href')
print ('Done')
