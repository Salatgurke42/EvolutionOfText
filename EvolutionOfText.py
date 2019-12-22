#-----------------------------------------------------
# Python 'Evolution of Text' Program
# More programs at: usingpython.com/programs
# Slightly modified by D.R. on Jan 27, 2018
# Modified for Python 3 on Dec 22, 2019
#-----------------------------------------------------

import string
import random
import time
#import matplotlib.pyplot as plt


def evolution(target, repetitions):
    generation_data = []

    for i in range(repetitions):
        possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
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
        generation_data.append(generation)
        #print("Target matched! That took " + str(generation) + " generation(s)")
    return generation_data
#######################################################

target = input("Please enter target: ")
repetitions = int(input("How many repetitions? "))

generation_data = evolution(target, repetitions)
print("Generations for the target", target, ":", generation_data)