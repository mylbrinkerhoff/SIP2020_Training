########################################################################
#
# SelectVowels.py
#
# Given a specific positive integer divide by 2 if even. If odd multiply by 3 and add 1.
# Repeat until your reach 1
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 13 (M)
#
########################################################################

# Module for regular expressions
import re

# Read in the EPW.CD file 
sonnet = open("EPW.CD", "r")

# Regex for words starting with a vowel
vowel_pattern = re.compile("^(a|e|i|o|u)")

# Looping through the file one line at a time.
for line in sonnet:
    line = line.rstrip("\n")
    string = line.split("\\") # Spliting the string at the \
    orth = string[1] # Store the orthography in orth
    pron = string[6] # Store the pronunciation in pron

    # If loop that will test if the orthography meets the patten and then print out the
    # orthography and pronunciation tab-seperated
    if vowel_pattern.search(orth):    
        print(line)
        # print(orth, pron, sep = '\t')

sonnet.close()