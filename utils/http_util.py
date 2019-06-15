# encoding=utf-8

import requests, json
from utils.log_manage import Log as log
from utils.file_manage import read

class HttpUtils(object):

    def __init__(self):
        pass
    # def option(self,re):

    def getToken(self):
        table = read()
        return table['token']

    def postByToken(self,request_body, url):
        log.debug(url)
        log.debug('POST')
        request_bodys = json.dumps(request_body)
        log.debug('REQUEST_body')
        log.debug(request_bodys)
        token = self.getToken()
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "token": token
        }
        response = requests.post(url, headers=headers, json=request_body)
        log.debug('RESPONSE')
        log.debug(response.text)
        response = json.loads(response.text)
        return response

    def post(self, request_body, url):
        log.debug(url)
        log.debug('POST')
        # 允许ascii 显示中文
        # dict 转json str对象
        request_bodys = json.dumps(request_body)

        log.debug('REQUEST_body')
        log.debug(request_bodys)

        headers = {
            "content-type": "application/json;charset=UTF-8"
        }
        response = requests.post(url, headers=headers, json=request_body)
        log.debug('RESPONSE')
        log.debug(response.text)
        response = json.loads(response.text)
        return response


    def form_post(self, request_body, url):
        log.debug('POST')
        # request_body = json.dumps(request_body, separators=(',', ':'),ensure_ascii=False)
        # request_bodys = json.loads(request_body, encoding="GB2312")
        log.debug('REQUEST_body')
        log.debug(request_body)

        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, headers=headers, data=request_body)
        log.debug('RESPONSE')
        log.debug(response.text)
        log.debug(response.apparent_encoding)
        return response


if __name__ == '__main__':
    print(read())