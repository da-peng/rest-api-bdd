# encoding=utf-8
from utils.config_parser import config
import csv

import pickle, os
from utils.log_manage import Log as log
current_path = os.path.dirname(os.path.dirname(__file__))

common_config_path = '/conf/common/env.ini'

msa_path = config(common_config_path)['store.file.path']['PATH']

path = current_path + '/adbot.csv'


# 读
# def read():
#     with open(path, 'rb') as fp:
#         size = len(fp.read())
#         # 这里文件读取后会游标移动 还原到最开始位置
#         fp.seek(0)
#         if size==0:
#             isNone = True
#             return -2
#         else:
#             table = pickle.load(fp)
#             return table
def read():

    with open(path, 'r') as fp:
        reader = csv.reader(fp)
        #rows=list(reader)
        rows=[row for row in reader]
        return rows



# 覆盖
#def write(data):
#     with open(path, 'wb') as fp:
#         pickle.dump(data, fp)
#         log.debug('持久化储存数据成功')
def write(data1,data2):
    with open(path, 'w') as fp:
        csv_writer=csv.writer(fp)
        csv_writer.writerow(data1)
        csv_writer.writerow(data2)
        log.debug('持久化储存数据成功')


# 追加
# def add(dict_data):
#     data = {}
#     table = None
#     isNone = False
#     with open(path, 'rb') as fp:
#         size = len(fp.read())
#         # 这里文件读取后会游标移动 还原到最开始位置
#         fp.seek(0)
#         if size==0:
#             isNone = True
#         else:
#             table = pickle.load(fp)
#     with open(path, 'wb') as fp:
#         if  isNone:
#             for i in dict_data.keys():
#                 # request-params[i] = []
#                 data[i]=dict_data[i]
#             # print(request-params)
#             pickle.dump(data, fp)
#         elif isinstance(table,dict): # value 是一个List
#             for i in dict_data.keys():
#                 # if i  not in table.keys():
#                 #     table[i] = []
#                 table[i]=dict_data[i]#  往list append后面加
#             # print(table)
#             pickle.dump(table, fp)
#         log.debug('持久化储存数据成功')
def add(data1,data2):
    with open(path, 'a+') as fp:
        csv_writer=csv.writer(fp)
        csv_writer.writerow(data1)
        csv_writer.writerow(data2)

if __name__ == '__main__':
    # write({'a': 1})


    print(read())


    #print(type(read()[1][0]))
