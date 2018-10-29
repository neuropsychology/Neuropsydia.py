# -*- coding: utf-8 -*-
import pygame
import webbrowser

from pygame import gfxdraw
import numpy as np

from .core import *
from .write import *
from .image import *




# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def line(left_x=-5, left_y=0, right_x=5, right_y=0, line_color="black", thickness=1):
    """
    Draw a line.

    Parameters
    ----------
    left_x : float
        Left end horizontal position.
    left_y : float
        Left end vertical position.
    right_x : float
        Right end horizontal position.
    right_y : float
        Right end vertical position.
    line_color : str
        Line color.
    thickness : float
        Line thickness.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.line()
    >>> n.close()


    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    - pygame.gfxfraw
    """
    left_x_pygame = Coordinates.to_pygame(x = left_x)
    left_y_pygame = Coordinates.to_pygame(y = left_y)
    right_x_pygame = Coordinates.to_pygame(x = right_x)
    right_y_pygame = Coordinates.to_pygame(y = right_y)

    if left_x == right_x or left_y == right_y:
        pygame.draw.line(screen, color(line_color), (left_x_pygame, left_y_pygame), (right_x_pygame, right_y_pygame), thickness)
    else:
        if thickness == 1:
            pygame.draw.aaline(screen, color(line_color), (left_x_pygame, left_y_pygame), (right_x_pygame,right_y_pygame), thickness)
        else:
            pygame.draw.line(screen, color(line_color), (left_x_pygame, left_y_pygame), (right_x_pygame, right_y_pygame), thickness)

            # Failed Attempt to have a antialiased line
#            X0 = np.array([left_x, left_y])
#            X1 =  np.array([right_x, right_y])
#
#            center_L1 = (X0 + X1) / 2
#
#            length = 10 # Line size
#            thickness = 2
#            angle = math.atan2(X0[1] - X1[1], X0[0] - X1[0])
#
#            UL = (center_L1[0] + (length / 2.) * np.cos(angle) - (thickness / 2.) * np.sin(angle), center_L1[1] + (thickness / 2.) * np.cos(angle) + (length / 2.) * np.sin(angle))
#            UR = (center_L1[0] - (length / 2.) * np.cos(angle) - (thickness / 2.) * np.sin(angle), center_L1[1] + (thickness / 2.) * np.cos(angle) - (length / 2.) * np.sin(angle))
#            BL = (center_L1[0] + (length / 2.) * np.cos(angle) + (thickness / 2.) * np.sin(angle), center_L1[1] - (thickness / 2.) * np.cos(angle) + (length / 2.) * np.sin(angle))
#            BR = (center_L1[0] - (length / 2.) * np.cos(angle) + (thickness / 2.) * np.sin(angle), center_L1[1] - (thickness / 2.) * np.cos(angle) - (length / 2.) * np.sin(angle))
#
#            UL = Coordinates.to_pygame(x = UL[0], y=UL[1])
#            UR = Coordinates.to_pygame(x = UR[0], y=UR[1])
#            BL = Coordinates.to_pygame(x = BL[0], y=BL[1])
#            BR = Coordinates.to_pygame(x = BR[0], y=BR[1])
#
#            pygame.gfxdraw.aapolygon(screen, (UL, UR, BR, BL), color(line_color))
#            pygame.gfxdraw.filled_polygon(screen, (UL, UR, BR, BL), color(line_color))

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def rectangle(x=0, y=0, width=10, height=10, line_color="black", thickness=1, fill_color=None, rotate=0):
    """
    Draw a rectangle.

    Parameters
    ----------
    x : float
        Center's horizontal position.
    y : float
        Center's vertical position.
    width : float
        Rectangle's width.
    height : float
        Rectangle's height.
    line_color : str
        Rectangle's edges color.
    thickness : float
        Rectangle's edges thickness.
    fill_color : str
        Rectangle's fill color.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.rectangle()
    >>> n.close()


    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    - pygame.gfxfraw
    """



    left = Coordinates.to_pygame(x= (x - width / 2))
    top = Coordinates.to_pygame(y= (y + height /2))
    width = Coordinates.to_pygame(distance_x = width)
    height = Coordinates.to_pygame(distance_y = -height)

    if rotate != 0:
        print("Rotation not working... sorry")
#        def points_to_angle(x, y):
#            x = (x[0]-screen_width/2, -1*(x[1]-screen_height/2))
#            y = (y[0]-screen_width/2, -1*(y[1]-screen_height/2))
#
#            dx = x[1] - x[0]
#            dy = y[1] - y[0]
#            rads = np.arctan2(-dy,dx)
#            rads = 2*np.pi % rads
#            degs = np.degrees(rads)
#            return(degs)
#
#
##    def angle_to_points(degs):
##        rads = np.radians(degs)
##        return(x, y)
#
##        Works only for squares
#        rotate = (rotate/100)*width
#        topleft_point = (left+rotate, top)
#        topright_point = (left+width, top+rotate)
#        bottomleft_point = (left, top+height-rotate)
#        bottomright_point = (left+width-rotate, top+height)
#
#        print(points_to_angle(topleft_point, topright_point))
#
#        pygame.draw.polygon(screen, color(line_color), [topleft_point, bottomleft_point, bottomright_point, topright_point], thickness)

#    else:
    if fill_color != None:
        pygame.draw.rect(screen, color(fill_color),(left,top,width,height), 0)
    if thickness != 0:
        pygame.draw.rect(screen, color(line_color),(left,top,width,height), thickness)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def circle(x=0, y=0, size=10, line_color="black", thickness=0, fill_color="white"):
    """
    Draw a circle.

    Parameters
    ----------
    x : float
        Center's horizontal position.
    y : float
        Center's vertical position.
    size : float
        Diameter.
    line_color : str
        Circle's edges color.
    thickness : float
        Circle's edges thickness.
    fill_color : str
        Circle's fill color.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.circle()
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    - pygame.gfxfraw
    """
    x = Coordinates.to_pygame(x=x)
    y = Coordinates.to_pygame(y=y)
    radius = Coordinates.to_pygame(distance_x = size/2)
    thickness_radius = Coordinates.to_pygame(distance_x = (size-thickness)/2)

    if fill_color == None:
        pygame.gfxdraw.aacircle(screen, x, y, radius, color(line_color))
    else:
        if thickness == None:
            pygame.gfxdraw.filled_circle(screen, x, y, radius, color(fill_color))
        elif thickness == 0:
            pygame.gfxdraw.filled_circle(screen, x, y, radius, color(fill_color))
            pygame.gfxdraw.aacircle(screen, x, y, radius, color(line_color))
        else:
            pygame.gfxdraw.filled_circle(screen, x, y, radius, color(line_color))
            pygame.gfxdraw.aacircle(screen, x, y, radius, color(line_color))
            pygame.gfxdraw.filled_circle(screen, x, y, thickness_radius, color(fill_color))#
            pygame.gfxdraw.aacircle(screen, x, y, thickness_radius, color(fill_color))


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def countdown(style="circle", duration=3000, width=5, reverse=False, background="white", write_seconds=True, write_color="white", write_outline="black", color_fade=False, color_start="red", color_end="green", sound=False, melody=[1000, 1500]):
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
    - pygame.gfxfraw
    - time
    - winsound
    """
    if sound is True:
        import winsound

    original_width=width
    duration_frames = int(duration/(1000/60))


    if reverse == False:
        width=0.6
        width_per_frame = (original_width-width)/duration_frames
    else:
        width_per_frame = original_width/duration_frames


    t0 = builtin_time.clock()
    red, green, blue = color(color_start)



    for i in range(duration_frames):
        time.control(60)
        fill_color = tuple([red,green,blue])
        if style == "rectangle":
            rectangle(fill_color=background, width=original_width, height=original_width, thickness=2)
            rectangle(fill_color=fill_color, width=width, height=width)

        if style == "circle":
            circle(fill_color=background, size=original_width)
            circle(fill_color=fill_color, size=width)
        if write_seconds==True:
            write("%i" %((duration/1000+1)-(builtin_time.clock()-t0)), size = 2, color=write_color,outline=True, outline_color=write_outline)
        refresh()
        if reverse==False:
            width += width_per_frame
        else:
            width -= width_per_frame
        if color_fade==True:
            if color_end == "green":
                if red > 0:
                    red -= int(255/duration_frames)
                if green < 255:
                    green += int(255/duration_frames)

    if sound is True:
        for i in melody:
            winsound.Beep(i, 25)
#            time.wait(50)

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def start_screen(name="test", path="./Logo/", extension=".png", authors="", language="en"):
    """
    Help incomplete, sorry. Expecting a "Logo_" prefix to the image.

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
    newpage("white", auto_refresh=False)

    # Logo
    try:
        image(path + "Logo_" + name + extension, y=2, size=5)
    except:
        write(name, style="bold", y=2, size=5)

    # Authors
    write(authors, style='light', y=-1.7, size=0.6)

    # End
    if language == "fr" or language == "french":
        write('Appuyez sur ENTRER pour commencer.', style='end')
    else:
        write('Press ENTER to start.', style='end')

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def end_screen(name="test", success=True, path="./Logo/", extension=".png", authors="", language="en"):
    """
    Help incomplete, sorry. Expecting a "Logo_" prefix to the image.

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
    newpage("white", auto_refresh=False)

    # Logo
    try:
        image(path + "Logo_" + name + extension, y=7.5, size=4)
    except:
        write(name, style="bold", y=7.5, size=4)

    # Authors
    write(authors, style='light', y=4.25, size=0.6)

    # End
    if language == "fr" or language == "french":
        if success is True:
            write("Enregistrement des données réussi.", color='green')
        else:
            write("Echec de l'enregistrement des données.", color='red')
        write('Appuyez sur ENTRER pour quitter.', style='end')
    else:
        if success is True:
            write("Successful Data Collection.", color='green')
        else:
            write("Failed Data Collection.", color='red')
        write('Press ENTER to quit.', style='end')

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def sound(filename, path="", extension=".wav", wait=True, rate=48000):
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
    file = path + filename + extension
    if ".wav" in file:
        pygame.mixer.quit()
        pygame.mixer.init(frequency=rate)
        sound = pygame.mixer.Sound(file)
        sound.play()
        if wait is True:
            while pygame.mixer.get_busy():
                time.wait(10)

    else:
        print("NEUROPSYDIA ERROR: sound(): Wrong extension: only '.wav' are currently supported.")


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def opendoc():
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
    - webbrowser
    """
    webbrowser.open("https://github.com/neuropsychology/Neuropsydia.py/")

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def color_luminance(colour, perceived=True):
    """
    Compute the luminance based on the rgb colour. Based on http://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color.

    Parameters
    ----------
    r =  int
        red
    g = int
        green
    b = int
        blue
    perceived = bool, opt
        Adjusted formula for human eye.

    Returns
    ----------
    luminance = float
        The luminance value.

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start(False)
    >>> n.color_luminance(6, 124, 16)

    Authors
    ----------
    Dominique Makowski
    """
    colour = color(colour)
    r = colour[0]/255
    g = colour[1]/255
    b = colour[2]/255

    if perceived is False:
        luminance = (0.2126*r + 0.7152*g + 0.0722*b)
    else:
        luminance = np.sqrt( 0.299*(r**2) + 0.587*(g**2) + 0.114*(b**2))
    return(luminance)

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def color_contrast(color1, color2, perceived=True):
    """
    Compute the contrast ratio between two colours. Based on https://www.w3.org/TR/WCAG20/#contrast-ratiodef.

    Parameters
    ----------
    color1 = str or tuple
        First colour
    color2 = str or typle
        Second colour
    perceived = bool, opt
        Should the contrast be based on the human perceived luminance

    Returns
    ----------
    contrast = float
        The contrast ratio value.

    Example
    ----------
    >>> import neurokit as nk
    >>> nk.luminance(6, 124, 16)

    Authors
    ----------
    Dominique Makowski
    """
    l1 = color_luminance(color1, perceived=perceived)
    l2 = color_luminance(color2, perceived=perceived)
    if l1 > l2:
        contrast = (l1 + 0.05) / (l2 + 0.05)
    else:
        contrast = (l2 + 0.05) / (l1 + 0.05)

    return(contrast)


