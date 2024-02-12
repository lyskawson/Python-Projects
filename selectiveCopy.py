#!/usr/bin/env python3
import os, shutil 

workingDirectory = os.getcwd()
extension = '.txt'
destination = '/Users/aleklyskawa/Desktop'

for folders, subfolders, filenames in os.walk(workingDirectory):

        for filename in filenames:

            if filename.endswith(extension):
                print('All ' + extension + ' files have been copied from ' + os.path.abspath(workingDirectory) + ' to' + destination )
                shutil.copy(os.path.join(folders, filename), destination)


