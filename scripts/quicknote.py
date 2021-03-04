# Import libraries
import os
import sys
import datetime

# Gets the path to the notes folder
path = os.environ.get('NOTES_DIR') + 'fleeting/'

# Set a variable that holds the current time data 
time = datetime.datetime.now()

title = sys.argv[1]

note_name = os.path.expanduser(path + time.strftime("%Y-%m-%d") + "-" \
        + title + ".md")

if os.path.exists(note_name) == False:
    new_note = open(note_name, "x")
    new_note.write("# Fleeting note about " + title.replace('-', " ").title() +  " on "+ \
            time.strftime("%A %B %d, %Y") + "\n\n")
    new_note.write("## " + time.strftime("%I:%M%p") + "\n\n")
    new_note.close()
else:
    new_note = open(note_name, "a")
    new_note.write("\n## " + time.strftime("%I:%M%p") + "\n\n")
    new_note.close()
    print('Already created...opening file with new time')

os.system(('vim +$ ' + note_name))
