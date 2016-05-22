import random
#from  things import *
from DAY6.conf.things import *


def randomArmor():
    random1 = random.randint(2,100)%2
    random2 = random.randint(2,100)%2
    thingsLeveTemp = ['普通的','优秀的','神圣的']
    nametemp = ['上衣','裤子','内裤','袜子']
    name = thingsLeveTemp[random2] +  nametemp[random1]
    thingsLevel = thingsLeveTemp[random2]
    if thingsLevel == '普通的':
        defense = random.randint(3,40)
        price = defense * 5
    if thingsLevel == '优秀的':
        defense = random.randint(40,80)
        price = defense * 5
    if thingsLevel == '神圣的':
        defense = random.randint(80,120)
        price = defense * 5
    a = armor(name,price,defense,thingsLevel)
    return a
def randomFood():
    random1 = random.randint(2,100)%2
    random2 = random.randint(2,100)%2
    thingsLeveTemp = ['普通的','优秀的','神圣的']
    nametemp = ['包子','营养快线','啤酒','鸡腿']
    name = thingsLeveTemp[random2] +  nametemp[random1]
    thingsLevel = thingsLeveTemp[random2]
    if thingsLevel == '普通的':
        restroes = random.randint(70,120)
        price = restroes * 5
    if thingsLevel == '优秀的':
        restroes = random.randint(300,500)
        price = restroes * 5
    if thingsLevel == '神圣的':
        restroes = random.randint(80,120)
        price = restroes * 5
    a = food(name,price,restroes,thingsLevel)
    return a
def randomWeapon():
    """

    :rtype: object
    """
    random1 = random.randint(2,100)%2
    random2 = random.randint(2,100)%2
    thingsLeveTemp = ['普通的','优秀的','神圣的']
    nametemp = ['小刀','长枪','弓箭','板砖']
    name = thingsLeveTemp[random2] +  nametemp[random1]
    thingsLevel = thingsLeveTemp[random2]
    if thingsLevel == '普通的':
        minDamage = random.randint(70,120)
        maxDamage = minDamage + random.randint(1,100)
        price = minDamage * 5
    if thingsLevel == '优秀的':
        minDamage = random.randint(200,320)
        maxDamage = minDamage + random.randint(1,150)
        price = minDamage * 5
    if thingsLevel == '神圣的':
        minDamage = random.randint(500,1200)
        maxDamage = minDamage + random.randint(1,300)
        price = minDamage * 5
    a = weapon(name,price,minDamage,maxDamage,thingsLevel)
    return a
if __name__ == '__main__':
    a = randomFood()
    print(a.tell())