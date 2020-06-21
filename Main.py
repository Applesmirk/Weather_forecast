from get_data import *
from read_data import read_data
import numpy as np 
from train_prev_days import * 
from validation import cross_validation


station_id = 4104

#downloading data 
download_id(station_id)

#reading the data, and chossing which variables one wants to use 
data = read_data(station_id)

#extracting the value one wants to predict how many years the model should be included and how many continous days each data entry should contain 
xdata, ydata = prepare_data_days(data, keyindex = 0,range_= 5, days = 3)

#splitting the data in train and test data
(xtrain,ytrain), (xtest,ytest) = split_data(xdata, ydata, count = 5)

#training the model
model = learn(xtrain, ytrain)

#predicting the test data with our model 
pred, error = test (xtest, ytest, model)
print ("Mean error for test data:", error)


#Validating the algorithm with cross validaton (10 Models get trained each with different training data)
#print("Mean Error:", cross_validation(xdata, ydata))
