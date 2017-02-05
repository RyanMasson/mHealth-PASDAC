import os, sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tools/labels'))
from label2OneHotLabel import label2OneHotLabel
from sklearn.neighbors import KNeighborsClassifier


def classification(trainData, trainLabels, testData, SETTINGS):
    """Train model with trainData and trainLabels, then predict testLabels given testData. 
    Output one hot representation and probability

    Parameters
    ----------
        trainingData:               dataFrame
        trainLabels:                dataFrame
        testData:                   dataFrame
        SETTINGS:                   class 

    Return
    ------
        oneHotDf:                   dataFrame
        probaDf:                    dataFrame

    """
    method = SETTINGS.CLASSIFIER
    classLabels = SETTINGS.CLASSLABELS
    verbose = SETTINGS.VERBOSE_LEVEL

    if verbose >= 2:
        print('  -> Classification '+ method)

    trainData = trainData.as_matrix()
    trainLabels = trainLabels.as_matrix().ravel()
        
    if method == 'NaiveBayes':

        pass

    elif method ==  'knnVoting':

        classifier = KNeighborsClassifier(5)
        model =  classifier.fit(trainData, trainLabels)

        testData = testData.as_matrix()

        result = model.predict(testData)
        proba = model.predict_proba(testData)

        labelDf = pd.DataFrame(data = result, columns = ['Label'])
        probaDf = pd.DataFrame(data = proba, columns = classLabels)
        
        oneHotDf = label2OneHotLabel(labelDf, classLabels)

    return oneHotDf, probaDf