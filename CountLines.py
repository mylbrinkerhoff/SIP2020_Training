###############################################################################
#  
# CountLines.py
#
# This program will count the number of lines in a text tht is supplied 
# by the user in STDIN
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 6 (M)
#
###############################################################################                                                                                            

# Modules to read in files from stdin
import fileinput as fi

# Variables
count = 0

# Loop over the STDIN and count the number of lines in the file
for line in fi.input():
    count += 1
    print(f'{count} {line}')

# Print out the line number count
print(f'The number of lines in the text is {count}')
