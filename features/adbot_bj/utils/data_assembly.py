# encoding=utf-8
import os
import json

request_params = 'adbot_bj/request-params/'
test_data = 'adbot_bj/test-data'
project_path = os.path.abspath(os.path.dirname(__file__)).split('adbot_bj')[0]
from utils.log_manage import Log as log
import copy
import csv
from utils.time_manage import *
import random


def touchFileByParams(test_data_path, params, size):
    ParamHeader = list(params.keys())
    # keysName=';'.join(keys)+'\n'
    ParamType = []
    if not os.path.exists(test_data_path):
        for i in range(len(ParamHeader)):
            if isinstance(params[ParamHeader[i]], str):
                ParamType.append('str')
            elif isinstance(params[ParamHeader[i]], int):
                ParamType.append('int')
        # lines= []
        # lines.append(keysName)
        # lines.append(';'.join(vlaueType))
        with open(test_data_path, 'w') as fp:
            csv_write = csv.writer(fp)
            csv_write.writerow(ParamHeader)
            csv_write.writerow(ParamType)

            generateTestData(ParamHeader, ParamType, csv_write, size)




def generateTestData(keys, vlaueType, csv_write, size):
    count = 100000
    for i in range(size):
        rowData = []
        for i in range(len(keys)):
            keyName = keys[i].lower()

            if vlaueType[i] == 'str' and 'time' in keyName or 'date' in keyName:
                rowData.append(getRandomTime())
            elif 'citycode' in keyName:
                rowData.append('GuangZhou')
            elif 'brandcode' in keyName:
                rowData.append('awaiting')
            elif 'tenantcode' in keyName:
                rowData.append('ceshi')
            elif 'channelcode' in keyName:
                rowData.append('TEST_CHANNEL')
            elif 'shopcode' in keyName:
                rowData.append(random.randint(1234567, 12345678))
            elif 'shopname' in keyName:
                rowData.append('艾维庭美容纤体SPA(七宝万科广场店)')
            elif 'cityname' in keyName:
                rowData.append('广州')
            elif 'phone' in keyName:
                rowData.append('15013300167')
            elif 'orderstatus' in keyName:
                rowData.append('REFUND')
            elif 'thirdcode' in keyName:
                rowData.append('test' + str(count))
                count += 1
                # print(count)
            elif 'usernickname' in keyName:
                nick = ''
                for i in range(0, 4):
                    b = random.randint(0, 4)
                    if i == b:
                        c = random.randint(1, 9)
                        nick += str(c)
                    else:
                        c = chr(random.randint(65, 90))
                        nick += str(c)
                rowData.append(nick)
            elif 'userid' in keyName:
                rowData.append(random.randint(199999, 19999999))
            elif 'frequency' in keyName:
                rowData.append(random.randint(2, 99))
            elif 'url' in keyName:
                rowData.append('www.ceshi.com')
            elif 'content' in keyName:
                rowData.append('课程名称')
            elif 'address' in keyName:
                rowData.append('测试地址-测试地址')
            elif 'channeldistrictname' in keyName:
                rowData.append('区域名称')
            elif 'id' in keyName:
                rowData.append(random.randint(100000, 2999999))
            else:
                rowData.append(random.randint(19, 1999))
        csv_write.writerow(rowData)


def assembly_data(file_name, size):
    test_data_path = os.path.join(project_path, test_data, file_name + '.csv')
    request_params_path = os.path.join(project_path, request_params, file_name + '.json')

    with open(request_params_path, 'r') as fp:
        content = fp.read()
        # print(content, type(content))
    params = json.loads(content)

    touchFileByParams(test_data_path, params, size)
    data_list = []
    request_bodys = []
    count = 0
    with open(test_data_path, 'r') as fp:
        csv_read = csv.reader(fp)
        test_data_lines = csv_read
        for i in test_data_lines:
            if count >= 2:
                try:
                    request_data = jsonData(i, params)
                    # print(request_data)
                    if request_data != {}:
                        if count % 100 == 0:
                            # print(data_list)
                            request_bodys.append(copy.deepcopy(data_list))
                            data_list = []
                            data_list.append(copy.copy(request_data))
                        else:
                            data_list.append(copy.copy(request_data))
                except Exception as e:
                    log.debug(str(e))
                    continue
            count += 1
        request_bodys.append(copy.deepcopy(data_list))
    return request_bodys


def jsonData(test_data, params):
    if isinstance(test_data, list) and isinstance(params, dict):
        keys = list(params.keys())
        data_items = test_data
        # print(keys[1])
        if len(data_items) == len(params):
            for i in range(len(keys)):
                if isinstance(params[keys[i]], str):
                    params[keys[i]] = data_items[i].strip('').strip('\n')
                else:
                    try:
                        params[keys[i]] = int(data_items[i].strip('').strip('\n'))
                    except Exception as e:
                        raise Exception("数据类型错误，此处应该是数字;字段名称{0}".format(keys[i]))
            return params
        else:
            raise Exception('组装参数长度不一致:\n{0}\n长度:{1} 实际参数长度:{2} ,'
                            .format(data_items, len(data_items), len(params)))


if __name__ == '__main__':
    pass
    # print(os.path.abspath(os.path.dirname(__file__)).split('adbot_bj')[0])
    # print(os.path.join(project_path,test-data,'file_name'))
    print(assembly_data('card-orders', 20))
