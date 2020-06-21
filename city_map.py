from get_data import *
from read_data import read_data
import numpy as np 
from train_prev_days import * 
from validation import *
import random
import matplotlib.pyplot as plt 
from scipy.interpolate import Rbf

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
    example: creating predictions for some citys
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

    #create the model for each station 
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
        elem.prediction = elem.model.predict(pred_data)
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
    
    
    fig, ax = plt.subplots() 
    #interpolate points
    f = Rbf (longitude, altitude, predictions)

    x = np.linspace(min(longitude) - 0.1 , max(longitude) + 0.1, 100)
    y = np.linspace(min(altitude) - 0.1, max(altitude) + 0.1, 100)
    x,y = np.meshgrid(x,y)
    znew = f(x,y)

    #creating heatmap
    c = ax.pcolormesh(x,y, znew, cmap='coolwarm', vmin=min(predictions), vmax=max(predictions))
    ax.set_title('Temperature Prediction')
    fig.colorbar(c, ax=ax)

    #Adding Citys with names to the plot 
    ax.scatter(longitude, altitude)
    for i, city in enumerate(citys): 
        ax.annotate(city, (longitude[i], altitude[i]))
    
    plt.show()
    
    return 0 

get_city_models()





