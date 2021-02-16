# Import libraries
import os
import datetime

# Gets the path to the notes folder
path = os.environ.get('NOTES_DIR')

time = datetime.datetime.now()

note_name = time.strftime("%Y-%m-%d_%H:%M") + "_Note.md"

new_note = open(note_name, "x")
new_note.write("# Notes for " + time.strftime("%Y-%m-%d at %H:%M")+ "\n")
new_note.close()

os.system(('vim ' + note_name))

# TODO: CREATE A NEW MARKDOWN FILE WITH THE
#       DATE AT THE BEGINNING
