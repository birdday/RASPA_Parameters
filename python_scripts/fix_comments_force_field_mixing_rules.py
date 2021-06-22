import csv
import sys

file = '/Users/brian_day/Github-Repos/RASPA_Parameters/forcefield/TraPPE-General/force_field_mixing_rules_COMMENTS.def'
file_out = '/Users/brian_day/Github-Repos/RASPA_Parameters/forcefield/TraPPE-General/force_field_mixing_rules.def'


# Load file as text and strip whitespace
file_as_text = []
with open(file, newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         row_new = []
         for entry in row:
             if entry != '':
                 row_new.extend([entry])
         file_as_text.extend([row_new])
csvfile.close()

# Remove empty rows and non-necessary comment rows
file_as_text_new =[]
for i in range(len(file_as_text)):
    row = file_as_text[i]
    # Removes Empty Rows
    if row == []:
        continue
    # Removes unnecessary comments
    elif row[0] == '#' and i > 6 and i < len(file_as_text)-2:
        continue
    # Removes bracketed charges which should be specified in pseudo-atoms file, not forcefield file
    elif len(row) > 2 and i > 6 and i < len(file_as_text)-2:
        if row[1] == 'lennard-jones':
            file_as_text_new.extend([row[0:4]])
        elif row[1] == 'none':
            file_as_text_new.extend([row[0:2]])
    else:
        file_as_text_new.extend([row])


with open(file_out, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(file_as_text_new)
csvfile.close()

# Update
len(file_as_text_new) - 9
