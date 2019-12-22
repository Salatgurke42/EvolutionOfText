#-----------------------------------------------------
# Python 'Evolution of Text' Program
# More programs at: usingpython.com/programs
# Slightly modified by D.R. on Jan 27, 2018
# Modified for Python 3 on Dec 22, 2019
#-----------------------------------------------------

import string
import random
import time


def evolution():
    possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

    #target = str(input("Enter your target text: "))
    target = 'Hallo'
    attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
    attemptNext = ''

    completed = False

    generation = 0

    while completed == False:
        #print(attemptThis)
        attemptNext = ''
        completed = True
        for i in range(len(target)):
            if attemptThis[i] != target[i]:
                completed = False
                attemptNext += random.choice(possibleCharacters)
            else:
                attemptNext += target[i]
        generation += 1
        attemptThis = attemptNext
        time.sleep(0.1)
    print("Target matched! That took " + str(generation) + " generation(s)")

#######################################################

repeat = int(input("How many repetitions? "))

for i in range(repeat):
        evolution()

# Missing: Write no. of generations in file every time the script runs and make an experiment with running 100-10000 times on raspberry pi
