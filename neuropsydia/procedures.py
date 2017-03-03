# -*- coding: utf-8 -*-
"""
Procedures submodule
"""
from .core import *
from .scale import *
from .write import *
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def resting_state_brief_assessment(data=None, language="fr", test=""):
    """
    Standardized Resting State Assessment Procedure.

    Parameters
    ----------
    data = dict
        A dict where to store the data. If None, a new one will be created.

    Returns
    ----------
    None

    Example
    ----------
    None

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    # Defining the template of the scale
    def fancy_scale(style, y, title):
        result = scale(style=style, y=y, title=title, title_size=0.6, title_space=1, show_result=True, show_result_space=1, show_result_size=0.35, show_result_shape_size=0.55, show_result_decimals=0)
        return(result)

    # Checking if data is not empty
    if data is None:
        data = {}

    if language == "fr":
        # New blank page
        newpage()
        write("Estimez le pourcentage de temps que vous avez passé dans les 6 états suivants :", y=9.2, size=0.75)

        data[test + "Drowsiness"] = fancy_scale(style="purple", y=7, title="Je me sentais somnolant.")
        data[test + "Absorption_External"] = fancy_scale(style="blue", y=4, title="Mes pensées étaient dirigées sur ce qu'il se passait autour de moi (bruits, voix...).")
        data[test + "Absorption_Internal"] = fancy_scale(style="green", y=1, title="Mes pensées étaient dirigées sur des évenements que j'imaginais ou dont je me rappelais.")
        data[test + "Absorption_Body"] = fancy_scale(style="yellow", y=-2, title="Mes pensées étaient dirigées sur ce qu'il se passait dans mon corps (sensations physiques, respiration, coeur...).")
        data[test + "Mind_Wandering"] = fancy_scale(style="orange", y=-5, title="Mes pensées s'enchainaient librement, sans contrôle.")
        data[test + "Mind_Focus"] = fancy_scale(style="red", y=-8, title="J'étais concentré sur une idée, une sensation ou une perception en particulier.")

    return(data)