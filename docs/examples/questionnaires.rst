Questionnaires
================


State-Trait Anxiety Inventory (STAI-Y)
---------------------------------------

.. code:: python


    import neuropsydia as n  # Load neuropsydia


    questions_dictionary = {

        "Item": {
            1: "I feel calm.",
            2: "I feel secure.",
            3: "I am tense.",
            4: "I feel strained.",
            5: "We're not allowed to reveal all the questions :("  # As it is the last dict item, no comma after that.
        },
        "Reverse": {
            1: True,
            2: True,
            3: False,
            4: False,
            5: False
        }
    }

    n.start()  # Initialize neuropsydia

    participant_id = n.ask("Participant ID:", order=1)  # Get participant id
    participant_gender = n.ask("Gender:", order=2)  # Get participant's gender
    participant_age = n.ask("Age:", order=3)  # get participant's age

    df = n.questionnaire(questions_dictionary,  # The questions
                    participant_id=participant_id,
                    analog=False,  # Lickert-like
                    edges=[1, 4],  # Values underneath
                    labels=["Almost never", "Sometimes", "Often", "Almost always"],
                    style="blue",  # The cursor's color
                    instructions_text="A number of statements which people have used to describe themselves are given below. \nSelect the number that indicate how you feel right now, that is, at this moment. \nThere are no right or wrong answers. Do not spend too much time on any one statement but give the answer which seems to describe your present feelings best.")  # Add instructions at the beginning


    # Scoring
    score = df["Answer"].sum()

    # Cutoff based on Crawford et al. (2011). This just for illustration purposes, adapt it following your activity.
    if score > 56:
        interpretation = "Possible Anxiety"
    else:
        interpretation = "No anxiety"

    # Add info and save
    df["Participant_ID"] = participant_id
    df["Participant_Gender"] = participant_gender
    df["Participant_Age"] = participant_age
    df["Score"] = score
    df["Interpretation"] = interpretation
    df.to_csv("STAI_" + participant_id + ".csv")

    n.close()  # Close neuropsydia

    
.. hint:: Try to run this questionnaire!

   - Can you add all missing questions from a legal version?
   - Can you computerize the trait version?