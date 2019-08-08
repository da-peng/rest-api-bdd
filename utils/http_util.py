# encoding=utf-8

import requests, json
from utils.log_manage import Log as log
from utils.file_manage import read


class HttpUtils(object):

    def __init__(self):
        pass

    # def option(self,re):

    def getToken(self, key):
        table = read()
        token = table[key]
        log.debug('{0}角色，Token:{1}'.format(key, token))
        return token

    def postByToken(self, request_body, url, key):
        log.debug(url)
        log.debug('POST')
        request_bodys = json.dumps(request_body)
        log.debug('REQUEST_body')
        log.debug(request_bodys)
        token = self.getToken(key)
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
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        request = requests.Request('POST', url, headers=headers, data=request_body)
        prepared = request.prepare()

        log.debug(prepared.method)
        log.debug(prepared.url)
        log.debug(prepared.body)
        s = requests.Session()
        response = s.send(prepared)
        log.debug('RESPONSE')
        log.debug(response.text)
        return response

    def form_get(self, request_params, url):
        # request_body = json.dumps(request_body, separators=(',', ':'),ensure_ascii=False)
        # request_bodys = json.loads(request_body, encoding="GB2312")

        # log.debug(json.dumps(request_params))

        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        request = requests.Request('GET', url, headers=headers, params=request_params)
        prepared = request.prepare()

        log.debug(prepared.method)
        log.debug(prepared.url)
        s = requests.Session()
        response = s.send(prepared)
        log.debug('RESPONSE')
        log.debug(response.text)

        return response


if __name__ == '__main__':
    print(read())
