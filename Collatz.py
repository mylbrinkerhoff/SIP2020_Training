########################################################################
#
# Collatz.py
#
# Given a specific positive integer divide by 2 if even. If odd multiply by 3 and add 1.
# Repeat until your reach 1
#
# M. Brinkerhoff  *  SIP2020, UCSC  *  2020 July 7 (Tu)
#
########################################################################

# A positive integer
n = 100

# repeat until 1
while n > 1:
    print(int(n))

    # if n is even divide 2 otherwise multiply by 3 and add 1

    #Testing if it is even first
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    
    # Testing if it is odd first
    # if n % 2 == 1:
    #     n = n * 3 + 1
    # else: 
    #     n /= 2  

    # if n is equal to 1
    if n == 1:
        print(int(n))
