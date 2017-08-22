2. Create a Stroop Task
=========================


Contact
---------

For remarks, complaints, suggestions or anything else, please create an `issue <https://github.com/neuropsychology/Neuropsydia.py/issues>`_.


Denomination
--------------------

The first phase of the Stroop task consists of a training/baseline part referred to as the denomination. Neutral stimuli ("XXXX") are colored in red, blue or green, and the participant must respond as quick as possible.

Let's take our program skeleton:

.. code:: python

    import neuropsydia as n
     
    n.start()
    # Here will go the program code
    n.close()


To display stimuli, we will use the :code:`write()` function that we will insert in a :code:`for` loop.


.. code:: python

    import neuropsydia as n  # Load neuropsydia

    n.start()  # Start neuropsydia

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        n.newpage("grey")  # Neutral grey background
        n.write("XXXX")  # Load the stimulus
        n.refresh()  # Display it
        n.response()  # Wait for response

    n.close()  # Close neuropsydia


Run the program (F5). As you can see, it works, but it's far from being usable. We have to add colors to the stimuli and record the response. Also, add instructions.

.. code:: python

    import neuropsydia as n  # Load neuropsydia
    import numpy as np  # Load numpy

    
    n.start()  # Start neuropsydia

    n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
        n.newpage("grey")  # Neutral grey background
        n.write("XXXX", style="bold", color=stim_color, size=3)  # Load the stimulus
        n.refresh()  # Display it
        answer, RT = n.response()  # Record response and response time
        if answer == "ESCAPE":  # Enable experiment quit by pressing escape
            quit()

    n.close()  # Close neuropsydia

    
Much better. Now, we're gonna analyze the response (if correct or not) and store them within a dict.

.. code:: python

    import neuropsydia as n  # Load neuropsydia
    import numpy as np  # Load numpy

    n.start()  # Start neuropsydia

    # Initialize data storage
    data = {"Stimulus": [],
            "Stimulus_Color": [],
            "Answer": [],
            "RT": [],
            "Condition": [],
            "Correct": []}

    #==============================================================================
    # Part 1: Denomination
    #==============================================================================

    n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
        stim = "XXXX"
        n.newpage("grey")  # Neutral grey background
        n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
        n.refresh()  # Display it
        answer, RT = n.response()  # Record response and response time
        if answer == "ESCAPE":  # Enable experiment quit by pressing escape
            quit()

        # Append trial info to
        data["Stimulus"].append(stim)
        data["Stimulus_Color"].append(stim_color)
        data["Answer"].append(answer)
        data["RT"].append(RT)
        data["Condition"].append("Neutral")

        # Categorize the response
        if answer == "LEFT" and stim_color == "raw_red":
            data["Correct"].append(1)
        elif answer == "DOWN" and stim_color == "raw_green":
            data["Correct"].append(1)
        elif answer == "RIGHT" and stim_color == "raw_blue":
            data["Correct"].append(1)
        else:
            data["Correct"].append(0)

    n.close()  # Close neuropsydia

    print(data)


Conflict
--------------------

The only thing that will change in the second part is that the stimulus will not always be XXXX, but a color name.

.. code:: python

    import neuropsydia as n  # Load neuropsydia
    import numpy as np  # Load numpy

    n.start()  # Start neuropsydia

    # Initialize data storage
    data = {"Stimulus": [],
            "Stimulus_Color": [],
            "Answer": [],
            "RT": [],
            "Condition": [],
            "Correct": []}

    #==============================================================================
    # Part 1: Denomination
    #==============================================================================

    n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
        stim = "XXXX"
        n.newpage("grey")  # Neutral grey background
        n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
        n.refresh()  # Display it
        answer, RT = n.response()  # Record response and response time
        if answer == "ESCAPE":  # Enable experiment quit by pressing escape
            quit()

        # Append trial info to
        data["Stimulus"].append(stim)
        data["Stimulus_Color"].append(stim_color)
        data["Answer"].append(answer)
        data["RT"].append(RT)
        data["Condition"].append("Neutral")

        # Categorize the response
        if answer == "LEFT" and stim_color == "raw_red":
            data["Correct"].append(1)
        elif answer == "DOWN" and stim_color == "raw_green":
            data["Correct"].append(1)
        elif answer == "RIGHT" and stim_color == "raw_blue":
            data["Correct"].append(1)
        else:
            data["Correct"].append(0)

    #==============================================================================
    # Part 2: Conflict
    #==============================================================================

    n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
        stim = np.random.choice(["RED", "GREEN", "BLUE"])
        n.newpage("grey")  # Neutral grey background
        n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
        n.refresh()  # Display it
        answer, RT = n.response()  # Record response and response time
        if answer == "ESCAPE":  # Enable experiment quit by pressing escape
            quit()

        # Append trial info to
        data["Stimulus"].append(stim)
        data["Stimulus_Color"].append(stim_color)
        data["Answer"].append(answer)
        data["RT"].append(RT)

        # Categorize the condition
        if stim == "RED" and stim_color == "raw_red":
            data["Condition"].append("Congruent")
        elif stim == "GREEN" and stim_color == "raw_green":
            data["Condition"].append("Congruent")
        elif stim == "BLUE" and stim_color == "raw_blue":
            data["Condition"].append("Congruent")
        else:
            data["Condition"].append("Incongruent")

        # Categorize the response
        if answer == "LEFT" and stim_color == "raw_red":
            data["Correct"].append(1)
        elif answer == "DOWN" and stim_color == "raw_green":
            data["Correct"].append(1)
        elif answer == "RIGHT" and stim_color == "raw_blue":
            data["Correct"].append(1)
        else:
            data["Correct"].append(0)

    n.close()  # Close neuropsydia
    
    
    
Finally, just before the end (before the close), we can transform the data dict into a :code:`pandas.DataFrame`, that can then be easily saved. Don't forget to import pandas at the beginning.


.. code:: python

    import neuropsydia as n  # Load neuropsydia
    import numpy as np  # Load numpy
    import pandas as pd  # Load pandas

    n.start()  # Start neuropsydia

    # Initialize data storage
    data = {"Stimulus": [],
            "Stimulus_Color": [],
            "Answer": [],
            "RT": [],
            "Condition": [],
            "Correct": []}

    #==============================================================================
    # Part 1: Denomination
    #==============================================================================

    n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
        stim = "XXXX"
        n.newpage("grey")  # Neutral grey background
        n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
        n.refresh()  # Display it
        answer, RT = n.response()  # Record response and response time
        if answer == "ESCAPE":  # Enable experiment quit by pressing escape
            quit()

        # Append trial info to
        data["Stimulus"].append(stim)
        data["Stimulus_Color"].append(stim_color)
        data["Answer"].append(answer)
        data["RT"].append(RT)
        data["Condition"].append("Neutral")

        # Categorize the response
        if answer == "LEFT" and stim_color == "raw_red":
            data["Correct"].append(1)
        elif answer == "DOWN" and stim_color == "raw_green":
            data["Correct"].append(1)
        elif answer == "RIGHT" and stim_color == "raw_blue":
            data["Correct"].append(1)
        else:
            data["Correct"].append(0)

    #==============================================================================
    # Part 2: Conflict
    #==============================================================================

    n.instructions("Press LEFT when RED, DOWN when GREEN and RIGHT when BLUE.")

    n_trials = 10
    for trial in range(n_trials):
        n.newpage("grey")  # Neutral grey background
        n.write("+")  # Fixation cross
        n.refresh()  # Display it
        n.time.wait(250)  # Wait 250 ms

        stim_color = np.random.choice(["raw_red", "raw_green", "raw_blue"])  # Choose a color
        stim = np.random.choice(["RED", "GREEN", "BLUE"])
        n.newpage("grey")  # Neutral grey background
        n.write(stim, style="bold", color=stim_color, size=3)  # Load the stimulus
        n.refresh()  # Display it
        answer, RT = n.response()  # Record response and response time
        if answer == "ESCAPE":  # Enable experiment quit by pressing escape
            quit()

        # Append trial info to
        data["Stimulus"].append(stim)
        data["Stimulus_Color"].append(stim_color)
        data["Answer"].append(answer)
        data["RT"].append(RT)

        # Categorize the condition
        if stim == "RED" and stim_color == "raw_red":
            data["Condition"].append("Congruent")
        elif stim == "GREEN" and stim_color == "raw_green":
            data["Condition"].append("Congruent")
        elif stim == "BLUE" and stim_color == "raw_blue":
            data["Condition"].append("Congruent")
        else:
            data["Condition"].append("Incongruent")

        # Categorize the response
        if answer == "LEFT" and stim_color == "raw_red":
            data["Correct"].append(1)
        elif answer == "DOWN" and stim_color == "raw_green":
            data["Correct"].append(1)
        elif answer == "RIGHT" and stim_color == "raw_blue":
            data["Correct"].append(1)
        else:
            data["Correct"].append(0)

    df = pd.DataFrame.from_dict(data)  # Convert dict to a dataframe
    df.to_csv("data.csv")  # Save data

    n.close()  # Close neuropsydia