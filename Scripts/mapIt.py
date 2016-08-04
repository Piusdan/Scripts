#! Python3
# mapIt.py - launches a map in the browser using an adress from the
# command line or clipboard.

import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])

# Get address from clipboard
else:
    address = pyperclip.paste()
# make url
url = 'https://www.google.com/maps/place/' + str(address)
webbrowser.open(url)
