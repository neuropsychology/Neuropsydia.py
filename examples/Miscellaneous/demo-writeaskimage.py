# -*- coding: utf-8 -*-
import neuropsydia as n

n.start()

n.write("Welcome", style="title")
name = n.ask("What is your name?", y=5)
n.write("Ok, " + name + ", here is a super cool cat.", y=3)
n.image("cat.png", size=3, y=-3.5)
n.refresh()
n.time.wait(2000)

n.close()