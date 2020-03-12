# encoding=utf-8
import os

import requests, json
from utils.log_manage import Log as log

request_status = []

class BaseHttp(object):

    def __init__(self, ):
        pass

    # def option(self,re):
    @staticmethod
    def __check_response(response):
        log.debug("RESPONSE STATUS")

        log.debug(str(response.status_code))

        if response.status_code != 200:
            log.error('Request error!')
        log.debug('RESPONSE')
        try:
            log.debug(json.dumps(json.loads(response.text), indent=2, ensure_ascii=False))
        except Exception as e:
            if response.text != '':
                raise Exception("Response Body ContentType is not Json")
            else:
                raise Exception("Response Body is none String")

    def __request_headers(self, header, request_body):
        # map转 str
        request_body = json.dumps(request_body)
        log.debug('REQUEST_BODY')
        #       log.debug(request_body)
        log.debug(json.dumps(json.loads(request_body), indent=2, ensure_ascii=False))
        headers = {
            "content-type": "application/json;charset=UTF-8",
            **header
        }
        log.debug('HEADERS')
        log.debug(json.dumps(headers, indent=2, ensure_ascii=False))
        return headers

    def __form_prepared(self, request):
        prepared = request.prepare()
        log.debug(prepared.method)
        log.debug(prepared.url)
        log.debug('REQUEST_BODY')
        log.debug(str(prepared.body))
        s = requests.Session()
        response = s.send(prepared)
        self.__check_response(response)
        response = json.loads(response.text)
        return response

    def post(self, request_body, url, header={}):
        log.debug(url)
        log.debug('POST')
        # 允许ascii 显示中文
        # dict 转json str对象
        headers = self.__request_headers(header, request_body)
        try:
            response = requests.post(url, headers=headers, json=request_body)
        except Exception as e:
            print('Connection Error %s' %str(e))
            raise  Exception('Connection Error %s' %str(e))
        self.__check_response(response)
        response = json.loads(response.text)
        try:
            statusCode = response['statusCode']
        except Exception as e:
            print(e)

        if statusCode != '20000':
            request_status.append(0)
        else:
            request_status.append(1)
        return response

    def get(self, request_body, url, header={}):
        log.debug(url)
        log.debug('GET')
        # 允许ascii 显示中文
        # dict 转json str对象
        headers = self.__request_headers(header, request_body)

        response = requests.get(url, headers=headers, json=request_body)
        self.check_response(response)

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
        response = self.__form_prepared(request)
        return response

    def form_get(self, request_params, url, header={}):

        headers = {
            "content-type": "application/x-www-form-urlencoded",
            **header
        }
        log.debug('HEADERS')
        log.debug(json.dumps(headers, indent=2, ensure_ascii=False))

        request = requests.Request('GET', url, headers=headers, params=request_params)

        response = self.__form_prepared(request)
        return response


if __name__ == '__main__':
    # print(read())
    i = {1: 2, 2: 3, 4: 6}
    j = {2: 2, 3: 4, **i}
    print(j)
