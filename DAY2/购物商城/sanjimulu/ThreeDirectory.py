#!/usr/bin/python
#encoding: utf-8
'''
作业1： 三级目录
'''
from cityData import cityData
#----------一级目录----------------
def levlOne(cityData = cityData):
    """
    入参cityData 为城市字典
    出参levloneList 返回一级城市列表
    """
    print("""--------------------------------
    欢迎进入城市查询系统！
    ------------------------------------
    当前可查询以下城市：
    q 退出""")
    levloneList = []
    for x in cityData:
        #获取一级城市列表
        levloneList.append(x)
    for i in levloneList:
        print(levloneList.index(i),i )
    return levloneList

#-----------------二级目录------------------
def levlTwo(levloneList,levlOneNum):
    """
    入参levloneList 一级城市列表
    入参levlOneNum 用户选择的城市序号
    出参levlTwoList 返回二级城市列表
    """
    if int(levlOneNum) <= len(levloneList)-1:
        print("""--------------------------------
    欢迎进入城市查询系统！
    ------------------------------------
    %s市下有以下区域：
    b 返回
    q 退出"""%(levloneList[int(levlOneNum)]))
        levlTwoInfo = cityData[levloneList[int(levlOneNum)]]
        levlTwoList = []
        for x in levlTwoInfo:
            levlTwoList.append(x)
        for i in levlTwoList:
            print(levlTwoList.index(i),i )
        return levlTwoList

#-----------------三级目录-----------------
def levlThird(levlTwoList,levlTwoNum,levloneList):
    """
    入参
    levlTwoList 二级城市列表
    levlTwoNum  用户选择的二级城市序号
    levloneList 一级城市列表
    出参
    当用户选择的城市序号存在时返回True
    """
    if int(levlTwoNum) <= len(levlTwoList)-1:
        print("""--------------------------------
    欢迎进入城市查询系统！
    ------------------------------------
    %s下有以下区域：
    b 返回
    q 退出"""%(levlTwoList[int(levlTwoNum)]))
        levlTwoInfo = cityData[levloneList[int(levlOneNum)]]
        levlThirdList = levlTwoInfo[levlTwoList[int(levlTwoNum)]]
        for i in levlThirdList:
            print(levlThirdList.index(i),i )
        return True

#程序开始
whileContinue = True
while whileContinue:
    #获取第一级菜单
    levloneList = levlOne()
    levlOneNum = input("请选择要查询的城市(输入quit退出程序)：")
    #判断退出循环的条件
    if levlOneNum == "q":
        whileContinue = False
        continue
    #如果用户输入的是数字即进入下一层
    elif levlOneNum.isnumeric():
        while whileContinue:
            levlTwoList = levlTwo(levloneList,levlOneNum)
            #当用户在上一层中输入的数字过大时，函数返回None，需要用户重新输入
            if levlTwoList == None:
                break
            levlTwoNum = input("请选择要查询的城市：")
            if levlTwoNum == "b":
                break
            elif levlTwoNum == "q":
                whileContinue = False
                continue
            #如果用户输入的是数字即进入下一层
            elif levlTwoNum.isnumeric():
                while whileContinue:
                    levlThirdList = levlThird(levlTwoList,levlTwoNum,levloneList)
                    #当用户在上一层中输入的数字过大时，函数返回None，需要用户重新输入
                    if levlThirdList == None:
                        break
                    levlThirdNum = input("请选择要查询的城市：")
                    if levlThirdNum == "b":
                        break
                    elif levlThirdNum == "q":
                        whileContinue = False
                        continue
                    #用户输入其他则在本层继续循环
                    else:
                        continue