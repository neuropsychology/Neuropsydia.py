# -*- coding: utf-8 -*-
import neuropsydia as n

n.start()

n.newpage()

response = n.choice(["Yes", "No"], y=5, title="Isn't it easy?")

response = n.choice(["Hell no", "Nope", "Dunno", "Sure"],
                    y=-5,
                    title="Am I better looking?",
                    height=-2,
                    boxes_edge_size=0,
                    boxes_background=["red", "amber", "teal", "blue"],
                    help_list=["means not at all", "means no", "means you don't know", "means yes"])

n.close()
