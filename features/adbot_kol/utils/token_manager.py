from utils.csv_manage import CSVManager


def getLoginInfo(key):
    fp = CSVManager('features/adbot_kol/test-data/login.csv')
    keys = fp.read()[0]
    value = fp.read()[1][keys.index(key)]
    return value



def getLoginInfo(key):
    fp = CSVManager('features/adbot_kol/test-data/account.csv')
    keys = fp.read()[0]
    value = fp.read()[1][keys.index(key)]
    return value