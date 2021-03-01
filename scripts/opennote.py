# TODO Create a script that inputs a string
# this string must be present in a file name
# if it is present in one...open that file
# if it is present in more than one... give options
# if it is not present in any...return an error poop

import os
import sys
import re

desired_file = sys.argv[1]

path = os.environ.get('NOTES_DIR')

list_of_files = []

for files in os.listdir(path):
    if files.endswith('.md'):
        file_str = list(files)
        del file_str[0:11]; del file_str[-3:]
        file_str = ''.join(file_str)
        if desired_file in file_str:
            list_of_files.append(files)

if len(list_of_files) == 1:
    os.system('vim '+ path + list_of_files[0])

elif len(list_of_files) == 0:
    print('Sorry :( I couldn\'t find anything)')

elif len(list_of_files) > 1:
    for (i, f) in enumerate(list_of_files, start=1):
        print(i, f)
    choice = int(input('What file would you like to open? '))
    os.system('vim ' + path + list_of_files[choice - 1])
