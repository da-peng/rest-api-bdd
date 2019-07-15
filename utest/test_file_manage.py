# encoding=utf-8
from utils.file_manage import *

class TestFileManage(object):
    def test_read(self):
        assert  read() is not None

    def test_add(self):
        assert add({'a':'1'}) is None

    def test_write(self):
        assert  write('a') is None