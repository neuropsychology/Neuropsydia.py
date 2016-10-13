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
def write(text="Write something here", style="body", x=0, y=0, size=1.0,
          rotate=0, color="black", background_color=None,
          outline=False, outline_size=0.1, outline_color="black",
          allow=None, wait=None, long_text=False, fast=False):
    """
    Display some text on screen.

    Parameters
    ----------
    text = str, optional
        The text to display
    style = str, optional
        "body", "psychometry", "psychometry_bold", "light", "bold", "title", "subtitle" or "end". Can overwrite other parameters such as position, size or allow. You can also insert the name of a system font, or a path to a specific font you want to use
    x = float, optional
        position on x axis (from -10 (left) to 10 (right))
    y = float, optional
        position on y axis (from -10 (down) to 10 (up))
    size = float, optional
        text size
    rotate = int, optional
        angle (0 to 360) by which rotate the text
    color = str or tuple, optional
        color of the text. See color() function.
    background_color = str or tuple, optional
        color of the background. See color() function. Default to None
    outline = bool, optional [this parameter needs your help]
        outline the text (not perfect for now, the outline is larger for horizontal than for vertical lines)
    outline_size = float, optional
        the size of the outlining
    outline_color = str or tuple
        color of  the outlining. See color() function
    allow = str, optional
        wait until a specific key is pressed (e.g., "ENTER", or "any" for any). Default to None
    long_text = bool, optional [this parameter needs your help]
        set to True if you want to write a longer text on multiple lines. Then, the x and y parameters are not working, but you can jump lines using  "\n" in your text (e.g., "\n\n\n here's my long text\n do you like it?"). Some other parameters are not compatible.
    fast = some parameters are toggled off, but faster.

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.write("here's my  title", style = "title")
    >>> n.write("here's my  text", font_color = "red")
    >>> n.write("press ENTER to quit", style = "end")
    >>> n.close()

    Authors
    ----------
    Léo Dutriaux, Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    - time
    """
    if fast is True:
        size = int(size*screen_width/35.0)
        x, y = Coordinates.to_pygame(x=x, y=y)
        if style != 'body':
            font = Font.get(style, size)
        else:
            font = Font.get('RobotoRegular.ttf', size)
        surface = font.render(text, True, core_color(color))
        rectangle = surface.get_rect()
        rectangle.center = (x, y)
        screen.blit(surface, rectangle)

    else:
        size = int(size*screen_width/35.0)
        outline_size = int(outline_size*screen_width/35.0)
        text = str(text)

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
            if background_color==None:
                background_color="white"
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
                newpage(background_color, auto_refresh=False)
                screen.blit(surface, rectangle)
            surface = font.render(text, True, core_color(color))
            if rotate != None or rotate != 0:
                surface = pygame.transform.rotate(surface,rotate)
            rectangle = surface.get_rect()
            rectangle.center = (x,y)
            newpage(background_color, auto_refresh=False)
            screen.blit(surface, rectangle)



        #If long text
        if long_text is True:
            paragraph = ''
            line = 0
            for i in range(len(text)):
                if i == (len(text) - 1):
                    paragraph = paragraph + text[i]
                    surface = font.render(paragraph, 1, (0, 0, 0))
                    rectangle = surface.get_rect()
                    rectangle.center = (screen_width/2, (surface.get_height()/2)+(line*surface.get_height()))
                    screen.blit(surface, rectangle)

                elif text[i] == '\n':
                    surface = font.render(paragraph, 1, (0, 0, 0))
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
                        surface_buffer = font.render(buffer, 1, (0, 0, 0))
                        rectangle = surface_buffer.get_rect()
                        if surface_buffer.get_width()+screen_width/4>screen_width:
                            surface = font.render(paragraph, 1, (0, 0, 0))
                            rectangle = surface.get_rect()
                            rectangle.center = (screen_width/2, (surface.get_height()/2)+(line*surface.get_height()))
                            screen.blit(surface, rectangle)
                            paragraph = ""
                            line += 1





        #END : In case or one must wait until something
        if allow != None or wait != None:
            refresh()
            if allow == None and wait != None:
                time.wait(wait)
                return(wait)
            if allow != None:
                return(response(allow=allow,time_max=wait))
