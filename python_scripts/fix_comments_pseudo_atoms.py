import csv
import sys

file = '/Users/brian_day/Github-Repos/RASPA_Parameters/forcefield/OPLS-Xylene/pseudo_atoms_COMMENTS.def'
file_out = '/Users/brian_day/Github-Repos/RASPA_Parameters/forcefield/OPLS-Xylene/pseudo_atoms.def'


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
    elif row[0] == '#' and i > 2:
        continue
    else:
        file_as_text_new.extend([row])


with open(file_out, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(file_as_text_new)
csvfile.close()
