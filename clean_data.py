import csv
import numpy as np
import string
import pandas as pd
import math

# all_2019data = pd.read_csv('data_player/2018_fulldata.csv')
# data_2018 = all2018_data.iloc[0:451,:]                   # 读到第451行，下面隔一行保存
# print(data_2018)
# data_2018.to_csv('data_player/data_2018.csv',index=False)      # index = false 是表示不保存index的意思

##############################################################################
##############################################################################


##############################################################################
###----------------  part 3: 自己写的function 读数据并保存 ----------------------

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


use_pandas_readdata('2019_fulldata', 450, 'data_2019')

data_2019 = pd.read_csv('data_player/data_2019.csv')
print(data_2019.columns.tolist())  # 查看column 的名字，放一个列表里

# 查看这个叫 'Club logo'的这列
### 这一行这个 club logo 名字不可用，需要加一个下划线，不然rdf 没法识别
data_2019.rename(columns={'Club Logo':'Club_Logo'},inplace = True)
data_2019.rename(columns={'Release Clause': 'Release_Clause'}, inplace=True)
data_2019.to_csv('data_player/data_2019.csv', index=False)

##############################################################################
##############################################################################


########################################################################
################### work at 3.16  ######################################

#######   下面这一段代码是清洗列数据
'''
####  除掉这个'LWB' columan 中的nan，用0代替
data_2019 = pd.read_csv('data_player/data_2019.csv')

dd = data_2019['LWB'].fillna(0)      
dd_list  = dd.tolist()
def covert_v(item):                     # 对于输入的item 转换成数字
    x = str(item)
    return eval(x)
ll = list(map(covert_v,dd_list))       # 把convert function 和
data_2019['LWB'] = pd.Series(ll)       # 'LWB'这一列等于上买呢修改过
data_2019.to_csv('data_player/data_2019_cleaning.csv', index=True)
clean_data = pd.read_csv('data_player/data_2019_cleaning.csv')
print(clean_data['LWB'])
'''
###############



path = 'data_player/'
path = '/Users/jiayun/PycharmProjects/untitled/untitled/untitled/Github Project/GM_personal_project/data_player/'
def covert_v(item):                     # 对于输入的item 转换成数字
    x = str(item)
    re = int(eval(x))
    return re

def clean_columns(filename,name_list):
    data = pd.read_csv(path + filename + '.csv')
    for item in name_list:
        item_candi = data[item].fillna(0)            # deal with nan, convert nan to 0
        item_list = item_candi.tolist()              # convert to list
        item_replace = list(map(covert_v,item_list))
        data[item] = pd.Series(item_replace)
    data.to_csv(path + filename + '.csv', index=False)
    return


## build a function to clean the needed list

'''
column_list = ['LS','ST','RS','LW','LF']  # 这个list中存着需要clean的 column名
clean_columns('data_2019',column_list)    # 测试一下这function
data_20199 = pd.read_csv(path + 'data_2019' + '.csv')
print(data_20199[['LS','ST','RS','LW','LF']])
# print(data_20199['LS'])
# print(type(data_20199))
'''
## start cleaning
cols_list = data_2019.columns.tolist()  # column names list
needs_cols_list = cols_list[28:-1]
clean_columns('data_2019', needs_cols_list)
cleaning_data_2019 = pd.read_csv(path + 'data_2019' + '.csv')
print(cleaning_data_2019[['LS', 'ST', 'RS', 'LW', 'LF']])
print(cleaning_data_2019.head(20))
print(list(cleaning_data_2019.columns))
