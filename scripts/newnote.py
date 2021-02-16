# Import libraries
import os
import datetime

# Gets the path to the notes folder
path = os.environ.get('NOTES_DIR')

# 
time = datetime.datetime.now()

note_name = os.path.expanduser(path + time.strftime("%Y-%m-%d") + ".md")

if os.path.exists(note_name) == False:
    new_note = open(note_name, "x")
    new_note.write("# Notes for " + time.strftime("%A %B %d") + "\n\n")
    new_note.write("## " + time.strftime("%I:%M%p") + "\n\n")
    new_note.close()
else:
    new_note = open(note_name, "a")
    new_note.write("\n## " + time.strftime("%I:%M%p") + "\n\n")
    new_note.close()
    print('Already created...opening file with new time')

# ADD YEAR and exception for duplicate time

os.system(('alacritty -e vim +$ ' + note_name))
