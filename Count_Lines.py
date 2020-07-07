########################################################################
#
# Count_Lines.py
#
# This program will loop thru a file and count the number of lines in 
# that file, which is supplied from STDIN
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 7 (Tu)
#
########################################################################

# Package to read in files from STDIN
import fileinput as fi 

# Variables
count = 0

# Loop over the STDIN and count the number of lines in the file
for line in fi.input():
    count += 1
    # count = count + 1
    print(f'{count} {line}') 

# Print outh the count of the lines
print(f'The number of lines in the text is {count})