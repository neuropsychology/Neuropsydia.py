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
#n.questionnaire(questions_dictionary, anchors=["", ""], results_save=True, dimensions_mean=True,
#                style="blue",
#                analog=False,
#                edges=[1,5],
#labels=["not at all", "not really", "maybe", "quite", "totally"],
#labels_size=0.6)

n.background_color()
n.scale(title="Is Python great?",
        y=3.3,
        anchors=["", ""],
        style="blue",
        analog=False,
        edges=[1,5],
        labels=["not at all", "not really", "maybe", "quite", "totally"],
        labels_size=0.6
        )
n.scale(title="How is neuropsydia?",
        y=-3.3,
        line_length=12,
        edges=[0,100],
        anchors=["atrocious", "brilliant"],
        point_center=True,
        force_separation=2,
        separation_labels=["Bad","Good"],
        style="purple",
        show_result=True,
        show_result_shape_line_color="blue"
        )

n.close()

