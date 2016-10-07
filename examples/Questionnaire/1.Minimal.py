# -*- coding: utf-8 -*-
import neuropsydia as n  # Load neuropsydia


questions_dictionary = {

    "Item": {
        1: "Is Neuropsydia great?",
        2: "Is Neuropsydia not great?",
        3: "Is Python great?",
        4: "Is Python not great?"
    }
}


n.start()
n.questionnaire(questions_dictionary)
n.close()
