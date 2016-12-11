# -*- coding: utf-8 -*-
"""
Code example of a minimal digit span task.
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia
import neurotools as nt  # To save the data
import pandas as pd  # To manipulate and save the data
import numpy as np  # To do some maths


n.start()  # Initialize neuropsydia

number_of_fails = 0
span = 2

while number_of_fails <= 3:

    sequence = np.random.randint(10, size=span)
    good_answer = ""  # transform sequence of ints into a str
    for digit in sequence:
        good_answer = good_answer + str(digit)  # add the current stimulus to sequence
        n.newpage("grey")
        n.time.wait(250)
        n.newpage("grey")
        n.write(digit, size=2)
        n.refresh()
        n.time.wait(1000)
    n.newpage("white")
    answer = n.ask("Answer :")

    if answer == good_answer:
        span = span + 1
    else:
        number_of_fails = number_of_fails + 1


n.close()  # Close neuropsydia
