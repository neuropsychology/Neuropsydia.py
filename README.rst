.. raw:: html
	<embed>
	<img src="https://github.com/neuropsychology/neuropsydia/blob/master/neuropsydia/files/logo/neuropsydia_banner.png" width="50%" align="left">
    </embed>
	
.. image:: https://github.com/neuropsychology/neuropsydia/blob/master/neuropsydia/files/logo/neuropsydia_banner.png
    :target: https://github.com/neuropsychology/neuropsydia/blob/master/neuropsydia/files/logo/neuropsydia_banner.png
    :scale: 50 %
    :align: center
    :alt: neuropsydia python for research
	
A Python module for creating experiments, tasks and questionnaires.

--------------

+------------------+-------------------------------------------------------------+
| Name             | neuropsydia                                                 |
+==================+=============================================================+
| Latest Version   | |PyPI version|                                              |
+------------------+-------------------------------------------------------------+
| Documentation    | |Documentation Status|                                      |
+------------------+-------------------------------------------------------------+
| Discussion       | |Join the chat at https://gitter.im/Neuropsydia-py/Lobby|   |
+------------------+-------------------------------------------------------------+
| Authors          | |image3| |image4|                                           |
+------------------+-------------------------------------------------------------+
| Support          | Windows 7, 8, 10                                            |
+------------------+-------------------------------------------------------------+

--------------



Installation
============
To get the latest stable version (:code:`1.0.0`), run the following in the `command prompt <https://docs.python.org/3/installing/>`_ (might take a few minutes):

.. code:: python

    pip install neuropsydia


To get the latest development version (:code:`1.0.1`), run the following:

.. code:: python

  pip install https://github.com/neuropsychology/Neuropsydia.py/zipball/dev

**NOTE: We strongly recommend (for Windows users) the use of the** `WinPython <https://winpython.github.io/>`_ **bundle, that will allow  you to have a ready-to-go scientific and portable Python setup.**

.. image:: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-installation.gif
    :target: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-installation.gif
    :scale: 50 %
    :align: left
    :alt: installation neuropsydia winpython pip


To upgrade Neuropsydia, uninstall it and reinstall it :wink:.

.. code:: python

  pip uninstall neuropsydia


Contribute
==========

-  You need some help? You found a bug? You would like to request a new
   feature? Just open an `issue <https://github.com/neuropsychology/Neuropsydia.py/issues>`__ :relaxed:
-  Want to add yourself a feature? Correct a bug? You're more than
   welcome to contribute! Check `this page <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/Contributing/Contribute/>`__
   to see how to submit your changes on github.

Citation
--------

You can cite Neuropsydia with the following:

::

    Makowski, D. & Dutriaux, L. (2016). Neuropsydia: A Python Module for Creating Experiments, Tasks and Questionnaires. 
    Memory and Cognition Lab' Day, 01 November, Paris, France

*Note: The authors do not give any warranty. If this software causes
your keyboard to blow up, your brain to liquefy, your toilet to clog or
a zombie plague to leak, the authors CANNOT IN ANY WAY be held
responsible.*


--------------

Tutorials
=========

Tutorials are currently under development. Check out `this page <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/Contributing/Contribute/>`_ to help us improve them.

- Novice

  - `1.0 Getting Started <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/CreatingExperiments/Neuropsydia.py/Tutorials/Novice/#part-10-getting-started>`_
  - `1.1 Computerize a questionnaire <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/CreatingExperiments/Neuropsydia.py/Tutorials/Novice/#part-11-computerize-a-questionnaire>`_
  - `1.2 Complexify this questionnaire <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/CreatingExperiments/Neuropsydia.py/Tutorials/Novice/#part-12-complexify-this-questionnaire>`_
  - `1.3 Include info about the participant <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/CreatingExperiments/Neuropsydia.py/Tutorials/Novice/#part-13-include-info-about-the-participant>`_
  - 1.4 The novice's trial
  
- Apprentice

  - 2.0 Basics of Python programming
  - `2.1 Structuring your Code <http://ecole-de-neuropsychologie.readthedocs.io/en/latest/CreatingExperiments/Neuropsydia.py/Tutorials/Apprentice/#part-21-structuring-your-code>`_
  - 2.1 Create a Stroop task
  - 2.2 The apprentice's trial
  
- Companion

  - 3.0 Create a more complex experiment
  - 3.1 The companion's trial
  
- Master

  - 4.0 Improve timing and precision
  - 4.1 Data manipulation and analysis
  - 4.2 The master's trial
  
  
--------------
  
Example
=======

A Go/No-Go Task in 50 lines
---------------------------

.. image:: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-gonogo.gif
    :target: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-gonogo.gif
    :scale: 50 %
    :align: left
    :alt: interactive scale psychology
	


**Try this!**

.. code:: python

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
    print(np.mean(RTs), np.std(RTs))  # Print the mean and the standard deviation
    print(len(df.query('Response=="FA"')))  # Print the number of intrusions (false alarms)

    n.close()  # Close neuropsydia

--------------
  
Features
========

Write, Ask and Display Images
-----------------------------
- Easily write, display images and interact with the user.
- Detailed control over the timing and latency: preload images and display them exactly whenever you want.

.. image:: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-writeaskimage.gif
    :target: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-writeaskimage.gif
    :scale: 50 %
    :align: left
    :alt: write ask and display images
    
    
.. code:: python

	import neuropsydia as n

	n.start()

	n.write("Welcome", style="title")
	name = n.ask("What is your name?", y=5)
	n.write("Ok, " + name + ", here is a super cool cat.", y=3)
	n.image("cat.png", size=3, y=-3.5)
	n.refresh()
	n.time.wait(2000)

	n.close()


Scales and Questionnaires
-------------------------

-  Fully automated questionnaires.
-  Powerful scale creation.


.. image:: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-scale.gif
    :target: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-scale.gif
    :scale: 50 %
    :align: left
    :alt: interactive scale psychology
	


.. code:: python

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

--------------

Choices
-------

-  Easily display clickable choices, useful in case of recognition tasks or so.

.. image:: https://github.com/neuropsychology/Neuropsydia.py/blob/master/examples/Files/demo-choice.gif
    :scale: 50 %
    :align: left
	:alt: interactive choice psychology remember guess know
	

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

	
	
	
	
	
.. |PyPI version| image:: https://badge.fury.io/py/neuropsydia.svg
   :target: https://badge.fury.io/py/neuropsydia
.. |Documentation Status| image:: http://readthedocs.org/projects/neuropsydia/badge/?version=latest
   :target: http://neuropsydia.readthedocs.io/en/latest/?badge=latest
.. |Join the chat at https://gitter.im/Neuropsydia-py/Lobby| image:: https://badges.gitter.im/Neuropsydia-py/Lobby.svg
   :target: https://gitter.im/Neuropsydia-py/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |image3| image:: https://img.shields.io/badge/CV-D._Makowski-purple.svg?colorB=9C27B0
   :target: https://cdn.rawgit.com/neuropsychology/Organization/master/CVs/DominiqueMakowski.pdf
.. |image4| image:: https://img.shields.io/badge/CV-L._Dutriaux-purple.svg?colorB=9C27B0
   :target: http://recherche.parisdescartes.fr/LaboratoireMemoireCognition_esl/Membres/Doctorants-Allocataires/Leo-Dutriaux
