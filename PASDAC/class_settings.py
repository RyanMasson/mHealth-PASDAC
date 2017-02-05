class SETTING(object):

    def __init__(self, field1, field2, field3):
        """
        Attributes:
            PATH_DATA: 
            PATH_OUTPUT: 
            PATH_OUTPUT_FEATURES: 
        """
        self.PATH_DATA = field1
        self.PATH_OUTPUT = field2
        self.PATH_OUTPUT_FEATURES = self.PATH_OUTPUT + field3


    def set_SAMPLINGRATE(self, SAMPLINGRATE = 31):
        self.SAMPLINGRATE = SAMPLINGRATE  # sampling rate

    def set_SUBJECT(self, SUBJECT):
        self.SUBJECT = SUBJECT  # which subject to use, possible values: 1, 2

    def set_SUBJECT_TOTAL(self, SUBJECT_TOTAL):
        self.SUBJECT_TOTAL = SUBJECT_TOTAL  # total number of subjects 

    def set_DATASET(self, DATASET):
        self.DATASET = DATASET  # which dataset to use, possible values: walk, gesture

        if self.DATASET == 'gesture':
            self.CLASSLABELS = ['NULL', 'Open window', 'Drink', 'Water plant', 'Close window', 'Cut', 'Chop', 'Stir', 'Book', 'Forehand', 'Backhand','Smash']
            self.SENSOR_PLACEMENT = ['Right hand', 'Right lower arm', 'Right upper arm']
            self.CLASSES = len(self.CLASSLABELS) # number of classes
            # number of folds, this is ruled by the data set/test protocol, in splitIntoRepetitions.py file, this is set automatically from the dataset. Change FOLDS here without changing the dataset will not really change the FOLDS.
            self.FOLDS = 2 #26 for /Data, 2 for /Data2R
            self.SENSORS_AVAILABLE = ['acc_1_x', 'acc_1_y', 'acc_1_z','gyr_1_x', 'gyr_1_y', 'acc_2_x', 'acc_2_y', 'acc_2_z', 'gyr_2_x', 'gyr_2_y','acc_3_x', 'acc_3_y', 'acc_3_z', 'gyr_3_x', 'gyr_3_y'] # sensors available, one entry for each column of the data matrix
     
    def set_SEGMENTATION_TECHNIQUE(self, SEGMENTATION_TECHNIQUE):
        self.SEGMENTATION_TECHNIQUE = SEGMENTATION_TECHNIQUE  # segmentation technique, possible values: SlidingWindow, Rest, Energy

    def set_SEGMENTATION_OPTIONS_threshold(self, threshold):
        self.SEGMENTATION_OPTIONS_threshold = threshold  # segmentation options

    def set_FEATURE_TYPE(self, FEATURE_TYPE):
        self.FEATURE_TYPE = FEATURE_TYPE  # type of features to calculate, possible values: Raw, VerySimple, Simple, FFT, All

    def set_W_SIZE_SECOND(self, W_SIZE_SECOND):
        self.W_SIZE_SECOND = W_SIZE_SECOND  # window size for feature calculation in seconds

    def set_W_STEP_SECOND(self, W_STEP_SECOND):
        self.W_STEP_SECOND = W_STEP_SECOND  # step size for feature calculation in seconds

    def set_SAVE(self, SAVE):
        self.SAVE = SAVE  # (de)activate saving of variables

    def set_PLOT(self, PLOT):
        self.PLOT = PLOT  # (de)activate plot 

    def set_VERBOSE_LEVEL(self, VERBOSE_LEVEL):
        self.VERBOSE_LEVEL = VERBOSE_LEVEL  # verbose level for debug messages, possible values: 0 (quiet), 1 (results), 2 (processing steps)

    def set_FEATURE_SELECTION(self, FEATURE_SELECTION):
        self.FEATURE_SELECTION = FEATURE_SELECTION  # feature selection method to use, possible values: none, mRMR, SFS, SBS

    def set_FEATURE_SELECTION_OPTIONS(self, FEATURE_SELECTION_OPTIONS):
        self.FEATURE_SELECTION_OPTIONS = 10  # number of features to select

    def set_FUSION_TYPE(self, FUSION_TYPE):
        self.FUSION_TYPE = 'early'  # 'early' (i.e. feature-level) or 'late' (i.e. classifier-level) data fusion

    def set_CLASSIFIER(self, CLASSIFIER):
        self.CLASSIFIER = 'knnVoting'  # classifier to use, possible values: knnVoting, NaiveBayes, SVM, liblinear, SVMlight, DA, cHMM, jointboosting
    
    def set_CLASSIFIER_OPTIONS(self, CLASSIFIER):
        if CLASSIFIER == 'knnVoting': # main parameter: number of nearest neighbours (k), default 5
            self.CLASSIFIER_OPTIONS_TRAINING = []
            self.CLASSIFIER_OPTIONS_TESTING = ['k', 1] 

    def set_EVALUATION(self, EVALUATION):
        self.EVALUATION = EVALUATION  # type of evaluation, possible values: pd (person-dependent), pi (person-independent, leave-one-person-out), loio (leave-one-instance-out)
    
