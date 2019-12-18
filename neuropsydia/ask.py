# -*- coding: utf-8 -*-
"""
Submodule for the ask() function.
"""
from .path import *
from .core import *
from .write import *

from .core import color as core_color #avoid conflict with arg name



#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#======================================================================== ======
#==============================================================================
#==============================================================================
def ask(text="Write something here:", style='light', x=-8, y=0, order=None, size=1.0, color="black", characters='latin', background="white", hide=False, detach_question=False, question_style="light", question_x=0, question_y=0, question_size=1, question_color="black", question_long_text=False, allow=None, allow_length=None, allow_type=None, allow_max=None, allow_NA=True):
    """
    Display a question and get the subject's answer.

    Parameters
    ------------
    text : str
        The question to be displayed.
    style : str
        "body", "light" or "bold".
    order : int
        For series of questions, it's sometimes easier to just specify the order (1, 2 , 3, ...) and the quetsions will appear one under the other.
    x : float
        Horizontal position (from -10 (left) to 10 (right)).
    y : float
        Vertical position of the center (from -10 (bottom) to 10 (top)).
    size : float
        Text size.
    color : str or tuple
        Text color. See `neuropsydia.color()`.
    characters : str
        'latin' or 'cjk'. 'cjk'  cover Simplified Chinese, Traditional Chinese, Japanese, and Korean.
    background : str or tuple
        Background color. See `neuropsydia.color()`.
    hide : bool
        Display "****" (stars) instead of the actual answer.
    detach_question : bool
        If set to true, then the question can be manipulated separately using the parameters below.
    question_style : str
        'body', 'psychometry', 'psychometry_bold', 'light', 'bold', 'title', 'subtitle' or 'end'. Can overwrite other parameters such as position, size or allow. You can also insert the name of a system font, or the path to a specific font.
    question_x : float
        Horizontal position of the question (from -10 (left) to 10 (right)).
    question_y : float
        Vertical position of the question (from -10 (bottom) to 10 (top)).
    question_size : float
        Question size.
    question_color : str
        Question color. See `neuropsydia.color()`.
    question_long_text : bool
        et to True for longer texts on multiple lines. Then, the x and y parameters are not working, but you can jump lines using 'backslash + n' in your text. Some parameters are disabled. Unperfect for now.
    allow : list
        Allow only specific answers (e.g., ["yes", "no"]).
    allow_length : int
        Allow only a specific answer length.
    allow_type : str
        "str", "int" or "float". Allow only a specific type.
    allow_max : int
        When allow_type is int or float, set a maximum.
    allow_NA : bool
        Allow absence of response.

    Returns
    ----------
    answer : str
        Input.

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> answer = n.ask("Hey, you're good?")
    >>> print(answer)
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)
    - Léo Dutriaux (https://github.com/LeoDutriaux)

    *Dependencies*

    - pygame
    """
    if detach_question is not False:
        write(text, style=question_style, x=question_x, y=question_y, size=question_size, color=question_color, characters=characters, long_text=question_long_text)
        text_new = ''
    else:
        text_new = text + " "

    # Convert size to pygame compatible size
    size = int(size*screen_width/35.0)

    # Get fonts
    if characters == 'cjk':
        if style is 'body':
            font = Font.get(Path.font() + 'NotoSansCJKtc-Regular.otf', size)
        elif style is 'light':
            font = Font.get(Path.font() + 'NotoSansCJKtc-Light.otf', size)
        elif style is 'bold':
            font = Font.get(Path.font() + 'NotoSansCJKtc-Bold.otf', size)
        else:
            font = Font.get(style, size)
    else:
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
                if allow_NA is True:
                    return("NA")
                else:
                    user_input = ''
                    warning_text = text_new+'    incorrect (input required)'
                    warning = 1
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
                else:
                    user_input = ''
                    warning_text = text_new+'    incorrect (input required)'
                    warning = 1
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
                    allow_type = "int"
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





