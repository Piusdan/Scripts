#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil
import os
import re

# create a regex that matches files with the American date format.
datePattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two digits for the day
    ((19|20)\d\d)                   # all text after the date
    (.*?)$                          # all text after the datetime
    ''', re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # skip file without date.
    if mo is None:
        continue

    # get different parts of the name.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European-style filename
    euroFilename = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart
# Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
# rename the files
    print('Renaming "%s" to "%s"...' %
          (os.path.basename(amerFilename), os.path.basename(euroFilename)))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing.
