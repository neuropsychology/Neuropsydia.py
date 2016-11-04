# -*- coding: utf-8 -*-
import mne


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def triggers_from_photodiode(photo_channel, names=None, treshold=0.04):
    """
    Create MNE compatible triggers based on a photodiode channel.

    Parameters
    ----------
    photo_channel = MNE channel
        The photodiode channel.
    names = list
        A list of event names.
    treshold = float
        The treshold to select the triggers.

    Returns
    ----------
    tuple
        (events, event_id)

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start(False)
    >>> 
    >>> raw = mne.io.read_raw("eeg_file")
    >>> photo_channel = raw.copy().pick_channels(['PHOTO'])
    >>> events, event_id = triggers_from_photodiode(photo_channel)
    >>> raw.add_events(events, stim_channel="STI 014")
    >>> 
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - mne > 0.13.0
    - numpy
    """
    original_names = names.copy()
    
    if names != None:
        event_names = list(set(names))
        event_index = [1, 2, 3, 4, 5, 32]
        event_id = {}
        for i in enumerate(event_names):
            names = [event_index[i[0]] if x==i[1] else x for x in names]
            event_id[i[1]] = event_index[i[0]]
          
    # Extract data from one channel
    data, times = photo_channel[:]
    T = list(data.T)
    
    events = []
    for i in range(len(times)):
        if T[i] < treshold:
            events.append(1)
        else:
            events.append(0)
    
    event_times = []
    for i in range(len(events)):
        if i > 0:
            if events[i]==1 and events[i-1]==0:
                event_times.append(i)

    if len(event_times) != len(original_names):
        print("NEUROPSYDIA ERROR: triggers_from_photodiode(): length of trigger names vector does not match the number of detected triggers (n = " +
              str(len(event_times)) + "), change names or crop the raw data")
    if names != None:
        events = np.array([event_times, [0]*len(event_times), names]).T
    else:
        events = np.array([event_times, [0]*len(event_times), [1]*len(event_times)]).T
                          
    return(events, event_id)



