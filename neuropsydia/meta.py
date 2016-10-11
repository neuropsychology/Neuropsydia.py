# -*- coding: utf-8 -*-
import pandas as pd
import datetime

from .path import *
from .core import *
from .write import *
from .image import *
from .start import *
from .scale import *
from .ask import *

from .core import background_color as core_background_color  # avoid conflict with arg name


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def instructions(text, background_color='white', color="black", size=1.0,
                 title=None, replace_title=False, end_text="Appuyez sur ENTRER pour commencer."):
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
    - time
    """
    core_background_color(background_color)
    if replace_title == False:
        write("INSTRUCTIONS", style="title", color=color)
        if title != None:
            write(title, style="subtitle", color=color)
    if replace_title != False and title != None:
        write(title, style="title", color=color)

    write('\n\n\n\n\n'+text, size=size, color=color, long_text=True)
    write(end_text, style='end', color=color)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def questionnaire(questions_dictionary, questions_list_key_name='Item', background_color='white', size=1, show_page_number=True,  randomize=False, reverse=False, results_save=False, results_type="csv", results_name="questionnaire_results", results_path="", dimensions_mean=False, dimensions_key_name='Dimension', style='red', x=0, y=-3.3, anchors=None, anchors_space=2, anchors_size=0.7, edges=[0,100], validation=True, analog=True, step=1, labels="numeric", labels_size=0.8, labels_rotation=0, labels_space=-1, labels_x=0, line_thickness=4, line_length=8, line_color="black", title=None, title_style="body", title_size=1, title_space=2, point_center=False, point_edges=True, force_separation=False, separation_labels=None, separation_labels_size=1, separation_labels_rotate=0, separation_labels_space=-1, show_result=False, show_result_shape="circle", show_result_shape_fill_color="white", show_result_shape_line_color="red", show_result_shape_size=0.8, show_result_space=1.2, show_result_size=0.5, show_result_color="black"):
    """
    A wrapper function for easily creating questionnaires. You can go back or foth using the LEFT and RIGHT keyboard arrows.

    Parameters
    ----------
    questions_dictionary = dict
        needs an object of the following stucture:

        >>> questions_dictionary = {
        >>>     "Item": {
        >>>         1: "Is Neuropsydia great?",
        >>>         2: "Is Neuropsydia not great?",
        >>>         3: "Is Python great?",
        >>>         4: "Is Python not great?"
        >>>         }
        >>> }

    Returns
    ----------
    A pandas dataframe containing the data. See http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe for details.

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

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    - pandas 18.0
    - time
    """
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

    i = 0
    while i < n_questions:
        try:
            core_background_color(background_color)
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

            t0 = builtin_time.clock()
            answer = scale(style=style, anchors = anchors, anchors_space=anchors_space, anchors_size=anchors_size, edges = edges, validation=validation, analog=analog, step=step, labels=labels, labels_size=labels_size, labels_rotation=labels_rotation, labels_space=labels_space,labels_x=labels_x, line_thickness=line_thickness, line_length=line_length, line_color=line_color, background_color=background_color, title=title, title_style=title_style, title_size=title_size, title_space=title_space, reverse=reverse_question, point_center=point_center, point_edges=point_edges, force_separation=force_separation, separation_labels=separation_labels, separation_labels_size=separation_labels_size, separation_labels_rotate=separation_labels_rotate, separation_labels_space=separation_labels_space, show_result=show_result, show_result_shape=show_result_shape, show_result_shape_fill_color=show_result_shape_fill_color, show_result_shape_line_color=show_result_shape_line_color, show_result_shape_size=show_result_shape_size, show_result_space=show_result_space, show_result_size=show_result_size, show_result_color=show_result_color)
            RT = (builtin_time.clock()-t0 ) * 1000
            if answer == 'RIGHT':
                answer = "NA"
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

    if dimensions_mean == True:
        try:
            means_dict = dict(df.groupby(dimensions_key_name).mean()['Answer'])
            for dim in means_dict.keys():
                df[dim] = means_dict[dim]
        except:
            print("NEUROPSYDIA ERROR: questionnaire(): arg dimensions_key_name does not match.")

    if results_save == True:
        if results_type == "csv2":
            df.to_csv(results_path + results_name + '.csv', sep=';', index_label="Item_Number", na_rep='NA')
        else:
            df.to_csv(results_path + results_name + '.csv', sep=',', index_label="Item_Number", na_rep='NA')
    return(df)
