#!/usr/bin/env python3

from os         import system, environ
from pathlib    import Path as path
from datetime   import datetime

# Get paths of this script & journal file
rel_path        = path(__file__).parent
abs_path        = path(__file__).resolve()
journal_file    = path(f'{rel_path}/journal.md')

# Search bashrc for alias 'j'. If it doesn't exist, create it.
def set_alias(shell):
    pattern     = "alias j='"
    home_folder = path('~').expanduser()
    bashrc      = path(f'{home_folder}/.bashrc').resolve()
    zshrc       = path(f'{home_folder}/.zshrc').resolve()

    #zsh
    if shell == '/bin/zsh' and zshrc.is_file():
        with open(zshrc, 'r+') as f:
            if pattern not in f.read():
                f.write(pattern + f"{zshrc}'")
                print(f'Alias set in {zshrc}. Source or restart zsh & hit "j" '
                'to start program')
            else:
                print("'j' is already an alias. You'll have to run the program "
                'manually')
    #bash
    elif shell == '/bin/bash' and bashrc.is_file():
        with open(bashrc, 'r+') as f:
            if pattern not in f.read():
                f.write(pattern + f"{bashrc}'")
                print(f'Alias set in {bashrc}. Source or restart bash & hit "j" '
                'to start program')
            else:
                print("'j' is already an alias. You'll have to run the program "
                'manually')
    else:
        print("Can't find $SHELL or shell run commands. Can't set alias")
# end set_alias()

# Open journal in default editor, otherwise open in nvim.
def open_in_pref_editor():
    pref_editor = environ.get('EDITOR')
    if environ.get('EDITOR') == None:
        system(f'nvim + {journal_file}')
    else:
        system(pref_editor + journal_file)

pretty_date   = '%A, %e %B, %Y'
today_date    = (datetime.now().strftime(pretty_date))

# Create journal file if not already created & set alias if not existing.
if journal_file.is_file() == False:
    print('Journal file not found. Creating...')
    with open(journal_file, 'x') as f:
        f.write(f'# {today_date}')
    find_shell = environ.get('SHELL')
    set_alias(find_shell)

# Get today's date & compare it to the last mod date of journal_file
mod_date      = datetime.fromtimestamp(journal_file.stat().st_mtime).strftime(pretty_date)
if today_date == mod_date:
    print("Continuing today's entry...")
    open_in_pref_editor()
else:
    print("Creating today's entry...")
    with open(journal_file, 'a') as f:
        f.write(f'# {today_date}')
    open_in_pref_editor()
