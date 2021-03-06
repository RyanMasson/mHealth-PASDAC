import numpy as np
from Segmentation.segment import segment
from Preprocessing.splitIntoRepetitions import splitIntoRepetitions
from Preprocessing.smoothing import smoothing
from Segmentation.assignLabels import assignLabels
from Features.featureExtraction import featureExtraction


def runPreprocess(dataAll, labelsAll, segmentsAll, SETTINGS):

    """ Run preprocess, including smoothing, splitting data, labels and segments into repetitions,
    doing segmentation and feature extraction for each repetition

    Parameters
    ----------
        dataAll:                dataFrame
        labelsAll:              dataFrame
        segmentsAll:            dataFrame
        SETTINGS:               struct

    Return
    ------
        features:               list of dataFrames
        fType:                  list
                                eg: ['Mean_acc_1_x', 'Variance_acc_1_x', 'Mean_acc_1_y', 'Variance_acc_1_y',
                                    ....
                                   'Mean_gyr_3_y', 'Variance_gyr_3_y']
        fDescr:                 list
                                eg: ['Mean', 'Variance']
        segments:               list of dataFrames
        segmentations:          list of dataFrames
        labelsSegmentations:    list of dataFrames
        
    """
    # (0) Smoothing
    dataAll = smoothing(dataAll, 'gaussian', winsize = 10)

    # (1) Preprocessing
    # Split data set into repetitions
    # data, labels, segments are arrays containing dataframes
    data, labels, segments, nRepetitions = splitIntoRepetitions(dataAll, labelsAll, segmentsAll) 

    features = []
    segmentations = []
    labelsSegmentationRepetitions = []

    # Loop over repetitions
    for i in range(nRepetitions):
        
        if SETTINGS.VERBOSE_LEVEL >= 2:
            print('REPETITION '+str(i)+'/'+str(nRepetitions))
        else:
            pass
        
        # (2) Segmentation
        segmentations.append(segment(data[i], 'SlidingWindow', SETTINGS))
        labelsSegmentations = assignLabels(segments[i], segmentations[i])
        labelsSegmentationRepetitions.append(labelsSegmentations)
        
        # (3) Feature extraction    
        feat, fType, fDescr = featureExtraction(data[i], segmentations[i], SETTINGS.FEATURE_TYPE, SETTINGS.VERBOSE_LEVEL)
        features.append(feat)
    
    labelsSegmentations = labelsSegmentationRepetitions
    
    return features, fType, fDescr, segments, segmentations, labelsSegmentations 
