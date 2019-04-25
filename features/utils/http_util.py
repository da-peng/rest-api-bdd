# encoding=utf-8

import requests, json


class HttpUtils(object):

    def __init__(self):
        pass

    def post(self, request_body, url):
        print('\n')
        print('* ' * 5 + 'POST' + ' *' * 5)
        request_body = json.dumps(request_body, ensure_ascii=False)
        print('* ' * 5 + 'REQUEST_body' + ' *' * 5)
        print(request_body)

        response = requests.post(url, json=request_body)
        print('')
        print('* ' * 5 + 'RESPONSE' + ' *' * 5)
        print(response.text)
