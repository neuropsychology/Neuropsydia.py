# -*- coding: utf-8 -*-
from .path import *
from .core import *
from .image import *
from .write import *


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def start(open_window=True):
    """
    Initialize all the components of Neuropsydia. Always at the beginning of a neuropsydia script.

    Parameters
    ----------
    open_window = bool
        should it open the pygame's window or close it immediatly (useful when using neuropsydia for something else than experiments, e.g., statistics)

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.event.set_blocked(pygame.KEYDOWN)


    if open_window == False:
        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.mouse.set_visible(True)
        pygame.quit()

    else:
        background_color("black")
        write('Initialisation...', size=0.8, y=-9, color="lightblue")
        refresh()

        preloaded = {}
        preloaded = preload("Neuropsydia_PSY_blue", extension = ".png", y= -2.5, size=4.25, cache = preloaded, path = Path.logo())
        preloaded = preload("Neuropsydia_TEXT_white", extension = ".png", y= 7, size=1.5, cache = preloaded, path = Path.logo())
        preloaded = preload("Neuropsydia_HEAD_white", extension = ".png", y= -2.5, size=4.25, cache = preloaded, path = Path.logo())

        background_color("black")
        image("Neuropsydia_TEXT_white", extension = ".png", y= 7, size=1.5, cache = preloaded, path = Path.logo())
        image("Neuropsydia_PSY_blue", extension = ".png", y= -2.5, size=4.25, cache = preloaded, path = Path.logo())
        write('Press ENTRER to continue.', size=0.8, y=-9, color="white", allow="ENTER")

        for i in range(0,100,2):
            background_color("black")
            image("Neuropsydia_HEAD_white", extension = ".png", y= -2.5, size=4.25, cache = preloaded, path = Path.logo())
            background_color("black",opacity = 100 - i)
            image("Neuropsydia_TEXT_white", extension = ".png", y= 7, size=1.5, cache = preloaded, path = Path.logo())
            image("Neuropsydia_PSY_blue", extension = ".png", y= -2.5, size=4.25, cache = preloaded, path = Path.logo())
            refresh()
        time.wait(1000)
        background_color("white",fade=True)
        refresh()

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def close():
    """
    A clean closing of all the components of Neuropsydia. Always at the end of a neuropsydia script.

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    background_color("black")
    write("Please wait...",color="white")
    refresh()

    preloaded = {}
    preloaded = preload("Neuropsydia_TEXT_white", extension = ".png", y= 5.5, size=1.25, cache = preloaded, path = Path.logo())
    preloaded = preload("Neuropsydia_HEAD_white", extension = ".png", y= -3, size=3.75, cache = preloaded, path = Path.logo())
    preloaded = preload("Neuropsydia_PSY_blue", extension = ".png", y= -3, size=3.75, cache = preloaded, path = Path.logo())
    preloaded = preload('N', extension = ".png", x=7, y=-8, size=1.0, cache = preloaded, path = Path.logo())
    preloaded = preload("Python", extension = ".png", x=-7, y=-8, size=0.4, cache = preloaded, path = Path.logo())

    for i in range(0,100,2):
        background_color("black")
        write("Merci d'avoir utilisé", style="light", y=8.75, size=1, color="white")
        image("Neuropsydia_TEXT_white", extension = ".png", y= 5.5, size=1.25, cache = preloaded, path = Path.logo())
        image("Neuropsydia_HEAD_white", extension = ".png", y= -3, size=3.75, cache = preloaded, path = Path.logo())
        image("Neuropsydia_PSY_blue", extension = ".png", y= -3, size=3.75, cache = preloaded, path = Path.logo())
        image('N', extension = ".png", x=7, y=-8, size=1.0, cache = preloaded, path = Path.logo())
        image("Python", extension = ".png", x=-7, y=-8, size=0.4, cache = preloaded, path = Path.logo())
        background_color("black", opacity = 100-i)
        refresh()
    time.wait(1500)

    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.mouse.set_visible(True)
    pygame.quit()


