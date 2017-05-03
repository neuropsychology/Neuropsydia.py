# -*- coding: utf-8 -*-
"""
Test suite.
Authors: Dominique Makowski
Copyright: The Neuropsydia Development Team
Site: https://github.com/neuropsychology/Neuropsydia.py
"""
import neuropsydia as n


n.start()

n.write("dupa")
n.refresh()
n.time.wait(100)
n.newpage()
n.image("img.jpg", fullscreen=True)
n.refresh()
n.time.wait(100)

n.close()

print("STATUS: PASSED.")