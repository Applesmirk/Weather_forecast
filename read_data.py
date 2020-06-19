import csv

def get_data(keys):
    """
    input a list of keywords to get list of data provided from a file 'daten.txt'
    """
    data = []
    with open('daten.txt') as f:
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
data = get_data(['MESS_DATUM','TMK'])

print(data[-1])
