#encoding=utf-8
import time
import datetime

def getCurrentTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def sleep():
    time.sleep(1)

def getEndTime():
    return (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = str(ct)[-3:]
    time_stamp = "%s.%s" % (data_head, data_secs)
    return time_stamp