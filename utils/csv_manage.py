# encoding=utf-8

import os
import csv


class CSVManager(object):
    def __init__(self, path):
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self._path = os.path.join(current_path, path)

    def read(self):
        with open(self._path, 'r') as fp:
            reader = csv.reader(fp)
            # rows=list(reader)
            rows = [row for row in reader]
            return rows

    def write(self, *data):
        with open(self._path, 'w+') as fp:
            csv_writer = csv.writer(fp)
            for i in data:
                csv_writer.writerow(i)

    def add(self, *data):
        context = len(self.read())
        with open(self._path, 'a+') as fp:
            csv_writer = csv.writer(fp)
            count = 0
            for i in data:
                if context != 0 and count >=1:
                    csv_writer.writerow(i)
                count += 1


if __name__ == '__main__':
    fp = CSVManager('utils' + 'data.csv')
    data = (['token', 'wechatSessionKey', 'wechatAccountId'], [1, 2, 3])
    fp.write(data)
