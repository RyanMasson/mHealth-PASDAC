from class_settings import SETTING

setting1 = SETTING('Data2R','Output','/Feature')
setting1.set_SAMPLINGRATE(32)# sampling rate
setting1.set_SUBJECT(1)
setting1.set_SUBJECT_TOTAL(2)
setting1.set_DATASET('gesture')
setting1.set_SEGMENTATION_TECHNIQUE('SlidingWindow')
setting1.set_FEATURE_TYPE('VerySimple') # type of features to calculate, possible values: Raw, VerySimple, Simple, FFT, All
setting1.set_W_SIZE_SECOND(1) # window size for feature calculation in seconds	
setting1.set_W_STEP_SECOND(0.1) # step size for feature calculation in seconds
setting1.set_SAVE(1) # (de)activate saving of variable outputs
setting1.set_PLOT(1) # (de)activate plotting
setting1.set_VERBOSE_LEVEL(2) # verbose level for debug messages, possible values: 0 (quiet), 1 (results), 2 (processing steps)
setting1.set_FEATURE_SELECTION('none') # feature selection method to use, possible values: none, mRMR, SFS, SBS
setting1.set_FEATURE_SELECTION_OPTIONS(10) # number of features to select
setting1.set_FUSION_TYPE('early') # 'early' (i.e. feature-level) or 'late' (i.e. classifier-level) data fusion
setting1.set_CLASSIFIER('knnVoting') # classifier to use, possible values: knnVoting, NaiveBayes, SVM, liblinear, SVMlight, DA, cHMM, jointboosting
setting1.set_CLASSIFIER_OPTIONS('knnVoting')
setting1.set_EVALUATION('pd') # type of evaluation, possible values: pd (person-dependent), pi (person-independent, leave-one-person-out), loio (leave-one-instance-out)


if __name__ == "__main__":
	print(setting1.SAMPLINGRATE)
	print(setting1.CLASSIFIER)
	print(setting1.CLASSLABELS)
	print(setting1.CLASSIFIER_OPTIONS_TRAINING)
	print(setting1.CLASSIFIER_OPTIONS_TESTING)
	print(setting1.EVALUATION)
	print(setting1.SAVE)
