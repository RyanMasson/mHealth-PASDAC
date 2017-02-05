import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tools/labels'))
from label2segments import label2segments

def splitIntoRepetitions(dataAll, labelsAll, segmentsAll):
    """Split data into a list of single repetitions

    Parameters
    ----------
        dataAll:                dataFrame
        labelsAll:              dataFrame
        segmentsAll:            dataFrame
        
    Return
    ------
        features:               list of dataFrames
    """
    endIndices = segmentsAll.loc[segmentsAll['Label'] == labelsAll.max()[0], 'End']
    endIndices = endIndices.reset_index(drop = True)
    startIndices = endIndices.shift().fillna(0).astype(int)

    data = []
    labels = []
    segments = []

    nRepetitions = startIndices.shape[0]

    for s, e in zip(startIndices, endIndices):
        data.append(dataAll.iloc[s:e,:].reset_index(drop = True).astype(int))
        labels.append(labelsAll.iloc[s:e].reset_index(drop = True).astype(int))
        segments.append(label2segments(labelsAll.iloc[s:e].reset_index(drop = True).astype(int)))

    return data, labels, segments, nRepetitions
