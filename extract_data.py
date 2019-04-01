import csv
import numpy as np
import string
import pandas as pd

data_path = 'data_player/'
file_name = 'data_2019'
data = pd.read_csv(data_path + file_name + '.csv')
# print(list(data.columns))
sp = data['ShotPower']
# print(data['ShotPower'])
# print(data['ST'])

pos = data['Position'].tolist()
pos = set(pos)
# print(pos)

## try to find the index 'RB' in raw data
data_col = list(data.columns)
print(len(data_col))
for i in range(len(data_col)):
    item = data_col[i]
    if item == 'RB':
        print(i)
        break
    else:
        continue

data_col_dict = enumerate(data_col)

extract_data = data.iloc[:, 54:88]
extract_data2 = data.iloc[0:451, 54:88]

# ability index is col+54
a_data = np.array(extract_data2)
# print(a_data)

##---------------------- convert wage to number ---------------------
hypo_a_data = data['Wage']
target_list = data['Wage'].tolist()


def replace_money_symbol(item):
    item = item.replace('€', '')
    item = item.replace('K', '')
    re = int(eval(item)) * 1000
    return re


hypo_a_data = list(map(replace_money_symbol, hypo_a_data))
##---------------------- convert wage to number end ---------------------


nd_hypo_a_data = np.array(hypo_a_data).reshape(450, 1)
# print(nd_hypo_a_data.shape)
final_data = np.concatenate((a_data, nd_hypo_a_data), axis=1)
### here fina_data is the data for analysing


### extract needed data, save to csv file
data.rename(columns={'Release_Clause': 'p_wage'}, inplace=True)
data['p_wage'] = pd.Series(hypo_a_data)
# data.iloc[:, 54:89].to_csv(data_path + 'extracted_data.csv', index=False)
data.iloc[:, 54:89].to_csv('extracted_data.csv', index=False)

data = pd.read_csv('extracted_data.csv')
print(list(data.columns))
print(data.shape)
