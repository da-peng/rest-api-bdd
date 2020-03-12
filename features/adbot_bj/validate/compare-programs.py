#encoding=utf-8
from utils.db_connect import DbConnect
from utils.log_manage import Log as log
import os
import csv
project_path = os.path.abspath(os.path.dirname(__file__)).split('adbot_bj')[0]
test_data = 'adbot_bj/test-data'

def readfile(file_name,column):
    with open(os.path.join(project_path, test_data, file_name + '.csv')) as fp:
        csv_read = csv.reader(fp)
        count = 0
        values =[]
        index = 0
        for i in csv_read:
            if count ==0:
                index = i.index(column)
            else:
                if index!= 0:
                    values.append(i[index])
            count+=1


def compareData(db_name,table_name,column,values):
    connect = DbConnect(db_name)
    sql = "SELECT * FROM {0} WHERE {1} in {2}".format(table_name,column,values)
    ret = connect.query(sql)

    connect.close()


if __name__ =='__main__':
    pass