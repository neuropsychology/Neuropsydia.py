# -*- coding: utf-8 -*-
import neurokit as nk
import pandas as pd
import datetime
import random

from .path import *
from .core import *
from .write import *
from .image import *
from .start import *
from .scale import *
from .ask import *


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def instructions(text, background='white', color="black", size=1.0,
                 title="INSTRUCTIONS", title_color="black", subtitle=None, subtitle_color="black", end_text="Appuyez sur ENTRER pour commencer.", top_space=5):
    """
    Help incomplete, sorry.

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    newpage(background, auto_refresh=False)

    if title is not None:
        write(title, style="title", color=title_color)
    if subtitle is not None:
        write(subtitle, style="subtitle", color=subtitle_color)

    top_space = ["\n"]*top_space
    top_space = "".join(str(elem) for elem in top_space)
    write(top_space + text, size=size, color=color, long_text=True)
    write(end_text, style='end', color=color)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def questionnaire(questions_dictionary, questions_list_key_name='Item', background='white', size=1, show_page_number=True,  randomize=False, reverse=False, results_save=False, results_name="questionnaire_results", results_path="", participant_id="", dimensions_mean=False, dimensions_key_name='Dimension', style='red', x=0, y=-3.3, anchors=None, anchors_space=2, anchors_size=0.7, edges=[0,100], validation=True, analog=True, step=1, labels="numeric", labels_size=0.8, labels_rotation=0, labels_space=-1, labels_x=0, line_thickness=4, line_length=8, line_color="black", title=None, title_style="body", title_size=1, title_space=2, point_center=False, point_edges=True, force_separation=False, separation_labels=None, separation_labels_size=1, separation_labels_rotate=0, separation_labels_space=-1, show_result=False, show_result_shape="circle", show_result_shape_fill_color="white", show_result_shape_line_color="red", show_result_shape_size=0.8, show_result_space=1.2, show_result_size=0.5, show_result_color="black", instructions_text=None, instructions_top_space=5, show_result_decimals=1, cursor_size=1):
    """
    A wrapper function for easily creating questionnaires. You can go back and forth in the questions using the LEFT and RIGHT keyboard arrows.

    Parameters
    ----------
    questions_dictionary : dict
        A dict of the following stucture:

        >>> questions_dictionary = {
        >>>     "Item": {
        >>>         1: "Is Neuropsydia great?",
        >>>         2: "Is Neuropsydia not great?",
        >>>         3: "Is Python great?",
        >>>         4: "Is Python not great?"
        >>>         }
        >>> }

    questions_list_key_name : str
        Key name of the sub-dict containing the items.
    background : str
        Background color.
    size : int
        Question's size.
    show_page_number : bool
        Show page number.
    randomize : bool
        Randomize question presentation.
    reverse : bool
        Needs a "Reverse" sub-dict with booleans showing which questions are reversed.
    results_save : bool
        Save the results.
    results_name : str
        Filename.
    results_path : str
        Path where to save.
    participant_id : str
        Append the participant's name in the filename.
    dimensions_mean : bool
        Compute the mean by dimension. Needs a "Dimension" sub-dict.
    dimensions_key_name : str
        Key name of the sub-dict containing dimensions.
    style : str
        style, check `neuropsydia.scale_styles()` function to see what's available.
    x : float
        Horizontal position of the center (from -10 (left) to 10 (right)).
    y : float
        Vertical position of the center (from -10 (bottom) to 10 (top)).
    anchors : list of two str
        a list of two propositions to be displayed on the sides of the scale (e.g., [not at all, very much]).
    anchors_space : float
        spacing betweeen the edge and the anchors.
    anchors_size : float
        size of the anchors' font.
    edges : list
        the underlying numerical edges of the scale.
    validation : bool
        confirm the response with a second left click or withdraw with a right click.
    analog : bool
        continuous (discrete) scale.
    step : int
        if analog is True, what are the step to go between the edges (determine the number of points on the scale).
    labels : str or list
        "num", "numeric" or "numbers" or list of actual text labels (e.g., ["not at all", "a bit", "very much"]).
    labels_size : float
        Size of labels.
    labels_rotation : float
        Labels rotation angle.
    labels_space : float
        Space between scale and labels.
    labels_x : float
        Horizontal dodging position.
    line_thickness : float
        Scale line thickness.
    line_length : float
        Scale line length.
    line_color : str
        Scale line color.
    background : str
        Scale background color.
    title : str
        Scale title/question to ask.
    title_style : str
        'body', 'psychometry', 'psychometry_bold', 'light', 'bold'. You can also insert the name of a system font, or the path to a specific font.
    title_size : float
        Title size.
    title_space : float
        Space between scale and title.
    point_center : bool
        Place a point at the center.
    point_edges : bool
        Place points at the edges.
    reverse : bool
        The result is scored as inverse.
    force_separation : int
        Creates visual separations with points.
    separation_labels : list
        Place labels corresponding to the separations.
    separation_labels_size : float
        Separation labels size.
    separation_labels_rotate : float
        Separation labels rotation angle.
    separation_labels_space : float
        Space between scale and separation labels.
    show_result : bool
        Add a marker to show the value on scale.
    show_result_shape : str
        Shape of this marker. "circle" or "rectangle".
    show_result_shape_fill_color : str
        Fill color of the marker.
    show_result_shape_line_color : str
        Line color of the marker.
    show_result_shape_size : float
        Marker's shape size.
    show_result_space : float
        Space between scale and marker.
    show_result_size : float
        Results text size.
    show_result_color : str
        Results text color.
    show_result_decimals : int
        How many decimals to show.
    cursor_size : float
        Size of the circle cursor.

    Returns
    ----------
    df : pandas.DataFrame
        A pandas' dataframe containing the data.

    Example
    ----------
    >>> import neuropsydia as n
    >>> questions_dictionary = {
    >>>     "Item": {
    >>>         1: "Is Neuropsydia great?",
    >>>         2: "Is Neuropsydia not great?",
    >>>         3: "Is Python great?",
    >>>         4: "Is Python not great?"
    >>>     },
    >>>     "Reverse": {
    >>>         1: False,
    >>>         2: True,
    >>>         3: False,
    >>>         4: True
    >>>     },
    >>>     "Dimension": {
    >>>         1: "Neuropsydia",
    >>>         2: "Neuropsydia",
    >>>         3: "Python",
    >>>         4: "Python"
    >>>     }
    >>> }
    >>> n.start()
    >>> n.questionnaire(questions_dictionary, anchors=["No", "Yes"], results_save=True, dimensions_mean=True)
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    - pandas
    """
    time_start = datetime.datetime.now()
    if isinstance(questions_dictionary,dict) == False:
        print("NEUROPSYDIA ERROR: questionnaire(): wrong object given (not a dictionary), check http://www.neuropsydia.com/#!create-questionnaire/ncq23 for help.")
    try:
        questions = questions_dictionary[questions_list_key_name]
    except:
        print("NEUROPSYDIA ERROR: questionnaire(): arg questions_list_key_name does not match.")

    n_questions = len(questions)
    order = list(questions.keys())
    if randomize is True:
        random.shuffle(order)

    questions_dictionary["Answer"] = {}
    questions_dictionary["RT"] = {}
    questions_dictionary["Order"] = {}
    questions_dictionary["Time"] = {}

    if instructions_text != None:
        try:
            instructions(instructions_text, top_space=instructions_top_space)
        except:
            print("NEUROPSYDIA ERROR: questionnaire(): problem in 'instructions_text' arg, make sure it's a normal string.")



    i = 0
    while i < n_questions:
        try:
            newpage(background, auto_refresh=False)
            time.wait(30)
            if show_page_number is True:
                write('Question n°' + str(i+1) + '/' + str(n_questions), style="light", y=9)
            text = questions_dictionary[questions_list_key_name][order[i]]
            write('\n\n\n\n\n\n'+text, long_text=True, size=size)
            try:
                reverse_question = questions_dictionary['Reverse'][order[i]]
            except:
                if isinstance(reverse,list) is True:
                    reverse_question=reverse[i]
                else:
                    reverse_question=reverse

            try:
                if isinstance(questions_dictionary["Anchors"], dict):
                    anchors = questions_dictionary['Anchors'][order[i]]
            except:
                pass

            t0 = builtin_time.clock()
            answer = scale(style=style, anchors=anchors, anchors_space=anchors_space, anchors_size=anchors_size, edges = edges, validation=validation, analog=analog, step=step, labels=labels, labels_size=labels_size, labels_rotation=labels_rotation, labels_space=labels_space,labels_x=labels_x, line_thickness=line_thickness, line_length=line_length, line_color=line_color, background=background, title=title, title_style=title_style, title_size=title_size, title_space=title_space, reverse=reverse_question, point_center=point_center, point_edges=point_edges, force_separation=force_separation, separation_labels=separation_labels, separation_labels_size=separation_labels_size, separation_labels_rotate=separation_labels_rotate, separation_labels_space=separation_labels_space, show_result=show_result, show_result_shape=show_result_shape, show_result_shape_fill_color=show_result_shape_fill_color, show_result_shape_line_color=show_result_shape_line_color, show_result_shape_size=show_result_shape_size, show_result_space=show_result_space, show_result_size=show_result_size, show_result_color=show_result_color, show_result_decimals=show_result_decimals, cursor_size=cursor_size)
            RT = (builtin_time.clock()-t0 ) * 1000
            if answer == 'RIGHT':
                answer = np.nan
            questions_dictionary["Answer"][order[i]] = answer
            questions_dictionary["RT"][order[i]] = RT
            questions_dictionary["Order"][order[i]] = i+1
            questions_dictionary["Time"][order[i]] = datetime.datetime.now()
            if answer == 'LEFT':
                i -= 1
            else:
                i += 1
        except:
           print("NEUROPSYDIA ERROR: questionnaire(): someting went wrong (error number 2)")

    df = pd.DataFrame.from_dict(questions_dictionary)
    df["Time_Start"] = time_start
    df["Time_End"] = datetime.datetime.now()
    df["Total_Duration"] = (datetime.datetime.now()-time_start).total_seconds()

    if dimensions_mean == True:
        for dim in set(df[dimensions_key_name]):
            df[dim] = df[(df[dimensions_key_name]==dim)]["Answer"].mean()

    if results_save == True:
        nk.save_data(df, filename=results_name, path=results_path, participant_id=participant_id, index=True, index_label="Item_Number")

    return(df)
