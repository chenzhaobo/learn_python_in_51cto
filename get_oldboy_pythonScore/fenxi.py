import json,prettytable,re
def loadlist():
    with open('result.txt','r') as f:
        for i in f:
            list1 = json.dumps(i)
    list1 = eval(json.loads(list1))
    return list1
def formatAndPrint(list1):
    namelist = ['学号','QQ号','总分']
    for i in list1:
        if len(i) > 2:
            daysNum = len(i[3:])
            break
    for i in range(daysNum):
        namelist.append('day'+str(i+1))
    x = prettytable.PrettyTable(namelist)
    for i in list1:
        if len(i)>2:
            x.add_row(i)
        else:
            for k in range(daysNum-len(i)):
                i.append(' ')
    print(x)
def maoPao(list1,key=None):
    a = len(list1)
    if not key or key == '1':
        key = 0
    elif key == '2':
        key = 2
    maxnum = 0
    #解决qq号没有成绩的BUG
    for i in list1:
        if len(i) > 2:
            daysNum = len(i)
            if daysNum > maxnum or maxnum == 0:
                maxnum = daysNum
    for i in range(len(list1)):
        if len(list1[i])>2 :
            pass
        else:
            for k in range(maxnum-len(list1[i])):
                list1[i].append('0')
    #排序
    for i in range(a):
        for j in range(a-i-1):
            try:
                if int(list1[j][key]) > int(list1[j+1][key]):
                    temp = list1[j+1]
                    list1[j+1] = list1[j]
                    list1[j] = temp
            except :
                print('排序出错，：')
                print('循环次数：list[i] = %s,j=%s,key=%s'%(list1[i],j,key))
                print(list1)
    for i in list1:
        if len(i) != daysNum:
            print(i,daysNum)
    return list1
def reverse(list1):
    return  list1.reverse()
def run(paiXuKey=None,ifReverse=False):
    list1 = loadlist()
    list1 = maoPao(list1,paiXuKey)
    if ifReverse:
         reverse(list1)
    formatAndPrint(list1)
# paiXuKey='2'
# ifReverse = True
# run(paiXuKey,ifReverse)
'''
x = ['A+','A','B+','B','B-','C+','C','C-','D','N/A','COPY','FAIL']
d = {}
for i in list1:
    if len(i) >2:
        d.setdefault(i[0],{})
        d[i[0]].setdefault('qq',i[1])
        for j in x:
            temp = i.count(j)
            d[i[0]].setdefault(j,temp)
k ={}
for i in list1:
    if len(i) >2:
        k.setdefault(int(i[2]),i[0])
keys = list(k.keys())
keys.sort()
for i in keys:
    print('学号:',k[i],'    总分：',i)
'''