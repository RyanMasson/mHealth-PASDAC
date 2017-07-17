import pandas as pd
import numpy as np

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

    elif method == "gaussian":
	if 'winsize' in kwargs:
	    winsize = kwargs['winsize']
	else:
	    winsize = 10
	    print("Arg 'winsize' is set as default ", winsize)

	rows = dataDf.shape[0]
	columns = dataDf.shape[1]
	windows_per_column = rows/winsize
	zeros = np.zeros(winsize-1)
	sigma = 1

	for i in range(columns):
	    for j in range(windows_per_column):
		curr_window = dataDf.iloc[:,i][j*winsize:((j*winsize)+winsize)]
		
		# pad zeros onto the left of the current window(j) of the current column(i)
		padded_win = np.append(zeros, curr_window)

		# build a normalized Gaussian kernel from this window
		kernel = [1.59837446e-05, 8.72682888e-04, 1.75283044e-02, 1.29517624e-01,
				3.52065405e-01, 3.52065405e-01, 1.29517624e-01, 1.75283044e-02,
					8.72682888e-04, 1.59837446e-05]		

		#kernel = np.zeros(winsize)
		#for y in range(winsize):
		    #kernel[y] = (1/(sigma*np.sqrt(2*np.pi)))*(1/(np.exp((curr_window.iloc[y]**2)/(2*sigma**2))))
		    #kernel[y] = (1/(sigma*np.sqrt(2*np.pi)))*(np.exp(-(curr_window.iloc[y]**2)/(2*sigma**2)))
		# normalize
		sum = 0.0
                for z in range(len(kernel)):
		    sum += kernel[z]
                for t in range(len(kernel)):
		    kernel[t] = kernel[t] / sum
		
		# reassign the current window of the data
		for k in range(winsize):
		    smoothed_point = 0.0		

		    # calculate smoothed data point
		    for x in range(winsize):
			smoothed_point += padded_win[k+x] * kernel[x]

		    dataDf.iloc[:,i][j*winsize:(j*winsize+winsize)][k] = smoothed_point

    print("saving smoothed data to csv file masson_smoothed_data.csv")
    dataDf.to_csv('masson_smoothed_data.csv')
	
    return dataDf
