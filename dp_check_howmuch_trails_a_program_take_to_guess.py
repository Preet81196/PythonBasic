"""
Description: Check How much trails a program take to guess a number created by itself
Author: Divyesh Patel
Date: Sun 17 May, 2020
"""

# TODO: run this for thousands of time, add results in a file, and find probability for each original_random.
# The Probability should be 1/100, Work on that data-result file to produce the probability

from random import randint as RI

original_random = RI(1, 100)
found = False
trials = 0

print("original_random", original_random)
while not found:
    additional_random = RI(1, 100)
    trials += 1
    print("additional random:", additional_random)
    if original_random == additional_random:
        found = True
        print("Trials", trials)