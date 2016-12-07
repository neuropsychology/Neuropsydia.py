# -*- coding: utf-8 -*-
"""
Module for the ask() function.
"""
from .path import *
from .core import *
from .write import *

from .core import color as core_color #avoid conflict with arg name



#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # --- ask ---
#version : 1.0
#display a question and get the subject's answer
#Authors : Léo Dutriaux, Dominique Makowski
#==============================================================================
#======================================================================== ======
#==============================================================================
#==============================================================================
def ask(text="Write something here:", style='light', x=-8, y=0, order=None, size=1.0, color="black", background="white", hide=False, detach_question=False, question_style="light", question_x=0, question_y=0, question_size=1, question_color="black", question_long_text=False, allow=None, allow_length=None, allow_type=None, allow_max=None, allow_NA=True):
    """
    Display a question and get the subject's answer.

    Parameters
    ----------
    text = str, optional
        the question to be displayed
    style = str, optional
        "body", "light" or "bold"
    order = int, optional
        for series of questions, sometimes it's easier to just specify the order (1, 2 , 3, ...) and the quetsions will appear one under the other
    x = float, optional
        position on x axis (from -10 (left) to 10 (right))
    y = float, optional
        position on y axis (from -10 (down) to 10 (up))
    size = float, optional
        text size
    color = str or tuple, optional
        color of the text. See color() function.
    background = str or tuple, optional
        color of the background. See color() function. Default to None
    hide = bool, optional
        display "****" (stars) instead of the actual answer
    detach_question = bool, optional
        if set to true, then the question can be manipulated separately using the parameters below
    - question_style = see style arg in write()
    - question_x = see x arg in write()
    - question_y = see y arg in write()
    - question_size = see size arg in write()
    - question_color = see color arg in write()
    - question_long_text = see long_text arg in write()
    allow = list, optional
        only allow specific answers (e.g., "yes" or "no")
    allow_length = int, optional
        allow only a specific answer length
    allow_type = str, optional
        "str", "int" or "float", allow only this specific type
    allow_max = int, optional
        when numeric answer, set a maximum

    Returns
    ----------
    str
        answer

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> response = n.ask("Hey, you're good?")
    >>> print(response)
    >>> n.close()

    Authors
    ----------
    Léo Dutriaux, Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    if detach_question is not False:
        write(text, style=question_style, x=question_x, y=question_y, size=question_size, color=question_color, long_text=question_long_text)
        text_new = ''
    else:
        text_new = text + " "

    # Convert size to pygame compatible size
    size = int(size*screen_width/35.0)

    # Get fonts
    if style is 'body':
        font = Font.get(Path.font() + 'RobotoRegular.ttf', size)
    elif style is 'light':
        font = Font.get(Path.font() + 'RobotoLight.ttf', size)
    elif style is 'bold':
        font = Font.get(Path.font() + 'RobotoBold.ttf', size)
    else:
        font = Font.get(style, size)

    # Adjust y position depending on order
    if order is not None:
        y = 5 - (order*1.25)


    # Convert coordinates to pygame compatible coordinates
    x, y = Coordinates.to_pygame(x=x, y=y)


    user_input = ''
    loop = True
    while loop is True:
        surface = font.render(text_new, 1, core_color(color))
        size = surface.get_size()
        pygame.draw.rect(screen, core_color(background), (x,y,size[0],size[1]))
        screen.blit(surface, (x,y))
        pygame.display.flip()

        # wait for user input
        answer = response(get_RT=False)

        if answer is "SPACE":
            answer = "_"
        if answer is not "ENTER":
            if answer is "ESCAPE":
                break
            if answer is pygame.K_BACKSPACE:
                if user_input != '':
                    user_input = user_input[:len(user_input)-1]
                    text_new = text_new[:len(text_new)-1]
                    pygame.draw.rect(screen, core_color(background), (x,y,size[0],size[1]))
            else:
                user_input = user_input + str(answer)
                if hide is True:
                    text_new = text_new + "*"
                else:
                    text_new = text_new + str(answer)
        else:
            if user_input is '':
                user_input = "NA"
                if allow_NA is True:
                    return(user_input)
            elif allow is not None or allow_length is not None or allow_type is not None:
                warning = 0
                if allow is not None and user_input not in list(allow):
                    warning_text = text_new+'    incorrect (answer not allowed)'
                    warning = 1
                if isinstance(allow_length, int) and len(user_input) != allow_length:
                    warning_text = text_new+'    incorrect (' +str(allow_length)+ ' characters required)'
                    warning = 1
                if allow_max is not None and float(user_input) > float(allow_max):
                    warning_text = text_new+'    incorrect (max = ' + str(allow_max) + ')'
                    warning = 1
                    allow_type = "in"
                if allow_type is not None:
                    if allow_type is "int":
                        try:
                            user_input = int(user_input)
                        except ValueError:
                            warning_text = text_new + '    incorrect (wrong type)'
                            warning = 1
                    if allow_type is "float":
                        try:
                            user_input = float(user_input)
                        except ValueError:
                            warning_text = text_new + '    incorrect (wrong type)'
                            warning = 1

                if warning == 1:
                    surface = font.render(warning_text, 1, core_color(color))
                    size = surface.get_size()
                    pygame.draw.rect(screen,  core_color(background), (x,y,size[0],size[1]))
                    screen.blit(surface, (x,y))
                    refresh()
                    time.wait(700)
                    pygame.draw.rect(screen,  core_color(background), (x,y,size[0],size[1]))
                    refresh()
                else:
                    return(user_input)
            else:
                return(user_input)





