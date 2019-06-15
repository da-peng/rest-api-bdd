#encoding=utf-8
import redis

host = '172.16.30.116'
port=6389
db = 1
password = "xgaiastzbiut5eghfma7f9s9"
re = redis.Redis(host=host,port=port,db=db,password=password)

re.keys(pattern=u'*')