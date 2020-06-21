from get_data import *
from read_data import read_data
import numpy as np 
from train_prev_days import * 
from validation import *
import random

class locations:
    def __init__(self,city,station_id, altitude, longitude, prediction=0,model=0):
        self.city = city
        self.station_id = station_id
        self.altitude = altitude
        self.longitude = longitude
        self.prediction = prediction
        self.model = model

def get_city_models():
    '''

    '''

    stations = [
    locations('Regensburg', 4104, 49013430, 12101634),
    locations('Parsberg', 3875, 491603469, 117187275),
    locations('Schwandorf', 4592, 49319888, 12109135),
    locations('Schorndorf-Knöbling', 4559, 49160155, 12591019),
    locations('Elsendorf-Horneck', 7075, 48708826, 11809827),
    locations('Mallersdorf-Pfaffenberg', 3147, 48769303, 12227654),
    locations('Straubing', 4911, 48877733, 12580154)
    ]

    #download the data for each station
    for elem in stations:
        station_id = elem.station_id
        download_id(station_id)

    for elem in stations:
        station_id = elem.station_id
        data = read_data(station_id,['TMK','SDK','RSK'])
        xdata, ydata = prepare_data_days(data,range_= 1, keyindex = 0, days = 3)
        elem.model = learn(xdata,ydata)

    #we want the same random numbers ervery time we execute
    random.seed(5)
    TMK = [random.uniform(10,25)  for i in range(21)]
    SDK = [random.gauss(6,1)  for i in range(21)]#Sonnenscheindauer so ca 6h pro tag
    RSK = [random.choice([abs(random.gauss(20,10)), 0, 0 ])  for i in range(21)]#wenn es regnet, dann richtig

    j=0
    for elem in stations:
        pred_data = []
        for i in range(j,j+3):
            pred_data.append(TMK[i])
            pred_data.append(SDK[i])
            pred_data.append(RSK[i])
        pred_data = np.reshape(np.array(pred_data),(1,9))
        print(pred_data.shape)
        #pred_data = [ TMK[i],SDK[i],RSK[i] for i in range(j,j+3) ]
        #print(pred_data)
        elem.prediction = elem.model.predict(pred_data)
        print(elem.prediction)
        j += 3

    return 0

get_city_models()





