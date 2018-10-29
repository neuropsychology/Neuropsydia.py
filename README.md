<p><header><a href=http://neuropsydia.readthedocs.io/><img src="https://github.com/neuropsychology/neuropsydia/blob/master/neuropsydia/files/logo/neuropsydia_banner.png" width="700" align="center" alt="neuropsydia python for research"></a></header></p>

A Python Module for Creating Experiments, Tasks and Questionnaires.

---



|Name|neuropsydia|
|----------------|---|
|Latest Version|[![PyPI version](https://badge.fury.io/py/neuropsydia.svg)](https://badge.fury.io/py/neuropsydia)|
|Documentation|[![Documentation Status](http://readthedocs.org/projects/neuropsydia/badge/?version=latest)](http://neuropsydia.readthedocs.io/en/latest/?badge=latest)|
|Discussion|[![Join the chat at https://gitter.im/Neuropsydia-py/Lobby](https://badges.gitter.im/Neuropsydia-py/Lobby.svg)](https://gitter.im/Neuropsydia-py/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)|
|Questions|[![](https://img.shields.io/badge/issue-create-purple.svg?colorB=FF9800)](https://github.com/neuropsychology/Neuropsydia.py/issues)|
|Authors|[![](https://img.shields.io/badge/CV-D._Makowski-purple.svg?colorB=9C27B0)](https://dominiquemakowski.github.io/) [![](https://img.shields.io/badge/CV-L._Dutriaux-purple.svg?colorB=9C27B0)](http://recherche.parisdescartes.fr/LaboratoireMemoireCognition_esl/Membres/Doctorants-Allocataires/Leo-Dutriaux)|
|Support|Windows 7, 8, 10|


---
# Installation
To get the latest stable version (`1.0.6`), run the following in the [command prompt](https://docs.python.org/3/installing/) (might take a few minutes):
```python
pip install https://github.com/neuropsychology/Neuropsydia.py/zipball/master
```


Not working? Check [this](http://neurokit.readthedocs.io/en/latest/tutorials/Python.html) out!


**NOTE: We strongly recommend (for Windows users) the use of the [WinPython](https://winpython.github.io/) bundle, that will allow  you to have a ready-to-go scientific and portable Python setup.**
<p align="left">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-installation.gif" height="500" alt="installation neuropsydia winpython pip">
</a>
</p>

To upgrade Neuropsydia, uninstall it and reinstall it :wink:.
```python
pip uninstall neuropsydia
```
---
# Contribute
- You need some help? You found a bug? You would like to request a new feature? 
  Just open an [issue](https://github.com/neuropsychology/Neuropsydia.py/issues) :relaxed:
- Want to add yourself a feature? Correct a bug? You're more than welcome to contribute!
  Check [this page](http://ecole-de-neuropsychologie.readthedocs.io/en/latest/Contributing/Contribute/) to see how to submit your changes on github.

## Citation
You can cite Neuropsydia with the following:
```
Makowski, D. & Dutriaux, L. (2016). Neuropsydia: A Python Module for Creating Experiments, Tasks and Questionnaires. 
Memory and Cognition Lab' Day, 01 November, Paris, France
```
*Note: The authors do not give any warranty. If this software causes your keyboard to blow up, your brain to liquefy, your toilet to clog or a zombie plague to leak, the authors CANNOT IN ANY WAY be held responsible.*

---
# Tutorials, Examples and Documentation

- [Tutorials]( http://neuropsydia.readthedocs.io/en/latest/tutorials/index.html)
  - [x] Getting Started
  - [x] Create a Stroop Task
- [Examples]( http://neuropsydia.readthedocs.io/en/latest/examples/index.html)
  - [x] State-Trait Anxiety Inventory (STAI-Y)
  - [x] Digit Span
  - [x] Go/No Go
  - [x] Flanker
- [API Documentation]( http://neuropsydia.readthedocs.io/en/latest/documentation.html)



---
# Example
## A Go/No-Go Task in 50 lines

<p align="left">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-gonogo.gif" height="500" alt="interactive scale psychology">
</a>
</p>

Try this!

```python
import neuropsydia as n  # Load neuropsydia
import random  # Import the random module
import pandas as pd  # To manipulate and save the data
import numpy as np  # To do some maths

n.start()  # Start neuropsydia
n.instructions("Goal: Hit SPACE whenever a GREEN circle appears. \nWhen it is RED, don't press anything.")  # Display instructions and break line with \n
n.newpage("grey")  # Fill the screen
n.countdown()  # Display countdown

# Initialize the data storage with a dictionary containing empty lists
data = {"Trial": [],
        "Stimulus": [],
        "ISI":[],
        "RT":[],
        "Response":[]}

for trial in range(5):  # Iterate over the number of trials
    stimulus = random.choice(["green", "red"])  # Select a stimulus type
    ISI = random.randrange(start=500, stop=2000, step=500)  # Select the inter-stimuli interval (ISI)

    n.newpage("grey")  # Fill the screen
    n.write("+")  # Fixation cross
    n.refresh()  # Diplay it on screen
    n.time.wait(ISI)  # Wait

    n.circle(size=2, fill_color=stimulus)  # Display the stimulus (filled with the color selected above)
    n.refresh()  # Diplay it on screen
    response, RT = n.response(time_max=1500)  # Wait until 1.5s and collect the response and its time

    # Categorize the response
    if response == "SPACE" and stimulus == "green":
        response_type = "HIT"  # Hit
    if response != "SPACE" and stimulus == "green":
        response_type = "MISS"  # Miss
    if response == "SPACE" and stimulus == "red":
        response_type = "FA"  # False Alarm
    if response != "SPACE" and stimulus == "red":
        response_type = "CR"  # Correct Rejection

    # Store data by appending each item to its list
    data["Trial"].append(trial)
    data["Stimulus"].append(stimulus)
    data["ISI"].append(ISI)
    data["RT"].append(RT)
    data["Response"].append(response_type)

# Data saving
df = pd.DataFrame.from_dict(data)  # Transform the data dictionary into a proper and savable dataframe
df.to_csv("data.csv")  # Save it

# Quick analysis
RTs = df.query('Response=="HIT"')["RT"]  # Select the Hits' RTs
print("Mean RT: " + str(round(RTs.mean(), 2)))   # Print the mean
print("SD RT: " + str(round(RTs.std(), 2)))  # Print the standard deviation
print("Number of False Alarms: " + str(len(df[df['Response']=="FA"])))  # Print the number of intrusions (false alarms)

n.close()  # Close neuropsydia
```

---
# Features



## Write, Ask and Display Images

- [x] Easily write, display images and interact with the user.
- [x] Detailed control over the timing and latency: preload images and display them exactly whenever you want.

<p align="left">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-writeaskimage.gif" height="500" alt="interactive scale psychology">
</a>
</p>

```python
import neuropsydia as n

n.start()

n.write("Welcome", style="title")
name = n.ask("What is your name?", y=5)
n.write("Ok, " + name + ", here is a super cool cat.", y=3)
n.image("cat.png", size=3, y=-3.5)
n.refresh()
n.time.wait(2000)

n.close()
```

---
## Scales and Questionnaires
- [x] Fully automated questionnaires.
- [x] Powerful scale creation.

<p align="left">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-scale.gif" height="500" alt="interactive scale psychology">
</a>
</p>

```python
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
``` 

---
## Choices
- [x] Easily display clickable choices, useful in case of recognition tasks or so.

<p align="left">
<a href="">
<img src="https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-choice.gif" height="500" alt="interactive choice psychology remember guess know">
</a>
</p>

```python
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
``` 
