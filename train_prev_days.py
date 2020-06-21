import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

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

def learn(xtrain, ytrain):
    '''
    machine learning function returns the machine learning model
    expects:
        xtrain,ytrain training data
    '''
    print('--- creating model ---')

    #x reshape von days * keys dim zu einer dim
    xtrain = np.array(xtrain)
    ytrain = np.array(ytrain)
    xtrain = np.reshape(xtrain ,(xtrain.shape[0], xtrain.shape[1] * xtrain.shape[2]))

    n_features = xtrain.shape[1]
    layersize = int(2*n_features/3)
    model = Sequential () 
    model.add(Dense(layersize, activation='relu', kernel_initializer='he_normal',input_shape=(n_features,)))
    model.add(Dense(int(layersize/2), activation='relu', kernel_initializer='he_normal' ))
    model.add(Dense(1))
    

    model.compile(optimizer='adam', loss='mse')
    model.fit(xtrain, ytrain, epochs=200, batch_size=20, verbose=0)

    return model
    
def test(xtest,ytest,model):
    '''
    tests the model and returns the predictions and the mean squared error 
    expects:
        xtest,ytest datasets
        keras model
    '''
    xtest = np.array(xtest)
    ytest = np.array(ytest)
    xtest = np.reshape(xtest ,(xtest.shape[0], xtest.shape[1] * xtest.shape[2]))

    error = model.evaluate(xtest, ytest, verbose=0)
    pred = model.predict(xtest)
    
    return pred,error