import csv
import numpy as np
import string
import pandas as pd

data_path = 'data_player/'
file_name = 'data_2019'
data = pd.read_csv(data_path + file_name + '.csv')
print(list(data.columns))
sp = data['ShotPower']
print(data['ShotPower'])
print(data['ST'])
