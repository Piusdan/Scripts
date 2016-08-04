#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file worse filename increments.
import zipfile
import os


def backupToZip(folder):
    # Backup the entire contects of "folder" into a zip file.

    folder = os.path.abspath(folder)  # make sure the folder is absolute

    # Figure out the filename this code should be based on
    # what file exists.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create teh zip file.
    zippedFolder = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for folderName, subFolders, fileNames in os.walk(folder):
        print('Adding files in %s...' % (folderName))

        # Add the current folder to the ZIP file.
        zippedFolder.write(folderName)

        # add all the files in this folder to the ZIP file.
        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue  # don't backup ZIP files
            zippedFolder.write(os.path.join(folderName, fileName))
    zippedFolder.close()
    print('Done')
if __name__ == '__main__':
    backupToZip('/media/root/D135-DB64/Python/Bins/Tinkering')
