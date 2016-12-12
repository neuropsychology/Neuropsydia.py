# -*- coding: utf-8 -*-
"""
Code example of a minimal digit span task.
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia
import numpy as np  # For generation of random sequence


n.start()  # Initialize neuropsydia
n.instructions("Listen to the experimenter.")  # Display instructions

# Initialize values
number_of_fails = 0  # Initial number of errors
span = 2  # Initial span

while number_of_fails < 3:
    sequence = np.random.randint(10, size=span)  # Generate sequence
    good_answer = ""  # Transform sequence of integers into string

    for digit in sequence:  # For every element in the sequence...
        good_answer = good_answer + str(digit)  # Add the current stimulus to sequence
        n.newpage("grey")
        n.time.wait(250)  # Display an empty screen for 250 ms
        n.newpage("grey")  # Load a grey background
        n.write(digit, size=3)  # Load the stimulus
        n.refresh()  # Render the stimulus on screen
        n.time.wait(1000)  # Wait 1000 ms

    # Get answer
    n.newpage("white")
    answer = n.ask("Answer:")

    # Manage result
    if answer == good_answer:
        span = span + 1  # Increase span
        number_of_fails = 0  # Reset value
    else:
        number_of_fails = number_of_fails + 1

n.newpage()  # Load a white background
n.write("Max span: " + str(span-1))  # Write task result
n.refresh()  # Render it on screen
n.time.wait(3000)  # Wait for 3s

n.close()  # Close neuropsydia
