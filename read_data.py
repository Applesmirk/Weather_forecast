import csv


data = {}
with open('daten.txt') as f:
    reader = csv.DictReader(f, delimiter = ';',skipinitialspace=True)
    for row in reader:
        date = row['MESS_DATUM'] #YYYYMMDD
        max_temp = row['TXK']  #2m über boden
        sonnenscheindauer = row['SDK'] #in stunden
        data[date] = max_temp,sonnenscheindauer
        
print(data)
