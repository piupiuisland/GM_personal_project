import csv
import numpy as np
import string

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

'''
file_1 = '2017_fulldata.csv'
data_2017 = read_data(file_1,401)
print(data_2017[0])                     # 看第一行
print(data_2017[1])
print(data_2017[400])
print(len(data_2017[0]))
print(len(data_2017[1]))
print(len(data_2017[2]))                 # 看数据有多少列
print(len(data_2017))
# save_data(data_2017,'data_2017')       # 保存文件
'''

file_2 = '2019_fulldata.csv'
data_2019 = read_data(file_2,21)        # 读一下这个文件，读到21行
print(data_2019[0])                     # 把第一行打印一下，因为第一行是colunmn names
print(len(data_2019[0]))

file_1 = '2017_fulldata.csv'
data_2017 = read_data(file_1,51)
save_data(data_2017,'2017dat')



###-------------- second part: use pandas load and save data -----------------------------

import pandas as pd

'''
all2018_data = pd.read_csv('data_player/2018_fulldata.csv')
data_2018 = all2018_data.iloc[0:451,:]
# print(data_2018)
# data_2018.to_csv('data_player/data_2018.csv',index=False)      # index = false 是表示不保存index的意思
'''

import pandas as pd
### 下面这个function是我自己写的  read 并 save， lines是变量第 lines行
def use_pandas_readdata(filename,num_ofLines,savename):
    path = 'data_player/'
    filepath = path + filename +'.csv'
    all_data = pd.read_csv(filepath)
    needed_data = all_data.iloc[0:num_ofLines,:]         # read until num_oflines这行， 写451就是读到451行
    savepath = path + savename + '.csv'
    needed_data.to_csv(savepath,index=False)
    return

use_pandas_readdata('2019_fulldata',451,'data_2019')
use_pandas_readdata('2017_fulldata',451,'data_2017')

data_2019 = pd.read_csv('data_player/data_2019.csv')
print(data_2019.columns.tolist())
# print(data_2019.head(20))
# print(data_2019['Club Logo'])
"""
### 这一行这个 club logo 名字不可用，需要加一个下划线，不然rdf 没法识别
data_2019.rename(columns={'Club Logo':'Club_Logo'},inplace = True)

# print(data_2019['Club_Logo'])        # check whether the 'Club Logo' has been changed
# data_2019.to_csv('data_player/data_2019.csv',index=False)
# print(data_2019['RCM'])

########################################################################
################### work at 3.19  ######################################

#### 下面3句是一起的，但是这个 pd.to_numeric 这个行不通，弄完整个列都是0。。

# print(pd.info(data_2019['LWB']))
# xx = pd.to_numeric(data_2019['LWB'], errors='coerce').fillna(0)
# print(xx)

# print(data_2019.info(data_2019['LWB']))
# data_2019['LWB'].astype(str).astype(int)   # 这个行不通

#### ------------- 上面这5行行不通。。。

# print(data_2019['LWB'])
# def convert_ability(value):
#     # new_value = value.repalce('+','')
#     new_value = value.replace(eval(value))
#     return np.float(new_value)
# data_2019['LWB'].apply(convert_ability)
# list = data_2019['LWB'].tolist()
# print(list)


# def value_convert(column_name):
#     data_list  = data_2019[column_name].tolist()
#
#     for j in data_list:
#         print(type(j))
#     return data_list
# # print(data_list)
# l = value_convert('LWB')


#######   下面这一段代码是清洗列数据
'''
dd = data_2019['LWB'].fillna(0)      # 除掉这个'LWB' columan 中的nan，用0代替
print(dd)

dd_list  = dd.tolist()
def covert_v(item):                     # 对于输入的item 转换成数字
    x = str(item)
    return eval(x)
ll = list(map(covert_v,dd_list))       # 把convert function 和

# data_2019['LWB'] = pd.Series(ll)
# data_2019.to_csv('data_player/data_2019_cleaning.csv',index=True)
clean_data = pd.read_csv('data_player/data_2019_cleaning.csv')
print(clean_data['LWB'])
'''
###############


## build a function to clean the needed list
column_list = ['LS','ST','RS','LW','LF']  # 这个list中存着需要clean的 column名
path = 'data_player/'

def covert_v(item):                     # 对于输入的item 转换成数字
    x = str(item)
    return eval(x)

def clean_columns(filename,name_list):
    data = pd.read_csv(path + filename + '.csv')
    for item in name_list:
        item_candi = data[item].fillna(0)            # deal with nan, convert nan to 0
        item_list = item_candi.tolist()
        item_replace = list(map(covert_v,item_list))
        data[item] = pd.Series(item_replace)
    data.to_csv(path + filename + '.csv')
    return

clean_columns('data_2019',column_list)

data_20199 = pd.read_csv(path + 'data_2019' + '.csv')
print(data_20199[['LS','ST','RS','LW','LF']])           # 同时把这些column 的数据打印出来
# print(data_20199['LS'])
# print(type(data_20199))

"""

data_20199 = pd.read_csv('data_2019_cleaning.csv')
print(data_20199[['LS', 'ST', 'RS', 'LW', 'LF']])
