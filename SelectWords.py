########################################################################
#
# SelectWords.py
#
# This program will choose entries in CELEX EPW.CD meeting certain criteria:
# 
# * No proper names
# * Nonzero frequency
# * Single words, not phrases 
# * Orthography is a palindrome
#
# Input Format:
# 9\aback\59\7\1\P\@-'b{k\[V][CVC]\[@][b&k]
# 
# Output format:
# <orth> <freq> <pron>
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 9 (Th)
#
########################################################################

# Location in celex
celex_orth = 1
celex_freq = 2
celex_pron = 6

# Read in the CELEX EPW.CD file
f = open('EPW.CD', 'r') 

# Loop through the file and split the line and extract the orth, freq, pron.
for line in f:
    string = line.split("\\")
   # print(string)

    orth = string[celex_orth]
    pron = string[celex_pron]
    freq = string[celex_freq]
    # revs_orth = reversed(orth)

    if (orth == orth.lower()) and (freq != 0):
                print(orth, freq, pron, sep='\t')
# TODO: Fix this program to print out the needed words. Issue with the 

# Close the file
f.close()