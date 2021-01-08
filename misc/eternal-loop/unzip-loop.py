#!/usr/bin/env python3

import zipfile

zip_file = "Eternal_Loop.zip"
password = "hackthebox"

# Take care of the first zip file since password won't be the filename inside
with zipfile.ZipFile(zip_file) as zr:
    zr.extractall(pwd = bytes(password, 'utf-8'))
    # namelist() returns an array, so take the first index to get the filename
    zip_file = zr.namelist()[0]
#    print(zip_file)

while True:
    with zipfile.ZipFile(zip_file) as zr:
        # gets a list of all the files within the zip archive
        for files in zr.namelist():
            password = files.split(".")[0]
            print(f"Now extracting {zip_file} with the password of: {password}")
        # unzip p/w protected zip with filename of zip inside
        zr.extractall(pwd = bytes(password, 'utf-8'))
        zip_file = files
