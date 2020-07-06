########################################################################
#
# SchwaStdin.py
#
# This program will prompt the user to provide a length and then comput the
# formant frequencies for the given vocal tract length.
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 6 (M)
#
########################################################################

# Speed of sound
speed_sound = 35000

# Vocal tract length 
#vocal_length = 17.5
vocal_length = input("What is the length of the vocal tract? ")
vocal_length = float(vocal_length)

# Formant frequencies
f1 = speed_sound/(4 * vocal_length)
f2 = (3 * speed_sound)/(4 * vocal_length)
f3 = (5 * speed_sound)/(4 * vocal_length)

# Print out the values of F1 thru F3
print(f'F1 = {f1} F2 = {f2} F3 = {f3}')
