from get_data import *
from read_data import read_data
import numpy as np 
from train_prev_days import * 
from validation import *
import random
import matplotlib.pyplot as plt 
from scipy.interpolate import interp2d

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
    locations('Regensburg', 4104, 49.013430, 12.101634),
    locations('Parsberg', 3875, 49.1603469, 11.7187275),
    locations('Schwandorf', 4592, 49.319888, 12.109135),
    locations('Schorndorf-Knöbling', 4559, 49.160155, 12.591019),
    locations('Elsendorf-Horneck', 7075, 48.708826, 11.809827),
    locations('Mallersdorf-Pfaffenberg', 3147, 48.769303, 12.227654),
    locations('Straubing', 4911, 48.877733, 12.580154)
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

    
    
    
    # prepare data for plotting and  
    longitude = [] 
    altitude = [] 
    predictions = [] 
    citys = [] 
    for elem in stations: 
        longitude.append(elem.longitude) # x values 
        altitude.append(elem.altitude) # y valuess
        predictions.append(elem.prediction) # z values
        citys.append(elem.city) # name for scatter 
        
    
        
    fig, axs = plt.subplots() 
    axs.scatter(altitude, longitude)
    for i, city in enumerate(citys): 
        axs.annotate(city, (longitude[i], altitude[i]))
    
    plt.show()
    
    return 0 

get_city_models()





