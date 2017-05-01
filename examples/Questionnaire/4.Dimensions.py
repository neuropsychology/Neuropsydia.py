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
n.questionnaire(questions_dictionary,
                anchors=["No", "Yes"],
                results_save=True,
                dimensions_mean=True)
n.close()
