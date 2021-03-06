import requests 
import os 
from zipfile import ZipFile

def get_name(station_id,url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"):
    """
    geting the name of the zip file from the dwd
    expects: 
        station_id must be integer 
        url (optional) if zip lies somewhere else then the default path of the dwd
    """
    if isinstance(station_id,int) != True : raise TypeError ("station_id must be of type integer")

    #get text from url 
    html = requests.get(url).text  
    html = str(html)
    
    #convert station_id so it is of length 5 in order to fit the required format 
    station_id= str(station_id)
    while (len(station_id)<5) : station_id = "0" + station_id
    
    #searching for the given station_id 
    station_id=f"_KL_{station_id}"
    station_id_found = html.find(station_id)
    if station_id_found == -1: raise Exception ("station_id not found")
    
    #returning the whole filename 
    return ("tageswerte" + station_id + html[station_id_found + 9 : station_id_found + 36])
    
def get_file(name, url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"): 
    """
    downloading file from dwd server and saving it in wd 
    expects: 
        name must be string
        url (optional, string) if zip lies somewhere else then the default path of the dwd
    
    """
    if isinstance(name,str) != True : raise TypeError("name must be of type string")

    response = requests.get(url + name, stream=True)
    handle = open(name, "wb")
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    handle.close()

def create_datafile(zipname):
    """
    creating the daten.txt file from the downloaded zipfile
    expects: 
        zipname must be string
    """
    if isinstance(zipname,str) != True : raise TypeError("zipname must be of type string")

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


def download_id(station_id,url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"): 
    """
    downlaoding and creating data file for given id 
    expects: 
        station_id must be integer 
        url (optional) if zip lies somewhere else then the default path of the dwd
    """
    
    if isinstance(station_id,int) != True : raise TypeError ("station_id must be of type integer")
    
    #geting the name of the corresponding zip file 
    name = get_name(station_id, url) 

    #downloading the zip file 
    print("--- downloading file ",name," ---")
    get_file(name, url)
    
    #creating data file
    print("--- creating data file for previous zip file ---")
    create_datafile(name)
    

if __name__ == "__main__":    
    
    download_id(4104)
