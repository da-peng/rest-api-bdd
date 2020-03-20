from utils.db_connect import DbConnect

# 返回的格式为[(32,0)]

db_name = 'adbot_kol_business'


def kol_id(mobile):
    connect = DbConnect(db_name)
    kol_id = connect.query("select kol_id from kol_account WHERE mobile=" + mobile + "")
    connect.close()
    return kol_id[0][0]


def account_id(mobile):
    connect = DbConnect(db_name)
    account_id = connect.query("select account_id from kol_account_approval_record WHERE mobile= " + mobile + "")
    connect.close()

    return account_id[0][0]


def id(mobile):
    connect = DbConnect(db_name)
    id = connect.query("select id from kol_account WHERE mobile=" + mobile + "")
    connect.close()

    return id[0][0]


if __name__ == '__main__':
    print(account_id( '18819077367'))
