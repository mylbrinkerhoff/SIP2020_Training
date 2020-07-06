########################################################################
#
# Count_to_n.py
#
# This program will count up to a given number
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 2 (Th)
#
########################################################################

# Speed of sound
speed_sound = 35000

# Vocal tract length 
#vocal_length = 17.5
vocal_length = input("What is the length of the vocal tract? ")
vocal_length = int(vocal_length)

# Formant frequencies
f1 = speed_sound/(4 * vocal_length)
f2 = (3 * speed_sound)/(4 * vocal_length)
f3 = (5 * speed_sound)/(4 * vocal_length)

print("F1 = {f1} F2 = {f2} F3 = {f3}".format())

