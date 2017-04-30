# -*- coding: utf-8 -*-
"""
Code example of a minimal flanker task.
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia
import pandas as pd  # To manipulate and save data
import numpy as np  # To do some maths

n.start()  # Start neuropsydia
n.instructions("Hit RIGHT or LEFT arrow according to the direction of the CENTRAL arrow.")  # Display instructions

# Initialize cache
cache = {}
for possible_angle in [0, 90, 180]:
    cache = n.preload("arrow-left.png", size=2, rotate=possible_angle, cache=cache)  # Preload images

# Initialize the data storage with a dictionary containing empty lists
data = {"Trial": [],
        "Trial_Type": [],
        "Stimulus_Orientation": [],
        "RT":[],
        "Response":[]}


n.newpage("grey")  # Fill the screen
n.countdown()  # Display countdown

n_trials = 10  # Number of trials
for trial in range(n_trials):  # Iterate over the number of

    n.newpage("grey")  # Fill the screen
    n.write("+")  # Fixation cross
    n.refresh()  # Diplay it on screen
    n.time.wait(500)  # Wait

    # Trial characteristics
    stimulus_angle = np.random.choice([0, 180])  # select target orientation
    trial_type = np.random.choice(["Congruent", "Neutral", "Incongruent"])  # select trial type
    if trial_type == "Congruent":
        distractors_angle = stimulus_angle
    if trial_type == "Incongruent":
        if stimulus_angle == 0:
            distractors_angle = 180
        else:
            distractors_angle = 0
    if trial_type == "Neutral":
        distractors_angle = 90


    n.image("arrow-left.png", x=-5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
    n.image("arrow-left.png", x=-2.5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
    n.image("arrow-left.png", x=0, size=2, cache=cache, rotate=stimulus_angle)  # Target
    n.image("arrow-left.png", x=2.5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
    n.image("arrow-left.png", x=5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
    n.refresh()
    response, RT = n.response(time_max=1000)  # Wait until 1 s and collect the response and its time


    # Response check
    if (response == "LEFT" and stimulus_angle == 0) or (response == "RIGHT" and stimulus_angle == 180):
        response = 1
    else:
        response = 0

    # Store data by appending each item to its list
    data["Trial"].append(trial)
    data["Trial_Type"].append(trial_type)
    data["Stimulus_Orientation"].append(stimulus_angle)
    data["RT"].append(RT)
    data["Response"].append(response)

# Data saving
df = pd.DataFrame.from_dict(data)  # Transform the data dictionary into a proper and savable dataframe
df.to_csv("data.csv")  # Save it

# Quick analysis
mean_cong = df[(df["Trial_Type"]=="Congruent") & (df["Response"]==1)]["RT"].mean()
mean_neu = df[(df["Trial_Type"]=="Neutral") & (df["Response"]==1)]["RT"].mean()
mean_incong = df[(df["Trial_Type"]=="Incongruent") & (df["Response"]==1)]["RT"].mean()
print("Mean RT Congruent: " + str(round(mean_cong, 2)))  # Print the mean of congruent
print("Mean RT Neutral: " + str(round(mean_neu, 2)))  # Print the mean of neutral
print("Mean RT Incongruent: " + str(round(mean_incong, 2)))  # Print the mean of incongruent

n.close()  # Close neuropsydia
