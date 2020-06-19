import numpy as np

def prepare_data_days(data, range_= 10, month=1, days=3): 

    data = data.astype(float)
    data = data[-(365*range_):,:]
    
    xtrain, ytrain = [], []
    for i in range(data.shape[0]): 
        if i + days >= len(data[:,0]): break 
        
        xtrain.append(data[i:i + days,:])
        ytrain.append(data[i + days,:])
    
    print(ytrain[-1])
