########################################################################
#
# SonnetSearch.py
#
# This program with search through Shakespeare's sonnets looking for a
# specific structure and prints out that line that contains that structure 
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 10 (F)
#
########################################################################

# Module for regular expressions
import re 

# from ***.py import <function_name> as <name>

# Open the Sonnent file
sonnet = open("sonnets_shakespeare.txt", "r")

# Loop through it looking for a specific regex and print that line

# Number pattern
# num_pattern = re.compile('\d')

# Word pattern
# word_pattern = re.compile('(to).(thy)') # tothy or toThy

# kind pattern
# kind_pattern = re.compile("kind-") # kind-hearted, kind-...

# love if it is at the start of the string
love_pattern = re.compile("(.*)(L|l)ove(.*)") # (.*)[Ll]ove(.*) 

# Loop that prints each line of the pattern
# for line in sonnet:
    # if num_pattern.search(line):
    # if word_pattern.search(line):
    # if kind_pattern.search(line):
    # if love_pattern.search(line):
        # print(line)

# Loop that will count the number of times a pattern occurrs
count = 0
no_count = 0
for line in sonnet:
    if love_pattern.search(line):
        count += 1
    else:
        no_count +=1

# Print out the count and no_count
print("""This file contains {count} lines that have the pattern.\n
And contains {no_count} lines that don't have the pattern.""".format(count=count, no_count=no_count))

# Close the file 
sonnet.close()