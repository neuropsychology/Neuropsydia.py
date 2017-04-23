# -*- coding: utf-8 -*-
class Trigger():
    """
    A class object to send trigger via TTL, ethernet or stimtracker.

    Parameters
    ----------
    TTL = bool, optional
        Send trigger through the parallel port.
    photosensor = str, optional
        "white" or "black" for the color of the rectangle.
    photosensor_position = str, optional
        "bottomleft", "bottomright", "topleft" or "topright" for its position.
    stimtracker = bool, optional
        Send trigger through a stimtracker.
    stimtracker_duration = float, optional
        Time for the stimtracker trigger to last (in seconds).

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> trigger = n.Trigger()
    >>> trigger.start()
    >>> trigger.stop()
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - ctypes
    - pyxid
    """
    def __init__(self, TTL=True, photosensor=None, photosensor_position="bottomleft"):
        self.photosensor = photosensor
        self.photosensor_position = photosensor_position
        if self.method=="TTL":
            try:
                from ctypes import windll
                global io
                io = windll.dlportio # requires dlportio.dll !
            except:
                print("NEUROPSYDIA WARNING: Trigger(): The parallel port couldn't be opened")

    def start(self, trigger=1, port=0x378, lines=1):
        """
        Send the trigger.

        Parameters
        ----------
        trigger = int, optional
            What trigger to send (TTL).
        port = binary, optional
            Port address (TTL).
        lines = int, optional
            Lines to activate (stimtracker).

        Returns
        ----------
        None

        Example
        ----------
        >>> import neuropsydia as n
        >>> n.start()
        >>> trigger = n.Trigger()
        >>> trigger.start()
        >>> trigger.stop()
        >>> n.close()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - ctypes
        - pyxid
        """
        if self.photosensor != None:
            if self.photosensor_position == "bottomleft":
                rectangle(x=-10, y=-10, width=screen_width/screen_width, height=screen_width/screen_height, thickness=0, fill_color=self.photosensor)
            refresh()
        if self.method == "TTL":
            try:
                io.DlPortWritePortUchar(port, trigger)
            except:
                print('NEUROPSYDIA WARNING: Trigger.start(): Failed to send trigger!')

    def stop(self, trigger=0, port=0x378):
        """
        Return to baseline (for TTL only).

        Parameters
        ----------
        trigger = int, optional
            What trigger to send (TTL).
        port = binary, optional
            Port address (TTL).

        Returns
        ----------
        None

        Example
        ----------
        >>> import neuropsydia as n
        >>> n.start()
        >>> trigger = n.Trigger()
        >>> trigger.start()
        >>> trigger.stop()
        >>> n.close()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - ctypes
        - pyxid
        """
        if self.method == "TTL":
            try:
                io.DlPortWritePortUchar(port, trigger)
            except:
                print('NEUROPSYDIA WARNING: Trigger.stop(): Failed to send trigger!')