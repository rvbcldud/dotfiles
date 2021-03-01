import re
import sys
import os

# TODO perhaps only go through a file once and just use the first line
# outputted. another option: print all occurrences of search term but list
# them all as under one file instead of separate files. if this cannot
# be resolved, then simply change "file" in the final output to something
# more readable

# Get path to my notes directory
path = os.environ.get('NOTES_DIR')

# Define lists to be used later for retrieving data
output_list = []
output_lines = []
output_line_numbers = []

# Search for desired tag or string in the notes directory
for files in os.listdir(path):
    if files.endswith('.md'):
        with open((path + files), "r") as file:
            for (i, line) in enumerate(file, start=1):
                if re.search(sys.argv[1], line):
                    # Retrieve the file name, what line on said file,
                    # and line number
                    output_list.append(files)
                    output_lines.append(line)
                    output_line_numbers.append(i)

# Print out list of results
i = 1
if len(output_list) > 12:
    print('This string is not specific enough!!')
    quit()
elif len(output_list) == 0:
    print('This search term found nothing')
    quit()
for (md, output, line) in zip(output_list, output_lines, output_line_numbers):
    print("----------option: " + str(i) + " @ " + "line " + str(line) + "-------")
    print ("     " + output + md)
    print("----------------------------------")
    i += 1

# Ask for user to input the file/note they were looking for
print(len(output_list))
user = int(input("\nInput the value of the desired file: ")) - 1

# Open chosen file in vim
os.system(('vim +' + str(output_line_numbers[user]) +' '+ path + output_list[user]))
