Tasks
=======


Digit Span
-------------


.. code:: python

    import neuropsydia as n  # Load neuropsydia
    import numpy as np  # For generation of random sequence


    n.start()  # Initialize neuropsydia
    n.instructions("Listen to the experimenter.")  # Display instructions

    # Initialize values
    number_of_fails = 0  # Initial number of errors
    span = 2  # Initial span

    while number_of_fails < 3:  # Do it while the number of errors is smaller than 3
        sequence = np.random.randint(10, size=span)  # Generate sequence of size span with ints ranging from 0 to 9
        good_answer = ""  # Initiate an empty good_answer

        for digit in sequence:  # For every digit in the sequence...
            good_answer = good_answer + str(digit)  # Add the current stimulus to the good answer
            n.newpage("grey")  # Load a grey background
            n.time.wait(250)  # Display an empty screen for 250 ms
            n.newpage("grey")  # Load a grey background
            n.write(digit, size=3)  # Load the stimulus
            n.refresh()  # Display the stimulus on screen
            n.time.wait(1000)  # Wait 1000 ms

        # Get answer
        n.newpage("white")
        answer = n.ask("Answer:")

        # Manage result
        if answer == good_answer:
            span = span + 1  # Increase span
            number_of_fails = 0  # Reset value
        else:
            number_of_fails = number_of_fails + 1

    n.newpage()  # Load a white background
    n.write("Max span: " + str(span-1))  # Write task result
    n.refresh()  # Render it on screen
    n.time.wait(3000)  # Wait for 3s

    n.close()  # Close neuropsydia

.. hint:: Try to run this task!

   - Can you change the sequence generation so it contains letters rather than digits?
   - Can you change the rules so the sequence length increases every two good answers?
   - Can you store the results and save them?
   
   
   
Go/No Go
-------------



.. code:: python

    import neuropsydia as n  # Load neuropsydia
    import random  # Import the random module
    import pandas as pd  # To manipulate and save data
    import numpy as np  # To do some maths

    n.start()  # Start neuropsydia
    n.instructions("Goal: Hit SPACE whenever a GREEN circle appears. \nIf RED, don't press anything!")  # Display instructions and break line with \n
    n.newpage("grey")  # Fill the screen
    n.countdown()  # Display countdown

    # Initialize the data storage with a dictionary containing empty lists
    data = {"Trial": [],
            "Stimulus": [],
            "ISI":[],
            "RT":[],
            "Response":[]}

    n_trials = 10  # Number of trials
    for trial in range(n_trials):  # Iterate over the number of trials
        stimulus = random.choice(["green", "green", "green", "red"])  # Select a stimulus type
        ISI = random.randrange(start=250, stop=1250, step=250)  # Select the inter-stimuli interval (ISI)

        n.newpage("grey")  # Fill the screen
        n.write("+")  # Fixation cross
        n.refresh()  # Diplay it on screen
        n.time.wait(ISI)  # Wait

        n.circle(size=2, fill_color=stimulus)  # Display the stimulus (filled with the color selected above)
        n.refresh()  # Diplay it on screen
        response, RT = n.response(time_max=1000)  # Wait until 1 s and collect the response and its time

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
    RTs = df[df['Response']=="HIT"]["RT"]  # Select the Hits' RTs
    print("Mean RT: " + str(round(RTs.mean(), 2)))   # Print the mean
    print("SD RT: " + str(round(RTs.std(), 2)))  # Print the standard deviation
    print("Number of False Alarms: " + str(len(df[df['Response']=="FA"])))  # Print the number of intrusions (false alarms)

    n.close()  # Close neuropsydia

.. hint:: Try to run this task!

   - Can you change the number of trials?
   - Can you change the ratio of no go trials?
   
   
Flanker
--------

.. code:: python


    import neuropsydia as n  # Load neuropsydia
    import pandas as pd  # To manipulate and save data
    import numpy as np  # To do some maths

    n.start()  # Start neuropsydia
    n.instructions("Hit RIGHT or LEFT arrow according to the direction of the CENTRAL arrow.")  # Display instructions

    # Initialize cache
    cache = {}
    for possible_angle in [0, 90, 180]:
        cache = n.preload("arrow-left.png", size=2, rotate=possible_angle, cache=cache)  # Preload images

    # Initialize the data storage with a dictionary containing empty lists
    data = {"Trial": [],
            "Trial_Type": [],
            "Stimulus_Orientation": [],
            "RT":[],
            "Response":[]}


    n.newpage("grey")  # Fill the screen
    n.countdown()  # Display countdown

    n_trials = 10  # Number of trials
    for trial in range(n_trials):  # Iterate over the number of

        n.newpage("grey")  # Fill the screen
        n.write("+")  # Fixation cross
        n.refresh()  # Diplay it on screen
        n.time.wait(500)  # Wait

        # Trial characteristics
        stimulus_angle = np.random.choice([0, 180])  # select target orientation
        trial_type = np.random.choice(["Congruent", "Neutral", "Incongruent"])  # select trial type
        if trial_type == "Congruent":
            distractors_angle = stimulus_angle
        if trial_type == "Incongruent":
            if stimulus_angle == 0:
                distractors_angle = 180
            else:
                distractors_angle = 0
        if trial_type == "Neutral":
            distractors_angle = 90


        n.image("arrow-left.png", x=-5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
        n.image("arrow-left.png", x=-2.5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
        n.image("arrow-left.png", x=0, size=2, cache=cache, rotate=stimulus_angle)  # Target
        n.image("arrow-left.png", x=2.5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
        n.image("arrow-left.png", x=5, size=2, cache=cache, rotate=distractors_angle)  # Distractor
        n.refresh()
        response, RT = n.response(time_max=1000)  # Wait until 1 s and collect the response and its time


        # Response check
        if (response == "LEFT" and stimulus_angle == 0) or (response == "RIGHT" and stimulus_angle == 180):
            response = 1
        else:
            response = 0

        # Store data by appending each item to its list
        data["Trial"].append(trial)
        data["Trial_Type"].append(trial_type)
        data["Stimulus_Orientation"].append(stimulus_angle)
        data["RT"].append(RT)
        data["Response"].append(response)

    # Data saving
    df = pd.DataFrame.from_dict(data)  # Transform the data dictionary into a proper and savable dataframe
    df.to_csv("data.csv")  # Save it

    # Quick analysis
    mean_cong = df[(df["Trial_Type"]=="Congruent") & (df["Response"]==1)]["RT"].mean()
    mean_neu = df[(df["Trial_Type"]=="Neutral") & (df["Response"]==1)]["RT"].mean()
    mean_incong = df[(df["Trial_Type"]=="Incongruent") & (df["Response"]==1)]["RT"].mean()
    print("Mean RT Congruent: " + str(round(mean_cong, 2)))  # Print the mean of congruent
    print("Mean RT Neutral: " + str(round(mean_neu, 2)))  # Print the mean of neutral
    print("Mean RT Incongruent: " + str(round(mean_incong, 2)))  # Print the mean of incongruent

    n.close()  # Close neuropsydia
    
.. hint:: Try to run this task!

   - Can you count the number of errors?
   - Can you ask for the participant name at the beginning, and save data using it?