import numpy as np
import tensorflow as tf

def prepare_data_days(data, keyindex, range_= 1, days=3 ): 

    data = data.astype(float)
    data = data[:,1:]
    data = data[-(365*range_):,:]
    
    xdata, ydata = [], []
    for i in range(data.shape[0]): 
        if i + days >= data.shape[0]: break 
        
        xdata.append(data[i:i + days,:])
        ydata.append(data[i + days, keyindex])


    return xdata, ydata


def split_data(xdata, ydata, faktor = .1, count = 0):
    '''
    expects:
        xdata,ydata lists
        factor: percentage of test data
        count: integer, data splitted into parts size *factor, select the counter-th part
    '''
    #compute the startin/end point
    start = int(faktor * count * len(xdata))
    end = int(faktor * (count + 1) * len(xdata))
    
    #create training and test sets
    xtest, ytest= xdata[start:end], ydata[start:end]
    del xdata[start:end]
    del ydata[start:end]
    	
    return (xdata,ydata), (xtest,ytest)

def learn(xtrain,ytrain,xtest,ytest):
    xtrain = np.array(xtrain)
    ytrain = np.array(ytrain)
    xtest = np.array(xtest)
    ytest = np.array(ytest)
    print(xtrain.shape, ytrain.shape)
    xtrain = tf.cast(xtrain.reshape(xtrain.shape[0] , xtrain.shape[1] * xtrain.shape[2]), dtype=tf.float32)
    xtest = tf.cast(xtest.reshape(xtest.shape[0] , xtest.shape[1] * xtest.shape[2]),dtype=tf.float32)
    

