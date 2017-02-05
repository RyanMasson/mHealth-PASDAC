import pandas as pd
import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tools'))
from secondsToSamples import secondsToSamples
from .segmentSlidingWindow import segmentSlidingWindow


def segment(data,  method, SETTINGS):
    """Segment data into segmentations

    Parameters
    ----------
    data:           numpy array or dataFrame
    method:         string
    SETTINGS:       class  

    Return
    ------
    segments:       dataFrame

    """

    samplingRate = SETTINGS.SAMPLINGRATE
    wSizeSecond = SETTINGS.W_SIZE_SECOND
    sSizeSecond = SETTINGS.W_STEP_SECOND
    verbose = SETTINGS.VERBOSE_LEVEL
    wSize = secondsToSamples(wSizeSecond, samplingRate)
    sSize = secondsToSamples(sSizeSecond, samplingRate)

    if verbose >= 2:
        print('  -> Segmentation '+ method)
        
    if method == 'SlidingWindow':
        segments = segmentSlidingWindow(data, int(wSize), int(sSize))
        if SETTINGS.SAVE == 1:
            segments.to_csv(SETTINGS.PATH_OUTPUT + '/segmentation.csv', index = None, header=False)

    # elif method == 'Rest':

    return segments
