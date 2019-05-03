#!/usr/bin/env bash

# Get absolute path of this script
path=$( cd "$( dirname "${BASH_SOURCE[0]}")" ; pwd -P )

journal_file=journal.md
date=$(date "+%A, %e %B, %Y")

# Search journal for today's date. If found, open editor. If not, create new entry.
grep -qs $"$date" $path/$journal_file
if [[ $? -eq 0 ]]; then
  echo "Continuing today's entry..."
else
  echo "Creating daily entry..."
  echo "# "$date$'\n' >> $path/$journal_file
fi

# Create journal file if not already present.
if [[ ! -f $path/$journal_file ]]; then
  echo "Journal doesn't exist. Creating..."
  echo "# "$date$'\n' >> $path/$journal_file
  # git add $journal_file here?
fi

# Open journal in default editor, otherwise open in nvim
if [[ -n "$EDITOR" ]]; then
  echo "Opening $journal_file in $EDITOR..."
else
  echo "Opening $journal_file in nvim..."
  nvim + $journal_file
fi
