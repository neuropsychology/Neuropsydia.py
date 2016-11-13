# -*- coding: utf-8 -*-
import mne
import pandas as pd
import numpy as np
import datetime

from .stats import z_score  # process_EDA()
from .miscellaneous import get_creation_date  # acq_to_df()

import cvxopt as cv  # process_EDA()
import cvxopt.solvers  # process_EDA()
import bioread  # acq_to_df()

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def acq_to_df(file, samples=1, unit="s", method="mean"):
    """
    Format a BIOPAC's AcqKnowledge file into a pandas' dataframe.

    Parameters
    ----------
    file =  str
        the path of a BIOPAC's AcqKnowledge file
    samples = int
        the final frequency (samples/unit)
    unit = str
        "s" or "ms", to calculate the frequency
    method = str
        "mean" or "pad", resampling method

    Returns
    ----------
    df = pandas.DataFrame()
        the dataframe


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start(False)
    >>>
    >>> df = acq_to_df('file.acq')

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pandas
    - bioread
    - datetime
    """
    # Read file
    creation_date = get_creation_date(file)
    file = bioread.read(file)

    # Convert creation date
    creation_date = datetime.datetime.fromtimestamp(creation_date)


    # Get the channel frequencies
    freq_list = []
    for channel in file.named_channels:
        freq_list.append(file.named_channels[channel].samples_per_second)

    # Get data with max frequency and the others
    data = {}
    data_else = {}
    for channel in file.named_channels:
        if file.named_channels[channel].samples_per_second == max(freq_list):
            data[channel] = file.named_channels[channel].data
        else:
            data_else[channel] = file.named_channels[channel].data

    # Create index
    time = []
    beginning_date = creation_date - datetime.timedelta(0, max(file.time_index))
    for timestamps in file.time_index:
        time.append(beginning_date + datetime.timedelta(0, timestamps))

    df = pd.DataFrame(data, index=time)

    # Create resampling factor
    if unit == "ms":
        resample_factor = str(samples) + "L"
    if unit == "s":
        resample_factor = str(samples) + "S"


    # max frequency must be 1000
    for channel in data_else:
        channel_frequency = file.named_channels[channel].samples_per_second
        serie = data_else[channel]
        index = list(np.arange(0, max(file.time_index), 1/channel_frequency))
        index = index[:len(serie)]
        # Create index
        time = []
        for timestamps in index:
            time.append(beginning_date + datetime.timedelta(0, timestamps))
        data_else[channel] = pd.Series(serie, index=time)
    df2 = pd.DataFrame(data_else)


    # Resample
    if method == "mean":
        df2 = df2.resample(resample_factor).mean()
        df = df.resample(resample_factor).mean()
    if method == "pad":
        df2 = df2.resample(resample_factor).pad()
        df = df.resample(resample_factor).pad()
    df = pd.concat([df, df2], 1)

    return(df)
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def process_EDA(EDA_raw, sampling_rate, tau0=2., tau1=0.7, delta_knot=10., alpha=0.4, gamma=1e-2, solver=None, options={'reltol':1e-9}):
    """
    A convex optimization approach to electrodermal activity processing (CVXEDA)

    This function implements the cvxEDA algorithm described in "cvxEDA: a
    Convex Optimization Approach to Electrodermal Activity Processing" (Greco et al., 2015).

    Parameters
    ----------
       EDA_raw
           observed EDA signal (we recommend normalizing it: EDA_raw = zscore(EDA_raw))
       sampling_rate
           sampling rate (samples/seconds) of EDA_raw
       tau0
           slow time constant of the Bateman function
       tau1
           fast time constant of the Bateman function
       delta_knot
           time between knots of the tonic spline function
       alpha
           penalization for the sparse SMNA driver
       gamma
           penalization for the tonic spline coefficients
       solver
           sparse QP solver to be used, see cvxopt.solvers.qp
       options
           solver options, see http://cvxopt.org/userguide/coneprog.html#algorithm-parameters

    Returns
    ----------
       phasic
           phasic component
       tonic
           tonic component
       p
           sparse SMNA driver of phasic component
       l
           coefficients of tonic spline
       d
           offset and slope of the linear drift term
       e
           model residuals
       obj
           value of objective function being minimized (eq 15 of paper)

    Authors
    ----------
    Luca Citi (lciti@ieee.org), Alberto Greco

    Citation
    ----------
    A Greco, G Valenza, A Lanata, EP Scilingo, and L Citi
    "cvxEDA: a Convex Optimization Approach to Electrodermal Activity Processing"
    IEEE Transactions on Biomedical Engineering, 2015
    DOI: 10.1109/TBME.2015.2474131

    Dependencies
    ----------
    - cvxopt
    - numpy
    """
    frequency = 1/(sampling_rate/100)

    EDA_raw = z_score(EDA_raw)

    n = len(EDA_raw)
    EDA_raw = cv.matrix(EDA_raw)

    # bateman ARMA model
    a1 = 1./min(tau1, tau0) # a1 > a0
    a0 = 1./max(tau1, tau0)
    ar = np.array([(a1*frequency + 2.) * (a0*frequency + 2.), 2.*a1*a0*frequency**2 - 8.,
        (a1*frequency - 2.) * (a0*frequency - 2.)]) / ((a1 - a0) * frequency**2)
    ma = np.array([1., 2., 1.])

    # matrices for ARMA model
    i = np.arange(2, n)
    A = cv.spmatrix(np.tile(ar, (n-2,1)), np.c_[i,i,i], np.c_[i,i-1,i-2], (n,n))
    M = cv.spmatrix(np.tile(ma, (n-2,1)), np.c_[i,i,i], np.c_[i,i-1,i-2], (n,n))

    # spline
    delta_knot_s = int(round(delta_knot / frequency))
    spl = np.r_[np.arange(1.,delta_knot_s), np.arange(delta_knot_s, 0., -1.)] # order 1
    spl = np.convolve(spl, spl, 'full')
    spl /= max(spl)
    # matrix of spline regressors
    i = np.c_[np.arange(-(len(spl)//2), (len(spl)+1)//2)] + np.r_[np.arange(0, n, delta_knot_s)]
    nB = i.shape[1]
    j = np.tile(np.arange(nB), (len(spl),1))
    p = np.tile(spl, (nB,1)).T
    valid = (i >= 0) & (i < n)
    B = cv.spmatrix(p[valid], i[valid], j[valid])

    # trend
    C = cv.matrix(np.c_[np.ones(n), np.arange(1., n+1.)/n])
    nC = C.size[1]

    # Solve the problem:
    # .5*(M*q + B*l + C*d - EDA_raw)^2 + alpha*sum(A,1)*p + .5*gamma*l'*l
    # s.t. A*q >= 0

    old_options = cv.solvers.options.copy()
    cv.solvers.options.clear()
    cv.solvers.options.update(options)
    if solver == 'conelp':
        # Use conelp
        z = lambda m,n: cv.spmatrix([],[],[],(m,n))
        G = cv.sparse([[-A,z(2,n),M,z(nB+2,n)],[z(n+2,nC),C,z(nB+2,nC)],
                    [z(n,1),-1,1,z(n+nB+2,1)],[z(2*n+2,1),-1,1,z(nB,1)],
                    [z(n+2,nB),B,z(2,nB),cv.spmatrix(1.0, range(nB), range(nB))]])
        h = cv.matrix([z(n,1),.5,.5,EDA_raw,.5,.5,z(nB,1)])
        c = cv.matrix([(cv.matrix(alpha, (1,n)) * A).T,z(nC,1),1,gamma,z(nB,1)])
        res = cv.solvers.conelp(c, G, h, dims={'l':n,'q':[n+2,nB+2],'s':[]})
        obj = res['primal objective']
    else:
        # Use qp
        Mt, Ct, Bt = M.T, C.T, B.T
        H = cv.sparse([[Mt*M, Ct*M, Bt*M], [Mt*C, Ct*C, Bt*C],
                    [Mt*B, Ct*B, Bt*B+gamma*cv.spmatrix(1.0, range(nB), range(nB))]])
        f = cv.matrix([(cv.matrix(alpha, (1,n)) * A).T - Mt*EDA_raw,  -(Ct*EDA_raw), -(Bt*EDA_raw)])
        res = cv.solvers.qp(H, f, cv.spmatrix(-A.V, A.I, A.J, (n,len(f))),
                            cv.matrix(0., (n,1)), solver=solver)
        obj = res['primal objective'] + .5 * (EDA_raw.T * EDA_raw)
    cv.solvers.options.clear()
    cv.solvers.options.update(old_options)

    l = res['x'][-nB:]
    d = res['x'][n:n+nC]
    t = B*l + C*d
    q = res['x'][:n]
    p = A * q
    r = M * q
    e = EDA_raw - r - t

    results = (np.array(a).ravel() for a in (r, t, p, l, d, e, obj))

    return(results)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def extract_peak(channel_data, value="max", size=0):
    """
    Exctract the peak (max or min) of one or several channels.

    Parameters
    ----------
    channel_data = pandas.DataFrame
        Use the `to_data_frame()` method for evoked nme data.
    value = str
        "max" or "min".
    size = int
        Return an averaged peak from how many points before and after.

    Returns
    ----------
    tuple
        (peak, time_peak)

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start(False)
    >>>
    >>> channel_data = evoked.pick_channels(["C1", "C2"]).to_data_frame()
    >>> peak, time_peak = extract_peak(channel_data, size=2)
    >>>
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - mne > 0.13.0
    - numpy
    - pandas
    """
    data = channel_data.mean(axis=1)
    data.plot()
    if value == "max":
        peak = np.max(data)
        time_peak = np.argmax(data)
    if value == "min":
        peak = np.min(data)
        time_peak = np.argmin(data)
    if size > 0:
        peak_list = [peak]
        peak_index = list(data.index).index(time_peak)
        data = data.reset_index(drop=True)
        for i in range(size):
            peak_list.append(data[peak_index+int(i+1)])
            peak_list.append(data[peak_index-int(i-1)])
        peak = np.mean(peak_list)
    return(peak, time_peak)




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
        return(events, event_id, names)
    else:
        events = np.array([event_times, [0]*len(event_times), [1]*len(event_times)]).T
        return(events, event_id)





