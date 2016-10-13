# -*- coding: utf-8 -*-
import neuropsydia as n

n.start()
n.newpage()

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
        separation_labels=["Bad","Good"],
        style="purple",
        show_result=True,
        show_result_shape_line_color="blue"
        )

n.close()

