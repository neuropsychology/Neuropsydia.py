# -*- coding: utf-8 -*-
"""
Code example of a minimal Stroop task.
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia
import numpy as np  # Load numpy
import pandas as pd  # Load pandas

n.start()  # Start neuropsydia

# Initialize data storage
data = {"Stimulus": [],
        "Stimulus_Color": [],
        "Answer": [],
        "RT": [],
        "Condition": [],
        "Correct": []}

#==============================================================================
# Part 1: Denomination
#==============================================================================

n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

n_trials = 10
for trial in range(n_trials):
    n.newpage("grey")  # Neutral grey background
    n.write("+")  # Fixation cross
    n.refresh()  # Display it
    n.time.wait(250)  # Wait 250 ms

    stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
    stim = "XXXX"
    n.newpage("grey")  # Neutral grey background
    n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
    n.refresh()  # Display it
    answer, RT = n.response()  # Record response and response time

    # Append trial info to
    data["Stimulus"].append(stim)
    data["Stimulus_Color"].append(stim_color)
    data["Answer"].append(answer)
    data["RT"].append(RT)
    data["Condition"].append("Neutral")

    # Categorize the response
    if answer == "LEFT" and stim_color == "raw_red":
        data["Correct"].append(1)
    elif answer == "DOWN" and stim_color == "raw_green":
        data["Correct"].append(1)
    elif answer == "RIGHT" and stim_color == "raw_blue":
        data["Correct"].append(1)
    else:
        data["Correct"].append(0)

#==============================================================================
# Part 2: Conflict
#==============================================================================

n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

n_trials = 10
for trial in range(n_trials):
    n.newpage("grey")  # Neutral grey background
    n.write("+")  # Fixation cross
    n.refresh()  # Display it
    n.time.wait(250)  # Wait 250 ms

    stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
    stim = np.random.choice(["RED", "GREEN", "BLUE"])
    n.newpage("grey")  # Neutral grey background
    n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
    n.refresh()  # Display it
    answer, RT = n.response()  # Record response and response time

    # Append trial info to
    data["Stimulus"].append(stim)
    data["Stimulus_Color"].append(stim_color)
    data["Answer"].append(answer)
    data["RT"].append(RT)

    # Categorize the condition
    if stim == "RED" and stim_color == "raw_red":
        data["Condition"].append("Congruent")
    elif stim == "GREEN" and stim_color == "raw_green":
        data["Condition"].append("Congruent")
    elif stim == "BLUE" and stim_color == "raw_blue":
        data["Condition"].append("Congruent")
    else:
        data["Condition"].append("Incongruent")

    # Categorize the response
    if answer == "LEFT" and stim_color == "raw_red":
        data["Correct"].append(1)
    elif answer == "DOWN" and stim_color == "raw_green":
        data["Correct"].append(1)
    elif answer == "RIGHT" and stim_color == "raw_blue":
        data["Correct"].append(1)
    else:
        data["Correct"].append(0)

df = pd.DataFrame.from_dict(data)  # Convert dict to a dataframe
df.to_csv("data.csv")  # Save data

n.close()  # Close neuropsydia



