#encoding=utf-8
import  re

def path_join(path,tenant_code):
    path_list = re.split('{|}', path)
    path_list[1] = tenant_code
    path = ''.join(path_list)
    return path


if __name__=='__main__':
    path='/marketing/{tenant_code}/activity-group/create'
    tenant_code='lqx'
    print(path_join(path,tenant_code))