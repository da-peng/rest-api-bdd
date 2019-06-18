# encoding=utf-8
import mysqlx
import mysql.connector
from utils.log_manage import Log as log

# session = mysqlx.get_session('mysqlx://root:@localhost:33060/my_schema')
# my_schema = session.get_default_schema()
# assert my_test_schema.get_name() == 'my_schema'
class DbConnect(object):
    def __init__(self, db_name):
        try:
            self.conn = mysql.connector.connect(
                host='172.16.30.116',
                port=3306,
                user='amily',
                password='amily.mysql.com',
                database=db_name
            )

        except Exception as e:
            log.error("Error while connecting to MySQL:{0}".format(e))

    def query(self, sql):
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.cur.close()
        return res

    def update(self, sql):
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.cur.close()

    def close(self):
        if self.conn.is_connected():
            self.conn.close()

    class MySqlXConnect(object):
        def __init__(self, schema):
            try:
                self.session = mysqlx.get_session({
                    'host': '172.16.30.116',
                    'port': 3306,
                    'user': 'amily',
                    'password': 'amily.mysql.com',
                    'schema': schema
                })
            except Exception as e:
                log.error("Error while connecting to MySQL:{0}".format(e))

        def query(self, sql):
            res = self.session.sql(sql).execute().fetch_all()
            self.session.close()
            return res

        def getCollection(self, table_name, ):
            collection = self.session.get_default_schema() \
                .get_collection(table_name)
            # Specify which document to find with Collection.find()
            # result = collection.find('name like :param').bind('param', 'S%').limit(1).execute()
            return collection
            # docs = result.fetch_all()
            # Print document
            # print('Name: {0}'.format(docs[0]['name']))

        def close(self):

            self.session.close()

    # The connected server does not have the MySQL X protocol plugin enabled or protocol mismatch


if __name__ == '__main__':

    # 活动商品
    db_name = 'uat_msa_marketing'
    connect = DbConnect(db_name)
    activity_res = connect.query("SELECT DISTINCT b.activity_id,c.product_id,c.sku_id "
                        "FROM "
                        "(SELECT activity_id,product_id FROM(SELECT id,activity_name FROM activity_group WHERE activity_end_time > now( )) "
                        "AS a LEFT JOIN activity_product ON a.id = activity_id) "
                        "AS b LEFT JOIN activity_product_sku AS c ON b.product_id = c.product_id")
    for activity_id, product_id,sku_id in activity_res:
        print('activity_id:{0},product_id:{1},sku_id:{2}'.format(activity_id,product_id,sku_id))
    # print('{0}'.format(res[0]))
    connect.close()

    # 商品
    # db_name = 'uat_msa_store'
    #
    # connect = DbConnect(db_name)
    #
    # product_res = connect.query("SELECT product_id,sku_code FROM product_sku WHERE tenant_code = 'baiyang'")
    # for product_id,sku_code in product_res:
    #     print('product_id:{0},sku_code:{1}'.format(product_id,sku_code))
    # connect.close()
    #
