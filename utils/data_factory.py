import csv
import json
import os
import random
import re


class DataFactory(object):
    def __init__(self):
        pass


class DataInfo(object):
    """
    1.  生成字段/类型的csv文件
    2.  手动在第三行输入字段 边界条件
    3.  生成 异常 测试数据
    4.  加入 自定义 数据生成的条件 Todo
    """

    def __init__(self, api_name, config):
        """
            {
            'dataPath':'',
            'samplePath':'',
            }
            :param config:
            :return:
        """
        # 测试数据文件生成地址
        self._api_name = api_name
        self._test_data_path = os.path.join(config['testDataFile'], api_name + '.csv')
        # 打开 请求示例 数据 默认是json文件结尾
        self._sample_data_path = os.path.join(config['sampleDataFile'], api_name + '.json')
        if self._sample_data_path.endswith('.json'):
            with open(self._sample_data_path, 'r') as fp:
                sample_data = json.loads(fp.read())
        param_header_list = list(sample_data.keys())
        param_type_list = []

        for i in range(len(param_header_list)):
            value = sample_data[param_header_list[i]]
            if isinstance(value, str):
                param_type_list.append('str')
            elif isinstance(value, int):
                param_type_list.append('int')
        self._param_header_list = param_header_list
        self._param_type_list = param_type_list

    def write_param_header_and_type(self):
        # 如果生成的测试数据文件不存在，则创建这个文件；
        # 第一行为字段名称
        # 第二行为字段类型

        # 加入预期 结果/实际请求响应信息statusMessage
        param_header_list = self._param_header_list
        param_header_list.append('预期结果')
        param_header_list.append('实际结果')
        param_header_list = ['原始字段:'] + param_header_list
        param_type_list = ['字段类型:'] + self._param_type_list

        if not os.path.exists(self._test_data_path):
            with open(self._test_data_path, 'w') as fp:
                csv_write = csv.writer(fp)
                csv_write.writerow(param_header_list)
                csv_write.writerow(param_type_list)
                csv_write.writerow(['字段边界条件:'])

    def get_param_condition(self):

        """
        第三行是 字段边界值条件,去掉第一个cell头
        :return:
        """

        return self.get_one_line(2)[1:]

    def get_one_line(self, n_rows):
        with open(self._test_data_path, 'r') as fp:
            reader = csv.reader(fp)
            lines = [i for i in reader]
        return lines[n_rows]

    def get_param_type(self):
        return self._param_type_list

    def get_param_header(self):
        return self._param_header_list

    def generate_correct_data(self):
        param_condition = self.get_param_condition()
        for condition in param_condition:
            pass

    def result_collection(self, conditions, i=1, result={'=': [], 'value': []}):
        '''
        :param i:
        :param conditions:
        :return:
        '''
        collection = []
        for condition in conditions:
            if ';' in condition:
                collection.extend(condition.split(';'))
            elif '>' in condition:
                ret = condition.split('>')
                ret.remove('')
                collection.extend(ret)
                if '=' not in ret[0]:
                    result['>'] = ret[0]
                else:
                    result['>='] = ret[0].replace('=', '')
            elif '<' in condition:
                ret = condition.split('<')
                ret.remove('')
                collection.extend(ret)
                if '=' not in ret[0]:
                    result['<'] = ret[0]
                else:
                    result['<='] = ret[0].replace('=', '')
            elif '=' in condition:
                ret = condition.replace('='*condition.count('='), '=').split('=')
                ret.remove('')
                collection.extend(ret)
                if ret[0] != '':
                    result['='].append(ret[0])
            else:
                if condition != '':
                    result['value'].append(condition)
        if i >= 2:
            return result
        else:
            return self.result_collection(collection, i + 1, result)

    def generate_type_error_data(self, types, length):
        if types == 'str':
            value = self.get_random_int(length)
        elif types == 'int':
            value = self.get_random_string(length)
        return value

    @staticmethod
    def get_random_string(length):
        random_string_list = map(lambda x: chr(random.randint(65, 90)), [i for i in range(length)])
        return ''.join(random_string_list)

    @staticmethod
    def get_random_int(length):
        if length > 1:
            return random.randint(1, 10)
        else:
            return 10 ** (length - 1) + random.randint(1, 10 * (length - 1) - 1)


class DataCondition(object):

    def __init__(self):
        # if not os.path.exists(self._test_data_path):
        #     with open(self._test_data_path, 'w') as fp:
        #         csv_write = csv.writer(fp)
        pass

    def write_expect_result(self):
        pass

    def type_error_data(self):
        """
        数据类型错误
        本来str 传int
        本来int 传str
        :return:
        """
        pass

    def null_error_data(self):
        """
        字段依次为空
        :return:
        """

        pass

    def required_error_data(self):
        """
        必填项不填
        :return:
        """
        pass

    def scope_error_data(self, retMsg):
        """
        超出数据指定范围
        a<0
        1<a<10
        1<a=<100
        :return:
        """
        pass


if __name__ == '__main__':
    # print(DataInfo.get_random_string(100))
    testDataFile = '/Users/grabby/PyCharm_Project/rest-api-bdd/features/adbot_bj/test-data'
    sampleDataFile = '/Users/grabby/PyCharm_Project/rest-api-bdd/features/adbot_bj/request-params'
    # TestData()
    dataInfo = DataInfo('card-orders', {'testDataFile': testDataFile, 'sampleDataFile': sampleDataFile})
    print(dataInfo.generate_type_error_data('str', 2))
    # print(dataInfo.generate_correct_data())
    print(dataInfo.result_collection(['100;200;300;;500;>=200;<=100;<100;>200;=200;=100;=;====1000']))
    # dataFactory.write_param_header_and_type()
