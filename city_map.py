from get_data import *
from read_data import read_data
import numpy as np 
from train_prev_days import * 

class locations:
    def __init__(self,city,station_id, altitude, longitude):
        self.city = city
        self.station_id = station_id
        self.altitude = altitude
        self.longitude = longitude

stations = [
    locations('Regensburg', 4104, 49013430, 12101634),
    locations('Parsberg', 3875, 491603469, 117187275),
    locations('Schwandorf', 4592, 49319888, 12109135),
    locations('Schorndorf-Knöbling', 4559, 49160155, 12591019),
    locations('Elsendorf-Horneck', 7075, 48708826, 11809827),
    locations('Mallersdorf-Pfaffenberg', 3147, 48769303, 12227654),
    locations('Straubing', 4911, 48877733, 12580154)
]
#stations.append(locations('Regensburg', 4104, 49013430, 12101634))

    #['Regensburg', 4104, 49013430, 12101634]#city, station_id, breitengrad,längengrad
    #['Parsberg', 3875, 491603469, 117187275]
    #['Schwandorf', 4592, 49319888, 12109135]
    #['Schorndorf-Knöbling', 4559, 49160155, 12591019]
    #['Elsendorf-Horneck', 7075, 48708826, 11809827]
    #['Mallersdorf-Pfaffenberg', 3147, 48769303, 12227654]
    #['Straubing', 4911, 48877733, 12580154]


models = []
for elem in stations:
    station_id = elem.station_id
    download_id(station_id)
    data = read_data(station_id,['TMK','SDK','UPM','RSK'])
    xdata, ydata = prepare_data_days(data,range_= 5, keyindex = 0, days = 3)
    models.append(learn(xdata,ydata))
    #print(test(xtest,ytest,model))
#(xtrain,ytrain), (xtest,ytest) = split_data(xdata, ydata, count = 5)

    


