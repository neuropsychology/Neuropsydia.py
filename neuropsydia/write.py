# -*- coding: utf-8 -*-
from .path import *
from .core import *

from .core import color as core_color  # avoid conflict with arg name


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def write(text="Write something here", style="body", x=0, y=0, size=1.0, rotate=0, color="black", background=None, outline=False, outline_size=0.1, outline_color="black", allow=None, wait=None, long_text=False, characters='latin', fast=False):
    """
    Display some text on screen.

    Parameters
    -------------
    text : str
        The text to display.
    style : str
        'body', 'psychometry', 'psychometry_bold', 'light', 'bold', 'title', 'subtitle' or 'end'. Can overwrite other parameters such as position, size or allow. You can also insert the name of a system font, or the path to a specific font.
    x : float
        Horizontal position of the center (from -10 (left) to 10 (right)).
    y : float
        Vertical position of the center (from -10 (bottom) to 10 (top)).
    size : float
        Text size.
    rotate : int
        Rotation angle (0 to 360).
    color : str or tuple
        Text color. See `neuropsydia.color()`.
    background : str
        Background color. See `neuropsydia.color()`.
    outline : bool
        Text outline (unperfect for now, as the outline is larger for horizontal than for vertical lines).
    outline_size : float
        Outline size.
    outline_color : str or tuple
        Outline color. See `neuropsydia.color()`.
    allow : str or list
        Wait until a specific key is pressed (e.g., 'ENTER', ['LEFT', 'RIGHT'] or 'any').
    wait : float
        Wait time (in milliseconds).
    long_text : bool
        Set to True for longer texts on multiple lines. Then, the x and y parameters are not working, but you can jump lines using 'backslash + n' in your text. Some parameters are disabled. Unperfect for now.
    characters : str
        'latin' or 'cjk'. To change if you need to  cover Simplified Chinese, Traditional Chinese, Japanese, and Korean. 
    fast : bool
        Disables some parameters for improved speed.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.write('here is my title', style='title')
    >>> n.write('here is my text', font_color='red')
    >>> n.write('press ENTER to quit', style='end')
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)
    - Léo Dutriaux (https://github.com/LeoDutriaux)

    *Dependencies*

    - pygame
    """
    if fast is True:
        size = int(size*screen_width/35.0)
        x, y = Coordinates.to_pygame(x=x, y=y)
        if style != 'body':
            font = Font.get(style, size)
        elif non_latin is False:
            font = Font.get('RobotoRegular.ttf', size)
        else:
            font = Font.get('NotoSansCJKtc-Regular.otf', size)
        surface = font.render(text, True, core_color(color))
        rectangle = surface.get_rect()
        rectangle.center = (x, y)
        screen.blit(surface, rectangle)

    else:
        size = int(size*screen_width/35.0)
        outline_size = int(outline_size*screen_width/35.0)
        text = str(text)
        if characters == 'cjk':
            if style == 'body':
                font_name = Path.font() + 'NotoSansCJKtc-Regular.otf'
            elif style == 'psychometry':
                font_name = Path.font() + 'LiberationMono-Regular.ttf'
            elif style == 'psychometry_bold':
                font_name = Path.font() + 'LiberationMono-Bold.ttf'
            elif style == 'light':
                font_name = Path.font() + 'NotoSansCJKtc-Light.otf'
            elif style == 'bold':
                font_name = Path.font() + 'NotoSansCJKtc-Bold.otf'
            elif style == 'title':
                if size == int(1.0*screen_width/35.0):
                    size = int(2.0*screen_width/35.0)
                font_name = Path.font() + 'NotoSansCJKtc-Black.otf'
                if y == 0:
                    y = 8.5
                if background==None:
                    background="white"
            elif style == 'subtitle':
                if size == int(1.0*screen_width/35.0):
                    size = int(1.5*screen_width/35.0)
                font_name = Path.font() + 'NotoSansCJKtc-Bold.otf'
                if y == 0:
                    y=7
            elif style == 'end':
                font_name = Path.font() + 'NotoSansCJKtc-Bold.otf'
                if y == 0:
                    y = -9
                if allow==None:
                    allow="ENTER"
            else:
                font_name = style      
        
        else:
            if style == 'body':
                font_name = Path.font() + 'RobotoRegular.ttf'
            elif style == 'psychometry':
                font_name = Path.font() + 'LiberationMono-Regular.ttf'
            elif style == 'psychometry_bold':
                font_name = Path.font() + 'LiberationMono-Bold.ttf'
            elif style == 'light':
                font_name = Path.font() + 'RobotoLight.ttf'
            elif style == 'bold':
                font_name = Path.font() + 'RobotoBold.ttf'
            elif style == 'title':
                if size == int(1.0*screen_width/35.0):
                    size = int(2.0*screen_width/35.0)
                font_name = Path.font() + 'RobotoBlack.ttf'
                if y == 0:
                    y = 8.5
                if background==None:
                    background="white"
            elif style == 'subtitle':
                if size == int(1.0*screen_width/35.0):
                    size = int(1.5*screen_width/35.0)
                font_name = Path.font() + 'RobotoBold.ttf'
                if y == 0:
                    y=7
            elif style == 'end':
                font_name = Path.font() + 'RobotoBold.ttf'
                if y == 0:
                    y = -9
                if allow==None:
                    allow="ENTER"
            else:
                font_name = style
                
        
                
        font = Font.get(font_name,size)
        if outline==True:
            font_outline = Font.get(font_name, size+outline_size)

        #If NOT long text
        if long_text is False:
            x, y = Coordinates.to_pygame(x=x,y=y)
            if outline is True:
                surface = font_outline.render(text, True, core_color(outline_color))
                if rotate != None or rotate != 0:
                    surface = pygame.transform.rotate(surface,rotate)
                rectangle = surface.get_rect()
                rectangle.center = (x,y)
                newpage(background, auto_refresh=False)
                screen.blit(surface, rectangle)
            surface = font.render(text, True, core_color(color))
            if rotate != None or rotate != 0:
                surface = pygame.transform.rotate(surface,rotate)
            rectangle = surface.get_rect()
            rectangle.center = (x,y)
            newpage(background, auto_refresh=False)
            screen.blit(surface, rectangle)



        #If long text
        if long_text is True:
            paragraph = ''
            line = 0
            for i in range(len(text)):
                if i == (len(text) - 1):
                    paragraph = paragraph + text[i]
                    surface = font.render(paragraph, 1, core_color(color))
                    rectangle = surface.get_rect()
                    rectangle.center = (screen_width/2, (surface.get_height()/2)+(line*surface.get_height()))
                    screen.blit(surface, rectangle)

                elif text[i] == '\n':
                    surface = font.render(paragraph, 1, core_color(color))
                    rectangle = surface.get_rect()
                    rectangle.center = (screen_width/2, (surface.get_height()/2)+(line*surface.get_height()))
                    screen.blit(surface, rectangle)
                    paragraph = ""
                    line += 1

                else:
                    paragraph = paragraph + text[i]
                    if text[i] == " ":
                        buffer = paragraph
                        for x in range (len(text)-i-1):
                            if text[i+x+1] == '\n' or text[i+x+1]== " ":
                                break
                            else:
                                buffer = buffer+text[i+x+1]
                        surface_buffer = font.render(buffer, 1, core_color(color))
                        rectangle = surface_buffer.get_rect()
                        if surface_buffer.get_width()+screen_width/4>screen_width:
                            surface = font.render(paragraph, 1, core_color(color))
                            rectangle = surface.get_rect()
                            rectangle.center = (screen_width/2, (surface.get_height()/2)+(line*surface.get_height()))
                            screen.blit(surface, rectangle)
                            paragraph = ""
                            line += 1





        #END : In case we must wait until something
        if allow != None or wait != None:
            refresh()
            if allow == None and wait != None:
                time.wait(wait)
                return(wait)
            if allow != None:
                return(response(allow=allow,time_max=wait))
