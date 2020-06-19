from zipfile import ZipFile
import os

def create_datafile(zipname):
    """
    creating the daten.txt file from the downloaded zipfile
    """
    ids = zipname.split('_')
    date0 = ids[3]
    date1 = ids[4]
    station_ID = ids[2]
    filename = f'produkt_klima_tag_{date0}_{date1}_{station_ID}.txt'

    archive = ZipFile(zipname, 'r')#open zip-file
    data = archive.extract(filename)#extract file with data
    archive.close()
    #check if daten.txt already exists and remove it
    for elem in os.listdir(os.getcwd()):
        if elem == f'daten_{station_ID}.txt':
            os.remove(f'daten_{station_ID}.txt')
        #remove the zip file
        elif elem == zipname:
            os.remove(zipname)
            
    os.rename(filename, f'daten_{station_ID}.txt')#rename file to daten.txt


create_datafile('tageswerte_KL_04104_18790101_20191231_hist.zip')
