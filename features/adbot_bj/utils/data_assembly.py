# encoding=utf-8
import os
import json

request_params = 'adbot_bj/request-params/'
test_data = 'adbot_bj/test-data'
project_path = os.path.abspath(os.path.dirname(__file__)).split('adbot_bj')[0]


def assembly_data(file_name):
    test_data_path = os.path.join(project_path, test_data, file_name)
    request_params_path = os.path.join(project_path, request_params, file_name + '.json')
    with open(request_params_path, 'r') as fp:
        content = fp.read()
        # print(content, type(content))
    params = json.loads(content)
    with open(test_data_path, 'r') as fp:
        test_data_lines = fp.readlines()
    data_list = []
    for i in test_data_lines:
        request_data = jsonData(i, params)
        data_list.append(request_data)
    # print(data_list)
    return data_list


def jsonData(test_data, params):
    if isinstance(test_data, str) and isinstance(params, dict):
        keys = list(params.keys())
        # print(keys)
        data_items = test_data.strip('\n').split(';')
        # print(data_items)
        # print(keys[1])
        if len(data_items) == len(params):
            for i in range(len(keys)):
                if isinstance(params[keys[i]],str):
                    params[keys[i]] = data_items[i]
                else:
                    params[keys[i]] = int(data_items[i])

    return params


if __name__ == '__main__':
    # print(os.path.abspath(os.path.dirname(__file__)).split('adbot_bj')[0])
    # print(os.path.join(project_path,test-data,'file_name'))
    print(assembly_data('channel-groupon-refund-orders'))
