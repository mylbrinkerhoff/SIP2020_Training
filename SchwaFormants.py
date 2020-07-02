########################################################################
#
# SchwaFormants.py
#
# This program will give you the formant values for a given vocal tract length
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 2 (Th)
#
########################################################################

# Speed of sound
speed_sound = 35000

# Vocal tract length 
vocal_length = 17.5

# Formant frequencies
f1 = speed_sound/(4 * vocal_length)
f2 = (3 * speed_sound)/(4 * vocal_length)
f3 = (5 * speed_sound)/(4 * vocal_length)

print("F1 = " + str(f1) + "; F2 = " + str(f2) + "; F3 = " + str(f3))
