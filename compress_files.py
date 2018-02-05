#!/usr/bin/python
import os
import zipfile
 
files_zip = zipfile.ZipFile('archive.zip', 'w')
 
for folder, subfolders, files in os.walk('/Users/snangunuri/Python_scripts_Srini'):
 
    for file in files:
        files_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '/Users/snangunuri/Python_scripts_Srini'), compress_type = zipfile.ZIP_DEFLATED)
 
files_zip.close()
