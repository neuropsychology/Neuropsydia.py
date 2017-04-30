# -*- coding: utf-8 -*-
"""
Code example of a minimal go/no-go task.
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia
import random  # Import the random module
import pandas as pd  # To manipulate and save data
import numpy as np  # To do some maths

n.start()  # Start neuropsydia
n.instructions("Goal: Hit SPACE whenever a GREEN circle appears. \nIf RED, don't press anything!")  # Display instructions and break line with \n
n.newpage("grey")  # Fill the screen
n.countdown()  # Display countdown

# Initialize the data storage with a dictionary containing empty lists
data = {"Trial": [],
        "Stimulus": [],
        "ISI":[],
        "RT":[],
        "Response":[]}

n_trials = 10  # Number of trials
for trial in range(n_trials):  # Iterate over the number of trials
    stimulus = random.choice(["green", "green", "green", "red"])  # Select a stimulus type
    ISI = random.randrange(start=250, stop=1250, step=250)  # Select the inter-stimuli interval (ISI)

    n.newpage("grey")  # Fill the screen
    n.write("+")  # Fixation cross
    n.refresh()  # Diplay it on screen
    n.time.wait(ISI)  # Wait

    n.circle(size=2, fill_color=stimulus)  # Display the stimulus (filled with the color selected above)
    n.refresh()  # Diplay it on screen
    response, RT = n.response(time_max=1000)  # Wait until 1 s and collect the response and its time

    # Categorize the response
    if response == "SPACE" and stimulus == "green":
        response_type = "HIT"  # Hit
    if response != "SPACE" and stimulus == "green":
        response_type = "MISS"  # Miss
    if response == "SPACE" and stimulus == "red":
        response_type = "FA"  # False Alarm
    if response != "SPACE" and stimulus == "red":
        response_type = "CR"  # Correct Rejection

    # Store data by appending each item to its list
    data["Trial"].append(trial)
    data["Stimulus"].append(stimulus)
    data["ISI"].append(ISI)
    data["RT"].append(RT)
    data["Response"].append(response_type)

# Data saving
df = pd.DataFrame.from_dict(data)  # Transform the data dictionary into a proper and savable dataframe
df.to_csv("data.csv")  # Save it

# Quick analysis
RTs = df[df['Response']=="HIT"]["RT"]  # Select the Hits' RTs
print("Mean RT: " + str(round(RTs.mean(), 2)))   # Print the mean
print("SD RT: " + str(round(RTs.std(), 2)))  # Print the standard deviation
print("Number of False Alarms: " + str(len(df[df['Response']=="FA"])))  # Print the number of intrusions (false alarms)

n.close()  # Close neuropsydia
