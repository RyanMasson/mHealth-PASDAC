import pandas as pd
import numpy as np

def segments2label(segments):
    
    """ Transform label representation to segment representation

    Parameters
    ----------
        segments:   dataFrame
                    with 'Start', 'End', 'Length', 'Label', 'Counter' as headers
    return
    ------
        labeling:   dataFrame
                    with 'Label' as headers
    """

    labeling = [];

    if len(segments) == 0:
        return

    totalsize = segments["End"].iloc[-1]

    # segments contains labelList in the 4th column
    if (len(segments.columns) >= 4):
        labels = segments["Label"].as_matrix()
    else:
        # label 1 is doing nothing by default
        labels = np.ones(len(segments))

    labeling = pd.DataFrame(data = np.zeros(totalsize), columns = ["Label"] ,dtype = int)

    for seg in range(len(segments)):
        labeling["Label"].iloc[segments.ix[seg,0]-1 : segments.ix[seg,1]] = labels[seg]

    labeling = labeling.iloc[:totalsize] # restrict to totalsize

    return labeling
