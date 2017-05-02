# -*- coding: utf-8 -*-
"""
Code example of a computerized questionnaire, the Beck Depression Inventory (BDI).
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n  # Load neuropsydia



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
             }
        # I cannot legally show the rest of the questions
        }



n.start()  # Initialize neuropsydia

#participant_id = n.ask("Participant ID:", order=1)  # Get participant id
#participant_gender = n.ask("Gender:", order=2)  # Get participant's gender
#participant_age = n.ask("Age:", order=3)  # get participant's age
#
#n.instructions("Listen to the experimenter.")



for item in items:
    for proposition in item:
        n.newpage()
        answer = n.choice([0, 1], overwrite_choices_display=["No", "Yes"])
        if answer == 0:
            break

n.close()  # Close neuropsydia

