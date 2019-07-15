# encoding=utf-8

from utils.time_manage import *
class TestTimeManage(object):

    def test_getCurrentTime(self):
        assert getCurrentTime() is not  None
        assert getEndTime() is not None
        assert get_time_stamp() is not None
