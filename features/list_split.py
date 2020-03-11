# encoding=utf-8

list = [x for x in range(24)]

print(list)



def iter(list):
    for i in range(len(list)):
        for j in range(i,len(list)-1):
            if j in list[i]:
                list[i].remove(j)
            
        
        # start = l1[0]
        # end = l1[len(l1)]
        # if start in list[i]:
        #     i = list[i].index[start]
        #
        # elif end in list[i]:
        #     j = list[i].index[end]



if __name__ == '__main__':
    l1 = [5,6]
    l2 =[x for x in range(6,24)]
    print(l2)
    l3 = [x for x in range(8)]
    rules = []
    rules.append(l1)
    rules.append(l2)
    rules.append(l3)
    print(l3)
    print(rules)
    # iters(rules)
