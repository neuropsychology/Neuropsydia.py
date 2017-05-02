# -*- coding: utf-8 -*-
"""
Code example of a computerized questionnaire, the Beck Depression Inventory (BDI).
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia
import pandas as pd


items = {
        1: {0: "I do not feel sad.",
             1: "I feel sad.",
             2: "I am sad all the time and I can't snap out of it.",
             3: "I am so sad and unhappy that I can't stand it."
             },
        2: {0: "I am not particularly discouraged about the future.",
             1: "I feel discouraged about the future.",
             2: "I feel I have nothing to look forward to.",
             3: "I feel the future is hopeless and that things cannot improve."
             },
        3: {0: "I do not feel like a failure.",
             1: "I feel I have failed more than the average person.",
             2: "As I look back on my life, all I can see is a lot of failures.",
             3: "I feel I am a complete failure as a person."
             }
        # I cannot legally show the rest of the questions
        }



n.start()  # Initialize neuropsydia

participant_id = n.ask("Participant ID:", order=1)  # Get participant id
participant_gender = n.ask("Gender:", order=2)  # Get participant's gender
participant_age = n.ask("Age:", order=3)  # get participant's age

n.instructions("Please tell if you agree with each following proposition.")  # Instructions


data = {}  # Initialize empty data dict
for item in items:

    data[item] = {}  # For each item, initialize empty sub-dict

    for proposition_number in items[item]:

        question = items[item][proposition_number]  # Current proposition

        n.newpage()
        n.write("\n\n\n" + question, long_text=True)  # Display current proposition
        answer = n.choice([0, 1],
                          overwrite_choices_display=["No", "Yes"],
                          boxes_edge_size=0,
                          boxes_background="teal")

        # Loop control
        if proposition_number == 0:
            if answer == 1:
                break
        else:
            if answer == 0:
                break

    data[item]["Proposition"] = question  # Store the current proposition
    data[item]["Score"] = proposition_number  # Store the score

# Convert to dataframe and store info
df = pd.DataFrame.from_dict(data, orient="index")
df["Participant_ID"] = participant_id
df["Participant_Gender"] = participant_gender
df["Participant_Age"] = participant_age

# Analysis and saving
df["Score_Total"] = df["Score"].sum()
df.to_csv("BDI_" + participant_id + ".csv")

n.close()  # Close neuropsydia


