# -*- coding: utf-8 -*-
import neuropsydia as n

questions_dictionary = {

    "Item": {
        1: "Is Neuropsydia great?",
        2: "Is Neuropsydia not great?",
        3: "Is Python great?",
        4: "Is Python not great?"
    },
    "Reverse": {
        1: False,
        2: True,
        3: False,
        4: True
    },
    "Dimension": {
        1: "Neuropsydia",
        2: "Neuropsydia",
        3: "Python",
        4: "Python"
    }

}

n.start()
n.questionnaire(questions_dictionary,  # The questions
                anchors=["Not at all", "Absolutely"],  # The edges of the scale
                results_save=True,  # Should it save the data?
                dimensions_mean=True,  # Compute the mean by dimension?
                analog=False,  # Lickert-like
                edges=[0, 7],  # Values underneath
                style="blue",  # The cursor's colour
                randomize=True,  # Randomize the question's order
                instructions_text="Here are the instructions")  # Add instructions at the beginning
n.close()
