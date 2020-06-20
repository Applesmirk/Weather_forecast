import numpy as np 
from train_prev_days import *
import tensorflow as tf 



def cross_validation(xdata, ydata): 
    """ 
    Cross Validation splitting data in 10 parts training on 9 parts and testing on 1 
    afterwards returning the mean 
    """ 
    
    ME = 0 
    for i in range(10):
        (xtrain, ytrain), (xtest, ytest) = split_data(xdata, ydata, faktor = .1, count = i)
        predictions, MSE= test(xtest, ytest, learn(xtrain, ytrain))
        ME = ME + np.sqrt(MSE)
    
    ME = ME / 10
    
    return ME
