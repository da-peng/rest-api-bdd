from utils.db_connect import DbConnect

#返回的格式为[(32,0)]

def kol_id(db_name,mobile):
    connect=DbConnect(db_name)
    kolid=connect.query("select kol_id from kol_account WHERE mobile="+mobile+"")
    connect.close()

    return kolid[0][0]


def account_id(db_name,mobile):
    connect = DbConnect(db_name)
    accountid=connect.query("select account_id from kol_account_approval_record WHERE mobile= "+mobile+"")
    connect.close()

    return accountid[0][0]
def id(db_name,mobile):
    connect = DbConnect(db_name)
    id=connect.query("select id from kol_account WHERE mobile="+mobile+"")
    connect.close()

    return id[0][0]



if __name__=='__main__':
    print(account_id('adbot_kol_business','18819077367'))

