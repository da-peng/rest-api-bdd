#encoding=utf-8
import time
from datetime import datetime, timedelta, timezone


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
    local_time = getCurrentTime()
    # data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_head = time.strftime("%M-%S", local_time)
    data_secs = str(ct)[-3:]
    time_stamp = "%s.%s" % (data_head, data_secs)
    return time_stamp


if __name__ =='__main__':
    print(getCurrentTime())
    print(getEndTime())