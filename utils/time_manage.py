#encoding=utf-8
import time
import random
from datetime import datetime, timedelta, timezone

a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
global start
start = time.mktime(a1)    #生成开始时间戳

if __name__ =='__main__':
    print(start)
    a1 = (1976, 1, 2, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    end = time.mktime(a1)  # 生成开始时间戳
    print(end)
    print(end-start)
    print()

def getRandomTime():
    start += 1*24*60*60
    date_touple = time.localtime(start)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    return date

def getCurrentDateTime():
    # 拿到UTC时间，并强制设置时区为UTC+0:00:
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    # astimezone()将转换时区为北京时间:
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    return bj_dt

def getCurrentTime():

    return getCurrentDateTime().strftime("%Y-%m-%d %H:%M:%S")

def sleep():
    time.sleep(1)

def getEndTime():
    return (getCurrentDateTime() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")


def get_time_stamp():
    ct = time.time()
    local_time = getCurrentDateTime()
    # data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_head = local_time.strftime("%M-%S")
    data_secs = str(ct)[-3:]
    time_stamp = "%s.%s" % (data_head, data_secs)
    return time_stamp


# if __name__ =='__main__':
#     print(getCurrentTime())
#     print(getEndTime())
#     print(get_time_stamp())