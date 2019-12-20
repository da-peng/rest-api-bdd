# encoding=utf-8
import os

import requests, json
from utils.log_manage import Log as log


class BaseHttp(object):

    def __init__(self,):
        pass
    # def option(self,re):


    def post(self, request_body, url,header={}):
        log.debug(url)
        log.debug('POST')
        # 允许ascii 显示中文
        # dict 转json str对象
        request_bodys = json.dumps(request_body)

        log.debug('REQUEST_BODY')
        #       log.debug(request_bodys)
        log.debug(json.dumps(json.loads(request_bodys), indent=2, ensure_ascii=False))

        headers = {
            "content-type": "application/json;charset=UTF-8",
            ** header
        }
        log.debug('HEADERS')
        log.debug(json.dumps(headers, indent=2, ensure_ascii=False))

        response = requests.post(url, headers=headers, json=request_body)
        log.debug('RESPONSE')
        log.debug(json.dumps(json.loads(response.text), indent=2, ensure_ascii=False))
        response = json.loads(response.text)
        return response


    def get(self, request_body, url,header={}):
        log.debug(url)
        log.debug('GET')
        # 允许ascii 显示中文
        # dict 转json str对象
        request_bodys = json.dumps(request_body)

        log.debug('REQUEST_BODY')
        #       log.debug(request_bodys)
        log.debug(json.dumps(json.loads(request_bodys), indent=2, ensure_ascii=False))

        headers = {
            "content-type": "application/json;charset=UTF-8",
            ** header
        }
        log.debug('HEADERS')
        log.debug(json.dumps(headers, indent=2, ensure_ascii=False))

        response = requests.get(url, headers=headers, json=request_body)
        log.debug('RESPONSE')
        log.debug(json.dumps(json.loads(response.text), indent=2, ensure_ascii=False))
        response = json.loads(response.text)
        return response


    def form_post(self, request_body, url, header={}):
        # value = self.getConfig(key)
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            **header
        }
        log.debug('HEADERS')
        log.debug(json.dumps(headers, indent=2, ensure_ascii=False))

        request = requests.Request('POST', url, headers=headers, data=request_body)
        prepared = request.prepare()

        log.debug(prepared.method)
        log.debug(prepared.url)
        log.debug(prepared.body)
        s = requests.Session()
        response = s.send(prepared)
        log.debug('RESPONSE')
        log.debug(json.dumps(json.loads(response.text), indent=2, ensure_ascii=False))
        response = json.loads(response.text)
        return response

    def form_get(self, request_params, url, header={}):

        headers = {
            "content-type": "application/x-www-form-urlencoded",
            **header
        }
        log.debug('HEADERS')
        log.debug(json.dumps(headers, indent=2, ensure_ascii=False))

        request = requests.Request('GET', url, headers=headers, params=request_params)
        prepared = request.prepare()

        log.debug(prepared.method)
        log.debug(prepared.url)
        s = requests.Session()
        response = s.send(prepared)
        log.debug('RESPONSE')
        log.debug(json.dumps(json.loads(response.text), indent=2, ensure_ascii=False))
        response = json.loads(response.text)
        return response




if __name__ == '__main__':
    # print(read())
    i ={1:2,2:3,4:6}
    j = {2:2, 3:4,**i}
    print(j)