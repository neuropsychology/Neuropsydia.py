# -*- coding: utf-8 -*-
import neuropsydia as n  # Load neuropsydia
import random  # Import the random module
import pandas as pd  # To manipulate and save the data
import numpy as np  # To do some maths

n.start()  # Start neuropsydia
n.instructions("Goal: Hit SPACE whenever a GREEN circle appears. \nWhen it is RED, don't press anything.")  # Display instructions and break line with \n
n.newpage("grey")  # Fill the screen
n.countdown()  # Display countdown

# Initialize the data storage with a dictionary containing empty lists
data = {"Trial": [],
        "Stimulus": [],
        "ISI":[],
        "RT":[],
        "Response":[]}

for trial in range(5):  # Iterate over the number of trials
    stimulus = random.choice(["green", "red"])  # Select a stimulus type
    ISI = random.randrange(start=500, stop=2000, step=500)  # Select the inter-stimuli interval (ISI)

    n.newpage("grey")  # Fill the screen
    n.write("+")  # Fixation cross
    n.refresh()  # Diplay it on screen
    n.time.wait(ISI)  # Wait

    n.circle(size=2, fill_color=stimulus)  # Display the stimulus (filled with the color selected above)
    n.refresh()  # Diplay it on screen
    response, RT = n.response(time_max=1500)  # Wait until 1.5s and collect the response and its time

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
RTs = df.query('Response=="HIT"')["RT"]  # Select the Hits' RTs
print(np.mean(RTs), np.std(RTs))  # Print the mean and the standard deviation
print(len(df.query('Response=="FA"')))  # Print the number of intrusions (false alarms)

n.close()  # Close neuropsydia
