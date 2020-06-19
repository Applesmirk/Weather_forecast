import csv
import numpy as np
from datetime import timedelta, date

def read_data(station_id, keys = ['MESS_DATUM','TMK','SDK'],check = False):
    """
    input a list of keywords to get list of data provided from a file 'daten.txt'
    expects:
        station_id: ID of the weather station
        keys: (optional)
            list consisting of elements like the following
          * 'MESS_DATUM' Messdatum format YYYYMMDD
            'FX' Tagesmaximum Windspitze in m/s
            'FM' Tagesmittel Windgeschwindigkeit in m/s
            'QN_4' Qualitätsniveau der nachfolgenden Spalten
            'RSK' tägliche Niederschlagshöhe in mm
            'RSKF' Niederschlagsform
          * 'SDK' tägliche Sonnenscheindauer in h
            'SHK_TAG' Tageswert Schneehöhe in cm
            'NM' Tagesmittel des Bedeckungsgrades in 1/8 ?
            'VPM' Tagesmittel des Dampfdruckes in hPa
            'PM' Tagesmittel des Luftdrucks in hPa
          * 'TMK' Tagesmittel der Temperatur in °C
            'UPM' Tagesmittel der Relativen Feuchte in %
            'TXK' Tagesmaximum der Lufttemperatur 2m Höhe in °C
            'TNK' Tagesminimum der Lufttemperatur 2m Höhe in °C
            'TGK' Minimum der Lufttemperatur am Erdboden 5cm Höhe in °C
        check: True/False(*) if you want to check if all dates are in the data set    
        
        *default
    """
    if isinstance(station_id,int) != True : raise TypeError ("station_id must be of type integer")
   
    print("--- reading data from file ---")
    #station id has to have 5 digits
    station_id= str(station_id)
    while (len(station_id)<5) : station_id = "0" + station_id

    data = []
    with open(f'daten_{station_id}.txt') as f:
        reader = csv.DictReader(f, delimiter = ';',skipinitialspace=True)
        for key in keys: 
            if key not in reader.fieldnames: raise ValueError("unknown key")

        i=0
        for row in reader:
            data.append([])
            for key in keys:
                data[i].append(row[key])
            i += 1
    if check: check_data(data)
    return np.array(data)

#returning every date inbetween two dates
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

    
def check_data(data):
    
    #converting data to only consist of the dates
    data = np.array(data)
    data = data[:, 0]
    
    #getting start and end date
    start = data[0]
    end = data[-1]
    start = date(int(start[0:4]), int(start[4:6]), int(start[6:8]))
    end = date(int(end[0:4]), int(end[4:6]), int(end[6:8]))
    
    #creating list of dates inbetween start and end 
    compare_dates= []
    for dt in daterange(start, end):
        compare_dates.append(dt.strftime("%Y%m%d"))
    
    #checking if every date in the data set is in the date list
    for dt in data: 
        if dt not in compare_dates: print("ERROR date:",dt, "missing")
    
    
if __name__ == "__Main__": 
    data = read_data(4104)
    print(data[-1])
    

    
