import csv

def get_data(keys,station_id):
    """
    input a list of keywords to get list of data provided from a file 'daten.txt'
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

#test for 
#'MESS_DATUM' date of measurement 
#'TMK' daily mean temperature
data = get_data(['MESS_DATUM','TMK'],4104)
print(data[-1])
