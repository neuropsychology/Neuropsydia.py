# -*- coding: utf-8 -*-
from pygame import gfxdraw
import platform

from .core import *
from .write import *

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def remove_following_duplicates(mylist):
    """
    Remove the duplicates that are following themselves, returning a list of ordered items.

    Parameters
    ----------
    mylist =  list
        A list

    Returns
    ----------
    The list without following duplicates.

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start(False)
    >>> mylist = ["a","a","b","a","a","a","c","c","b","b"]
    >>> n.remove_following_duplicates(mylist)

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - os
    - platform
    """
    index = 0
    while index != len(mylist):
        try:
            while mylist[index] == mylist[index+1]:
                mylist.pop(index+1)
        except:
            pass
        index += 1
    return(mylist)
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def get_creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.

    Parameters
    ----------
    path_to_file =  str
        The path

    Returns
    ----------
    creation_date

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start(False)
    >>> date = n.get_creation_date(path)

    Authors
    ----------
    Mark Amery

    Dependencies
    ----------
    - os
    - platform
    """
    if platform.system() == 'Windows':
        return(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            return(stat.st_birthtime)
        except AttributeError:
            print("Neuropsydia error: get_creation_date(): We're probably on Linux. No easy way to get creation dates here, so we'll settle for when its content was last modified.")
            return(stat.st_mtime)

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
    """
    left_x = Coordinates.to_pygame(x = left_x)
    left_y = Coordinates.to_pygame(y = left_y)
    right_x = Coordinates.to_pygame(x = right_x)
    right_y = Coordinates.to_pygame(y = right_y)

    if left_x == right_x or left_y == right_y:
        pygame.draw.line(screen, color(line_color), (left_x, left_y), (right_x, right_y), thickness)
    else:
        pygame.draw.aaline(screen, color(line_color), (left_x, left_y), (right_x,right_y), thickness)

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def rectangle(x=0, y=0, width=10, height=10, line_color="black", thickness=1, fill_color=None, opacity=225):
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
    """
    left = Coordinates.to_pygame(x= (x - width / 2))
    top = Coordinates.to_pygame(y= (y + height /2))
    width = Coordinates.to_pygame(distance_x = width)
    height = Coordinates.to_pygame(distance_y = -height)

    if fill_color != None:
        pygame.draw.rect(screen, color(fill_color),(left,top,width,height),0)
    pygame.draw.rect(screen, color(line_color),(left,top,width,height),thickness)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def circle(x=0, y=0, size=10, line_color="black", thickness=0, fill_color="white", opacity=225):
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