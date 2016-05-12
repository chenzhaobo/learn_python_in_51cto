#!/usr/bin/python
'''
作业1：编写的登录接口
1，输入用户名和密码
2，验证成功后显示欢迎信息
3，输错三次后锁定
'''
#用户数据和黑名单数据的路径
userDataPath = "userData.txt"
brackDataPath = "brackdata.txt"
#用户数据和黑名单数据加载到内存中
userDict = {}
brackDict = {}

#------------------------------
#程序开始,初始化所有数据
print("登录小程序正在启动....\n")
print('加载用户名数据...')
userData = open(userDataPath,"r")
for line in userData:
    temp = line.strip().split(',')
    if len(temp)> 1:
        userDict[temp[0]] = temp[1]
userData.close()
print("加载用户数据完成！")
print('加载黑名单数据...')
brackData = open(brackDataPath,"r")
for line in brackData:
    temp = line.strip().split(',')
    if len(temp)> 1:
        brackDict[temp[0]] = int(temp[1])
brackData.close()
print("加载黑名单数据完成！")
#--------------------------------------------------------

#获取用户输入的用户名和密码
ifContinue = True
while ifContinue:
    inputUserName = input("请输入用户名：")
    inputUserPasswd = input("请输入密码：")

    #判断用户名在黑名单中且错误次数大于等于3次,结束本次循环并继续
    if inputUserName in brackDict:
        if brackDict[inputUserName] >= 3:
            print(inputUserName,"用户已被锁定！")
            next = input("输入：q退出程序,输入其他继续程序:")
            if next == "q":
                ifContinue = False
                #退出程序时更新黑名单文件
                brackData = open(brackDataPath,"w")
                for i in brackDict:
                    brackData.write(i+","+str(brackDict[i])+'\n')
                brackData.close()
                print(brackDict)
            continue
    #用户名存在且密码错误次数未超过3次则判断密码是否正确
    if inputUserName in userDict  :
        if inputUserPasswd == userDict[inputUserName] :
            #密码正确登录成功。
            print("你已登录成功！欢迎你",inputUserName)
        else:
            #密码错误，黑名单次数加1
            print("密码错误!")
            if inputUserName in brackDict:
                brackDict[inputUserName] += 1
                #print(brackDict,"黑名单次数加1")
            elif inputUserName not in brackDict:
                brackDict[inputUserName] = 1
                #print(brackDict,"新加黑名单")
    #用户名不存在，提示。
    else:
        print("用户不存在")
    #退出循环的条件
    next = input("输入：q退出程序,输入其他继续程序:")
    if next == "q":
        ifContinue = False
        #退出程序时更新黑名单文件
        brackData = open(brackDataPath,"w")
        for i in brackDict:
            brackData.write(i+","+str(brackDict[i])+'\n')
        brackData.close()
        print(brackDict)