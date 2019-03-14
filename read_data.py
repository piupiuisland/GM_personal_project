import csv

###-------------- first part: use csv load and save data -----------------------------
# read data
def read_data(file_name,lines):
    file_path = 'data_player/'
    file = file_path + file_name
    needed_data = []
    with open(file,'r') as csvfile:
        r = csv.reader(csvfile,delimiter=',')
        # for row in r:
        for row in r:
            needed_data.append(row)
            if len(needed_data) == lines:      # 一旦行数到了lines这个行数，就停止了，不接着写入了
                break
    return needed_data

# save data
def save_data(data,file_name):
    file_path = 'data_player/'
    with open(file_path +file_name+'.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:                           # 把每个子列表写入 csvfile
            writer.writerow(item)
    return

file_1 = '2017_fulldata.csv'
data_2017 = read_data(file_1,401)
print(data_2017[0])
print(data_2017[1])
print(data_2017[400])
print(len(data_2017[0]))
print(len(data_2017[1]))
print(len(data_2017[2]))
print(len(data_2017))
# save_data(data_2017,'data_2017')
file_2 = '2019_fulldata.csv'
data_2019 = read_data(file_2,21)
print(data_2019[0])
print(len(data_2019[0]))

###-------------- second part: use pandas load and save data -----------------------------

import pandas as pd

# all2018_data = pd.read_csv('data_player/2018_fulldata.csv')
# data_2018 = all2018_data.iloc[0:451,:]
# print(data_2018)
# data_2018.to_csv('data_player/data_2018.csv',index=False)      # index = false 是表示不保存index的意思
#
# import pandas as pd
#
# def use_pandas_readdata(filename,lines,savename):
#     path = 'data_player/'
#     filepath = path + filename +'.csv'
#     all_data = pd.read_csv(filepath)
#     needed_data = all_data.iloc[0:lines,:]
#     savepath = path + savename + '.csv'
#     needed_data.to_csv(savepath,index=False)
#     return
#
# use_pandas_readdata('2019_fulldata',451,'data_2019')
# use_pandas_readdata('2017_fulldata',451,'data_2017')

data_2019 = pd.read_csv('data_player/data_2019.csv')
# print(data_2019.head(20))
# print(data_2019['Club Logo'])
data_2019.rename(columns={'Club Logo':'Club_Logo'},inplace = True)
print(data_2019['Club_Logo'])
# data_2019.to_csv('data_player/data_2019.csv',index=False)
print(data_2019['RCM'])