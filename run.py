#!/usr/bin/env python3

from os       import system, environ
from os.path  import getmtime, dirname, isfile
from datetime import datetime

# Get absolute path of this script & journal file
dir_path      = dirname(__file__)
journal_file  = dir_path + '/journal.md'

## Create journal file if not already created.
if isfile(journal_file) == False:
    print('Journal file not found. Creating...')
    with open(journal_file, 'x') as f:
        f.write('#')

# Open journal in default editor, otherwise open in vim. Have this func take in
# editor?
def open_in_pref_editor():
    pref_editor = environ.get('EDITOR')
    if environ.get('EDITOR') == None:
        system('nvim + ' + journal_file)
    else:
        system(pref_editor + journal_file)

# Get today's date & compare it to the last mod date of journal_file
pretty_date   = '%A, %e %B, %Y'
today_date    = (datetime.now().strftime(pretty_date))
mod_date      = datetime.fromtimestamp(getmtime(journal_file)).strftime(pretty_date)

if today_date == mod_date:
    print("Continuing today's entry...")
    open_in_pref_editor()
else:
    print("Creating today's entry...")
    with open(journal_file, 'a') as f:
        f.write('#' + today_date)
    open_in_pref_editor()
