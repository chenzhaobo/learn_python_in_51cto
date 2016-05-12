import os


def getPagination(showInfoDict, showPerPage=10):
    """
    输入需要分页的字典，列表返回字典的分页。
    :param showInfoDict:需要分页的字典
    :param showPerPage:每页展示的数量
    :return PaginationList:列表[分页1，分页2，...]
    :return keysOfPaginationList:字典{页数：该页下的字典键值}：{"1"：(第一页所存的keys)，....}
    """
    PaginationList = []
    keysOfPaginationList = {}
    keys = list(showInfoDict.keys())
    lenOfDict = len(showInfoDict)
    pageTemp = lenOfDict.__divmod__(showPerPage)
    if pageTemp[1] == 0:
        page = pageTemp[0]
    else:
        page = pageTemp[0] + 1

    for a in range(page + 1):
        if (a + 1) * 10 > len(keys):
            keysPerPage = keys[(a - 1) * 10:]
        else:
            keysPerPage = keys[a * 10:(a + 1) * 10]
        goodsListInfo = ""
        for x in keysPerPage:
            goodsName = x
            if showInfoDict[goodsName].get("price"):
                goodsPrice = showInfoDict[x]["price"]
                goodsAmount = showInfoDict[x]["amount"]
            else:
                goodsPrice = " "
                goodsAmount = " "
            goodsListInfo1 = "|" + str(goodsName).center(20, " ") + "|" + str(goodsPrice).center(20, " ") + "|" + str(
                goodsAmount).center(20, " ") + "|" + "\n"
            goodsListInfo += goodsListInfo1
            # print(goodsListInfo)
        PaginationList.append(goodsListInfo)
        # print(PaginationList)
        keysOfPaginationList[str(a)] = tuple(keysPerPage)

    return PaginationList, keysOfPaginationList


def showInfo(listInfo, showType="goods", page=1, AmountOfshoppingCar=0):
    """
    在屏幕上打印信息
    :param listInfo: 商品信息 list
    :param showType: goods 商品展示，shoppingCar 购物车
    :param page: 显示的页数
    :param AmountOfshoppingCar: 购物车的总金额
    :return getInput: 获取用户的选择
    """
    try:
        os.system("cls")
    except:
        os.system("clear")
    str1 = "_" * 84 + "\n"
    str3 = '|{0}|{1}|{2}|'.format('商品名称'.center(20, " "), "价格".center(20, " "), "数量".center(20, " ")) + "\n"
    str4 = listInfo[page - 1]
    str6 = "共{0}页，当前显示第{1}页信息。".format(len(listInfo), page).ljust(84, " ")
    if showType == "goods":
        str2 = "\n" + "商品展示".center(82, " ") + "\n"
        str5 = str1 + str2 + str3 + str4 + str6
        print(str5)
        getInput = input('请选择菜单 ：输入商品编号 | 购物车(c) | 余额充值(r) | 结帐(b) | 退出(q)| 翻页(n+页码数)|购买历史(h) : ')
    elif showType == "shoppingCar":
        str2 = "\n" + "购物车".center(82, " ") + "\n"
        str7 = "购物车总额：{0}元\n".format(round(AmountOfshoppingCar), 2).ljust(84, " ")
        str5 = str1 + str2 + str3 + str4 + str7 + str6
        print(str5)
        getInput = input('请选择菜单 ：输入商品编号修改 | 主菜单(c) | 余额充值(r) | 结帐(b) | 退出(q)| 翻页(n+页码数)|购买历史(h) \n清空购物车(delall) : ')
    elif showType == "buyHistory":
        str2 = "\n" + "已购商品".center(82, " ") + "\n"
        str5 = str1 + str2 + str3 + str4 + str6
        print(str5)
        getInput = input('请选择菜单 ： 购物车(c) | 退出(q)| 翻页(n+页码数): ')
    return getInput.strip()


def initGoods():
    """
    初始化商品数据
    :return:
    """
    import random
    goodsDict = {}
    for i in range(36):
        str1 = "产品类" + str(i + 1)
        goodsDict[str1] = {}
    for x in goodsDict.keys():
        for y in range(35):
            gname = x + "-商品" + str(y)
            # if goodsDict[x].get(gname):
            #     goodsDict[x][gname] = {"price":round(random.uniform(0,2000),2),"amount":int(random.uniform(0,200))}
            # else:
            #     goodsDict[x] = {gname:{"price":round(random.uniform(0,2000),2),"amount":int(random.uniform(0,200))}}
            goodsDict[x][gname] = {"price": round(random.uniform(0, 2000), 2), "amount": int(random.uniform(0, 200))}
    return goodsDict


def updateShoppingCar(userName, goodsName=None, price=None, amount=None, shoppingCarDict={}):
    """
    更新购物车
    :param userName: 用户名
    :param goodsName: 商品名称
    :param price: 商品价格
    :param amount: 商品数量
    :return:
    """
    if amount:
        amount = round(amount, 2)
    if shoppingCarDict.get(userName):
        if shoppingCarDict[userName].get(goodsName):
            shoppingCarDict[userName][goodsName] = {"price": price, "amount": amount}
        else:
            shoppingCarDict[userName] = {goodsName: {"price": price, "amount": amount}}
    else:
        shoppingCarDict[userName] = {goodsName: {"price": price, "amount": amount}}
    return shoppingCarDict


def getAmountOfshoppingCar(userName, shoppingCarDict):
    """
    获取购物车总额
    :param userName: 用户名
    :param shoppingCarDict: 保存购物车信息的字典
    :return: 购物车总额
    """
    amount = 0
    for x in shoppingCarDict[userName]:
        if x != None:
            a = shoppingCarDict[userName][x]["price"]
            b = shoppingCarDict[userName][x]["amount"]
            amount = amount + a * b
    return round(amount, 2)


def updateAmountOfGoods(goodsName, goodsAmount, goodsDict, updateType="+"):
    """
    更新商品库存信息
    :param goodsName: 商品名称
    :param goodsAmount: 商品库存数量
    :param goodsDict:原始商品信息字典
    :param updateType: 更新类型
    :return: 更新后的商品信息字典
    """
    for x in goodsDict:
        for y in x:
            if y == goodsName:
                if updateType == "+":
                    x[y] += goodsAmount
                elif updateType == "-":
                    x[y] -= goodsAmount
    return goodsDict


def userInfo(userName, userMoney=100000):
    return userMoney


def buyHistory(userName, goodsName=None, price=None, amount=None, buyHistory={}):
    """
    更新购物历史信息
    :param userName: 用户名
    :param goodsName: 商品名称
    :param price: 商品价格
    :param amount: 商品数量
    :return:
    """
    if amount:
        amount = round(amount, 2)
    if buyHistory.get(userName):
        if buyHistory[userName].get(goodsName):
            buyHistory[userName][goodsName] = {"price": price, "amount": amount}
        else:
            buyHistory[userName] = {goodsName: {"price": price, "amount": amount}}
    else:
        buyHistory[userName] = {goodsName: {"price": price, "amount": amount}}
    return buyHistory


def rfillMoney(userMoney):
    while 1:
        try:
            rfillMoney = int(input("请输入充值的金额:"))
            break
        except:
            print("你的输入有误！\n")
            continue
    userMoney += rfillMoney
    print("充值完成！")
    return userMoney


userName = "zb"
# 开始
# 初始化商品信息
goodsDict = initGoods()
print(goodsDict)
# 初始化购物车信息
shoppingCarDict = updateShoppingCar(userName)
# 商品信息中间变量
goodsDictTemp = goodsDict
# 购买历史
buyHistoryDict = buyHistory(userName)
# 定义初始变量
userMoney = userInfo(userName, userMoney=100000)
showType = "goods"
ifcontinue = 1
PageOfgoods = 1
pageOfshoppingCar = 1
page = PageOfgoods
while ifcontinue:
    # 获取商品分页信息,打印信息的列表，与之对应的关系字典
    PaginationListOfgoodsDict, keysOfPaginationListOfgoodsDict = getPagination(goodsDictTemp)
    # 获取购物车分页信息,打印信息的列表，与之对应的关系字典
    PaginationListOfshoppingCar, keysOfPaginationListOfshoppingCar = getPagination(shoppingCarDict)
    # 获取购买历史信息分页信息,打印信息的列表，与之对应的关系字典
    PaginationListOfbuyHistoryDict, keysOfPaginationListOfbuyHistoryDict = getPagination(buyHistoryDict)
    # 购物车金额
    AmountOfshoppingCar = getAmountOfshoppingCar(userName, shoppingCarDict)
    userChoice = showInfo(PaginationListOfgoodsDict, showType=showType, page=page,
                          AmountOfshoppingCar=AmountOfshoppingCar)
    userChoice = userChoice.strip()
    # 当打印类型为商品展示且数字代表客户选择购物
    if userChoice.isdigit() and showType == "goods":
        if keysOfPaginationListOfgoodsDict.get(userChoice):
            # 判断当前打印信息不为第一层，获取购买数量，更新购物车
            buyGoodsName = keysOfPaginationListOfgoodsDict[userChoice][int(userChoice) - 1]
            if goodsDictTemp[buyGoodsName].get("price"):
                # 获取用户购买的数量
                while 1:
                    try:
                        buyNumber = int(input("请输入你想购买的数量："))
                        break
                    except:
                        print("你的输入有误！\n")
                        continue

                buyGoodsPrice = goodsDictTemp[buyGoodsName]["price"]
                buyGoodsAmount = goodsDictTemp[buyGoodsName]["amount"]
                shoppingCarDict = updateShoppingCar(userName, goodsName=buyGoodsName, price=buyGoodsPrice,
                                                    amount=buyGoodsAmount, shoppingCarDict=shoppingCarDict)
                AmountOfshoppingCar = getAmountOfshoppingCar(userName, shoppingCarDict)
                goodsDict = updateAmountOfGoods(buyGoodsName, buyGoodsAmount, goodsDict, updateType="-")
            # 判断当前显示列表为第一层,则打印用户选择的第二层信息
            else:
                # buyGoodsName = keysOfPaginationListOfgoodsDict[userChoice][int(userChoice)-1]
                goodsDictTemp = goodsDict[buyGoodsName]
                continue
    # 购物车增删
    if userChoice.isdigit() and showType == "shoppingCar":
        if keysOfPaginationListOfshoppingCar.get(userChoice):
            modifName = keysOfPaginationListOfshoppingCar[userChoice][int(userChoice) - 1]
            print("修改商品：%s的信息...\n" % (modifName))
            while 1:
                try:
                    howToDo = int(input("|删除商品(1)|减少数量(2)|增加数量(3)|:"))
                    break
                except:
                    print("你的输入有误！\n")
                    continue
            if howToDo == 1:
                modifAmount = shoppingCarDict[userName][modifName]
                shoppingCarDict.pop(modifName)
                AmountOfshoppingCar = getAmountOfshoppingCar(userName, shoppingCarDict)
                goodsDict = updateAmountOfGoods(modifName, modifAmount, goodsDict, updateType="+")
            elif howToDo == 2:
                while 1:
                    try:
                        howToDo = int(input("请输入需要删除的数量:"))
                        break
                    except:
                        print("你的输入有误！\n")
                        continue
                modifAmount = shoppingCarDict[userName][modifName]
                if howToDo > modifAmount:
                    shoppingCarDict.pop(modifName)
                    AmountOfshoppingCar = getAmountOfshoppingCar(userName, shoppingCarDict)
                    goodsDict = updateAmountOfGoods(modifName, modifAmount, goodsDict, updateType="+")
                else:
                    shoppingCarDict.pop(modifName)
                    AmountOfshoppingCar = getAmountOfshoppingCar(userName, shoppingCarDict)
                    goodsDict = updateAmountOfGoods(modifName, howToDo, goodsDict, updateType="+")
            elif howToDo == 3:
                while 1:
                    try:
                        howToDo = int(input("请输入需要增加的数量:"))
                        break
                    except:
                        print("你的输入有误！\n")
                        continue
                    shoppingCarDict.pop(modifName)
                    AmountOfshoppingCar = getAmountOfshoppingCar(userName, shoppingCarDict)
                    goodsDict = updateAmountOfGoods(modifName, howToDo, goodsDict, updateType="-")
    # 返回
    if userChoice.isalpha() and showType == "shoppingCar":
        if userChoice == "c":
            showType == "goods"
            continue
        if userChoice == "q":
            print("退出商城，由于系统尚未完善，你的购物车信息可能已丢失！\n")
            break
    if userChoice.isalpha() and showType == "goods":
        if userChoice == "c":
            showType == "shoppingCar"
            continue
        if userChoice == "q":
            print("退出商城，由于系统尚未完善，你的购物车信息可能已丢失！\n")
            break
    if userChoice.isalpha() and showType == "buyHistory":
        if userChoice == "c":
            showType == "goods"
            continue
        if userChoice == "q":
            print("退出商城，由于系统尚未完善，你的购物车信息可能已丢失！\n")
            break

    # 翻页
    if "n" in userChoice and userChoice.isalnum():
        if showType == "shoppingCar":
            if userChoice.isdigit and int(userChoice[1:]) < len(keysOfPaginationListOfshoppingCar):
                page = int(userChoice[1:])
                continue
            else:
                page = len(keysOfPaginationListOfshoppingCar)
                continue

        if showType == "goods":
            if userChoice.isdigit and int(userChoice[1:]) < len(keysOfPaginationListOfgoodsDict):
                page = int(userChoice[1:])
                continue
            else:
                page = len(keysOfPaginationListOfgoodsDict)
                continue
    # 结帐
    if "b" == userChoice:
        print("正在计算...\n")
        if AmountOfshoppingCar <= userMoney:
            print("购物车中商品已成功购买！\n")
            shoppingCarDict = updateShoppingCar(userName)
            for x in shoppingCarDict[userName]:
                buyHistoryName = x
                buyHistoryPrice = x["price"]
                buyHistoryAmount = x["amount"]
                buyHistoryDict = buyHistory(userName, goodsName=buyHistoryName, price=buyHistoryPrice,
                                            amount=buyHistoryAmount)
        else:
            print("余额不足，请充值....")
            userMoney = rfillMoney(userMoney)
            continue
    if "r" == userChoice:
        userMoney = rfillMoney(userMoney)
        continue
    if "h" == userChoice:
        showType == "buyHistory"
        continue
