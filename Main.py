from get_data import *
from read_data import read_data
import numpy as np 
from train_prev_days import * 

station_id = 4104
download_id(station_id)
data = read_data(station_id)

prepare_data_days(data)
