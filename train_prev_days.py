import numpy as np

def prepare_data_days(data, range_= 1, days=3): 

    data = data.astype(float)
    data = data[-(365*range_):,:]
    
    xdata, ydata = [], []
    for i in range(data.shape[0]): 
        if i + days >= data.shape[0]: break 
        
        xdata.append(data[i:i + days,:])
        ydata.append(data[i + days,:])

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
    

