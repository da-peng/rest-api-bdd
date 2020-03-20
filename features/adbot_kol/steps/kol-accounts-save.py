from behave import *
import re
from utils.base_http import BaseHttp
from utils.csv_manage import CSVManager
import random
import string
from features.adbot_kol.utils.token_manager import  getLoginInfo

fp = CSVManager('features/adbot_kol/test-data/account.csv')

post = BaseHttp().post


@Given(u'访问kol账号申请接口{path},输入参数{accountLevel},{gender}')
def steps(context, path, accountLevel, gender):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = context.host + ''.join(path_list)

    # 从a-zA-Z0-9生成指定数量的随机字符：
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    accountName = 'test_' + ran_str

    mobile = random.choice(['131', '150', '136']) + str(random.randint(00000000, 99999999))
    wechatAccoutId = getLoginInfo('wechatAccountId')
    request_body = {
        "wechatAccoutId": wechatAccoutId,
        "accountName": accountName,
        "accountLevel": accountLevel,
        "accountSource": 0,
        "mobile": mobile,
        "gender": gender,
        "homepage": "http://www.dianping.com/member/1527027509",
        "cityName": "广州市",
        "commentCount": 0,
        "fansCount": 0,
        "accountLevelImg": "http://www.dianping.com/member/1527027509",
        "accountSourceImg": "http://www.dianping.com/member/1527027509"
    }
    response = post(request_body, path, context.headers)
    context.statusCode = response['statusCode']
    fp.add(['wechatAccoutId', 'mobile'], [wechatAccoutId, mobile])
