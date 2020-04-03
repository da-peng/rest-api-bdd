import csv
import datetime
import json
import os
import random
import time
from functools import reduce

from utils.csv_manage import CSVManager


class DataFactory(object):
    """
    普通边界条件的测试数据生成工程
    例如：
    int类型是值
    a>=10;a<=20
    b<=10;b<=30
    str类型是日期
    也是值
    日期类型：重现判断

    """

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

    def create_data_flow(self):
        """
        只有在写完所有的字段边界值后，才可以允许此处
        :return:
        """
        # 获取所有手工填写的边界条件
        condition_collections = self.__get_condition_collection()
        print(condition_collections)
        # 根据边界值生成所有可能的数据
        possible_data_collections = self.__generation_normal_data(condition_collections)
        # 穷举生成所有的数据
        test_data = self.get_two_dimension_array_exhaustion(possible_data_collections)
        # 将数据存回指定 _test_data_path
        CSVManager(self._test_data_path).write_by_two_dimension_array(test_data)

    def __write_param_header_and_type(self):
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

    def __get_condition_collection(self):
        """
        解析获取全部字段的边界条件
        :return:
        """
        param_condition = self.get_param_condition()
        condition_collections = []

        for condition in param_condition:
            item = [condition]
            one_field_condition = self.__get_one_field_condition(item)

            if one_field_condition != {}:
                condition_collections.append(one_field_condition)
        return condition_collections

    def __generation_normal_data(self, condition_collections):
        """
        生成 正常数据
        :param condition_collections:
        :return:
        """
        global fake_data
        normal_data_list = []
        # total_rows = self.get_normal_data_collection_min_lines(condition_collection)
        for i in range(len(condition_collections)):
            if self._param_type_list[i] == 'str':
                fake_data = self.__get_normal_data_possible_nums('str', condition_collections[i])
            elif self._param_type_list[i] == 'int':
                fake_data = self.__get_normal_data_possible_nums('int', condition_collections[i])
            normal_data_list.append(fake_data)
        return normal_data_list

    @staticmethod
    def get_normal_data_collection_min_lines(condition_collections):
        """
        计算笛卡尔积组合数
        :param condition_collections:
        :return:
        """
        possible_number_list = []
        for i in range(condition_collections):
            if '=' in i:
                possible_number_list.append(len(i['=']))
            elif '>=' in i or '<=' in i:
                possible_number_list.append(2)
            elif '>=' in i and '<=' in i:
                possible_number_list.append(3)
            elif '>' in i or '<' in i:
                possible_number_list.append(2)
            elif '>' in i and '<' in i:
                possible_number_list.append(3)
        cartesian_nums = reduce(lambda x, y: x * y, possible_number_list)
        return cartesian_nums

    def __get_normal_data_possible_nums(self, types, condition):
        """
        根据约束条件获取，多有字段可能有的所有的正常 边界值
        :param types:
        :param condition:
        :return:
        """
        result = []
        data = []
        if '=' in condition:
            result.extend(condition['='])
        elif '>' in condition and '<' in condition:
            n_min = condition['>']
            n_max = condition['<']
            if self.is_valid_date(n_min):
                data = [self.get_one_day_later(n_min),
                        self.get_random_date(n_min, n_max, '%Y-%m-%d'),
                        self.get_one_day_early(n_max)]
            elif self.is_valid_date_time(n_min):
                data = [self.get_one_hour_later(n_min),
                        self.get_random_date(n_min, n_max, '%Y-%m-%d %H:%M:%S'),
                        self.get_one_hour_early(n_max)]
            elif types == 'str':
                nums = random.randint(int(n_min), int(n_max))
                data = [self.get_random_string(int(n_min + 1)), self.get_random_string(nums),
                        self.get_random_string(int(n_max - 1))]
            else:
                data = [int(n_min) + 1, random.randint(int(n_min), int(n_max)), int(n_max) - 1]
        elif '<=' in condition and '>=' in condition:
            n_min = condition['>=']
            n_max = condition['<=']
            if self.is_valid_date(n_min):
                data = [n_min, self.get_random_date(n_min, n_max, '%Y-%m-%d'), n_max]
            elif self.is_valid_date_time(n_min):
                data = [n_min, self.get_random_date(n_min, n_max, '%Y-%m-%d %H:%M:%S'), n_max]
            elif types == 'str':
                nums = random.randint(int(n_min), int(n_max))
                data = [self.get_random_string(int(n_min)), self.get_random_string(nums),
                        self.get_random_string(int(n_max))]
            else:
                data = [int(n_min), random.randint(int(n_min), int(n_max)), int(n_max)]

        if '>' in condition and '<' not in condition:
            n_min = condition['>']
            if self.is_valid_date(n_min):
                data = [self.get_one_day_later(n_min)]
            elif self.is_valid_date_time(n_min):
                data = [self.get_one_hour_later(n_min)]
            elif types == 'str':
                data = [self.get_random_string(int(n_min) + 2), self.get_random_string(int(n_min) + 1)]
            else:
                data = [int(n_min) + 1, int(n_min) + 2]
        elif '<' in condition and '>' not in condition:
            n_max = condition['<']

            if self.is_valid_date(n_max):
                data = [self.get_one_day_early(n_max)]
            elif self.is_valid_date_time(n_max):
                data = [self.get_one_hour_early(n_max)]
            elif types == 'str':
                data = [self.get_random_string(int(n_max) - 2), self.get_random_string(int(n_max) - 1)]
            else:
                data = [int(n_max) - 1, int(n_max) - 2]
        elif '>=' in condition and '<=' not in condition:
            n_min = condition['>=']

            if self.is_valid_date(n_min):
                data = [n_min, self.get_one_day_later(n_min)]
            elif self.is_valid_date_time(n_min):
                data = [n_min, self.get_one_hour_later(n_min)]
            elif types == 'str':
                data = [self.get_random_string(int(n_min) + 1), self.get_random_string(int(n_min))]
            else:
                data = [int(n_min) + 1, int(n_min)]
        elif '<=' in condition and '>=' not in condition:
            n_max = condition['<=']

            if self.is_valid_date(n_max):
                data = [n_max, self.get_one_day_early(n_max)]
            elif self.is_valid_date_time(n_max):
                data = [n_max, self.get_one_hour_early(n_max)]
            elif types == 'str':
                data = [self.get_random_string(int(n_max) - 1), self.get_random_string(int(n_max))]
            else:
                data = [int(n_max) - 1, int(n_max)]
        result.extend(data)
        return result

    def __get_one_field_condition(self, conditions=[], i=1, result=None):
        """
        获取一个字段边界值条件
        :param result:
        :param i: 最终输出 边界条件 字典 '=' 可能是多个 只是 ;= <= ;>= ; > ; <
        :param conditions:
        :return:
        """
        if result is None:
            result = {'=': []}
        collection = []

        for condition in conditions:
            if ';' in condition:
                collection.extend(condition.split(';'))

            elif '>' in condition:
                ret = condition.split('>')
                ret.remove('')
                if '=' not in ret[0]:
                    result['>'] = ret[0]
                else:
                    result['>='] = ret[0].replace('=', '')
            elif '<' in condition:
                ret = condition.split('<')
                ret.remove('')
                if '=' not in ret[0]:
                    result['<'] = ret[0]
                else:
                    result['<='] = ret[0].replace('=', '')
            elif '=' in condition:
                ret = condition.replace('=' * condition.count('='), '=').split('=')
                ret.remove('')
                if ret[0] != '':
                    result['='].append(ret[0])
            else:
                if condition != '':
                    result['='].append(condition)

        if i >= 2:
            if result['='] == []:
                result.pop('=')
            return result
        else:
            # collection 搜集所有的条件
            return self.__get_one_field_condition(collection, i + 1, result)

    def __generate_type_error_data(self, types, length):
        if types == 'str':
            value = self.get_random_int(length)
        elif types == 'int':
            value = self.get_random_string(length)
        return value

    @staticmethod
    def is_valid_date(strs):
        """
        判断是否是一个有效的日期字符串
        """
        try:
            time.strptime(strs, "%Y-%m-%d")
            return True
        except Exception as e:
            return False

    @staticmethod
    def is_valid_date_time(strs):
        """
        判断是否是一个有效的日期字符串
        """
        try:
            time.strptime(strs, "%Y-%m-%d %H:%M:%S")
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_one_day_later(date, fmt="%Y-%m-%d"):
        date_time = datetime.datetime.strptime(date, fmt) + datetime.timedelta(days=1)
        return date_time.strftime(fmt)

    @staticmethod
    def get_one_hour_later(date_time, fmt="%Y-%m-%d %H:%M:%S"):
        new_date_time = datetime.datetime.strptime(date_time, fmt) + datetime.timedelta(hours=1)
        return new_date_time.strftime(fmt)

    @staticmethod
    def get_one_day_early(date, fmt="%Y-%m-%d"):
        date_time = datetime.datetime.strptime(date, fmt) + datetime.timedelta(days=-1)
        return date_time.strftime(fmt)

    @staticmethod
    def get_one_hour_early(date_time, fmt="%Y-%m-%d %H:%M:%S"):
        new_date_time = datetime.datetime.strptime(date_time, fmt) + datetime.timedelta(hours=-1)
        return new_date_time.strftime(fmt)

    @staticmethod
    def get_random_date(start, end, fmt="%Y-%m-%d %H:%M:%S"):
        s_time = time.mktime(time.strptime(start, fmt))
        etime = time.mktime(time.strptime(end, fmt))
        ret = int(random.random() * (etime - s_time) + s_time)
        return time.strftime(fmt, time.localtime(ret))

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

    @staticmethod
    def get_two_dimension_array_exhaustion(input_list=None):
        """
        二维数组正交穷举方法
        :param input_list:
        :return:
        """
        if input_list is None:
            input_list = [[]]
        result = input_list[:1]  # [[1,2,3]]
        # print(result)
        for i in range(1, len(input_list)):  # 1
            temp = []
            for num in input_list[i]:  # 5 /6
                res = []
                for k in result:  # [1,2,3]
                    s = []
                    if i >= 2:
                        s.extend(k)  # 1
                    else:
                        for j in k:  # 1
                            s = []
                            s.append(j)  # 1
                    s.append(num)  # 5[1,5]
                    res.append(s)  # [1,5]
                temp += res
            result = temp
        return result


if __name__ == '__main__':
    # print(DataInfo.get_random_string(100))
    testDataFile = '/Users/grabby/PyCharm_Project/rest-api-bdd/features/adbot_bj/test-data'
    sampleDataFile = '/Users/grabby/PyCharm_Project/rest-api-bdd/features/adbot_bj/request-params'
    # TestData()
    dataInfo = DataInfo('card-orders', {'testDataFile': testDataFile, 'sampleDataFile': sampleDataFile})
    # print(dataInfo.generate_type_error_data('str', 2))
    # print(dataInfo.generate_correct_data())
    # condition_collection = dataInfo
    # print(condition_collection)
    # array = dataInfo.__generation_normal_data(condition_collection)
    dataInfo.create_data_flow()




# 前面2个进行正交，结果再跟后面的进行正交

# input_list = [[1, 2, 3], [5, 6], [7, 8, 9], [10, 11]]


# dataFactory.write_param_header_and_type()

# {'=': ['200', '100', '1000'], 'value': ['100', '200', '300', '500'], '>=': '200', '<=': '100', '<': '100',
# '>': '200'}
# print([i for i in range(3)])
# print([i for i in range(1, 3)])
# print(dataInfo.get_random_date('2012-12-31', '2013-1-20', '%Y-%m-%d'))
# print(dataInfo.get_one_day_early('2012-12-31'))
