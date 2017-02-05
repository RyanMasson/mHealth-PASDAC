import numpy as np

def coreEvaluate(labels, pred, c):
    
    """ calculate metrics for class c and non-class c. 

    Parameters
    ----------
        labels:                 ndarray
        pred:                   ndarray
        c:                      int

    Return
    ------
        precisions:             ndarray
        recalls:                ndarray
        fallouts:               ndarray
        ccuracys:               ndarray

    """

    precisions = np.zeros(2)
    recalls = np.zeros(2)
    fallouts = np.ones(2)
    specificities = np.zeros(2)
    NPVs = np.zeros(2)
    FDRs = np.zeros(2)
    FNRs = np.ones(2)
    accuracies = np.ones(2)
    f1_pos = np.zeros(1)
    MCC = 0
    CKappa = 0







    return precisions, recalls, fallouts, specificities, NPVs, FDRs, FNRs, accuracies, f1_pos, MCC, CKappa


if __name__ == "__main__":
    
    import pandas as pd

    labels = pd.DataFrame(data = np.array([1, 1, 1, 2, 2, 2]))
    pred = pd.DataFrame(data = np.array([1, 1, 2, 2, 1, 1]))

    labelsArr = labels.as_matrix()
    predArr = pred.as_matrix()

    print(coreEvaluate(labelsArr, predArr, 1))
