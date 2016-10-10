# -*- coding: utf-8 -*-
import neuropsydia as n  # Load neuropsydia
import random  # import the random module

n.start()  # Start neuropsydia
n.instructions("Goal: hit SPACE whenever a GREEN circle appears. \nWhen it is RED, don't press anything.")  # Display instructions and break line with \n
n.background_color("grey")  # Fill the screen
n.countdown()  # Display countdown

for trial in range(10):  # Iterate over the number of trials
    stimulus = random.choice(["green", "red"])  # Select a stimulus type
    ISI = random.randrange(start=500, stop=5000, step=500)  # Select the inter-stimuli interval (ISI)

    n.background_color("grey")  # Fill the screen
    n.write("+")  # Fixation cross
    n.refresh()  # Diplay it on screen
    n.time.wait(ISI)  # Wait

    n.circle(size=5, fill_color=stimulus)  # Display the stimulus (filled with the proper color)
    n.refresh()  # Diplay it on screen
    response, RT = n.response(time_max=4000)  # Wait for response until 4 s and collect the input and the response time
    print(response, RT)
n.close()
