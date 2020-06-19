import csv

def read_data(station_id, keys = ['MESS_DATUM','TMK','SDK']):
    """
    input a list of keywords to get list of data provided from a file 'daten.txt'
    expects:
        keys: list consisting of elements like the following
            'MESS_DATUM' Messdatum format YYYYMMDD
            'FX' Tagesmaximum Windspitze in m/s
            'FM' Tagesmittel Windgeschwindigkeit in m/s
            'QN_4' Qualitätsniveau der nachfolgenden Spalten
            'RSK' tägliche Niederschlagshöhe in mm
            'RSKF' Niederschlagsform
            'SDK' tägliche Sonnenscheindauer in h
            'SHK_TAG' Tageswert Schneehöhe in cm
            'NM' Tagesmittel des Bedeckungsgrades in 1/8 ?
            'VPM' Tagesmittel des Dampfdruckes in hPa
            'PM' Tagesmittel des Luftdrucks in hPa
            'TMK' Tagesmittel der Temperatur in °C
            'UPM' Tagesmittel der Relativen Feuchte in %
            'TXK' Tagesmaximum der Lufttemperatur 2m Höhe in °C
            'TNK' Tagesminimum der Lufttemperatur 2m Höhe in °C
            'TGK' Minimum der Lufttemperatur am Erdboden 5cm Höhe in °C
            
        station_id: ID of the weather station
    """

    #station id has to have 5 digits
    station_id= str(station_id)
    while (len(station_id)<5) : station_id = "0" + station_id

    data = []
    with open(f'daten_{station_id}.txt') as f:
        reader = csv.DictReader(f, delimiter = ';',skipinitialspace=True)
        i=0
        for row in reader:
            data.append([])
            for key in keys:
                data[i].append(row[key])
            i += 1
    return data


data = read_data(4104)
print(data[-1])
