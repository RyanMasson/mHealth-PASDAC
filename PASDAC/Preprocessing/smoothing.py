import pandas as pd

def smoothing(dataDf, method="sliding", **kwargs):

    """smoothing function including sliding smoothing(box smoothing) and gaussian filter

    Parameters
    ----------
        dataDf:                 dataFrame
        method:                 str.  "sliding" or "gaussian"
        kwargs:
          when method == "sliding":
            winsize:            int

          when method == "gaussian":
            winsize:            int
            sigma:              int

    Return
    ------
        dataDf:                 dataFrame

    """
    if method == "sliding":
        if 'winsize' in kwargs:
            winsize = kwargs['winsize']
        else:
            winsize = 10
            print("Arg 'winsize' is set as default ", winsize)
            
        dataDf = dataDf.rolling(window=winsize, center=False).mean()
        dataDf = dataDf.fillna(method = 'backfill')

    # TODO: implement gaussian smoothing method according to the requirement
    # elif method == "gaussian":

    return dataDf