import os
from DAY6.bin import initAll
import prettytable
import time
def cleanPrint():
    try:
        os.system('cls')
    except:
        os.system('clear')
def fight(hero,master):
    '''
    英雄与怪物互相攻击
    :param hero:
    :param master:
    :return:
    '''
    #英雄攻击
    yingxiongshanghai = hero.attack()
    #怪物受到伤害
    master.getHurt(yingxiongshanghai)
    if master.isDeath:
        return
    #怪物攻击
    guaiwushanghai = master.attack()
    #英雄受到伤害
    hero.getHurt(guaiwushanghai)

def matchMaster(hero,master):
    cleanPrint
    #互相攻击直到一方死亡
    #叫两下
    master.tell()
    while not hero.isDeath or  master.isDeath:
        fight(hero,master)
        if master.isDeath or  hero.isDeath:
            break

    #怪物死亡，获得奖励
    if master.isDeath:
        guaiwumoney = master.dropMoney()
        print('怪物掉落了金钱：%s'%guaiwumoney)
        guaiwuThings = master.dropThings
        print('怪物掉落了物品：',guaiwuThings.name)
        hero.getExperience(master.experience)
        hero.getThings(guaiwuThings)
        #根据掉落物品的类型放入背包
        wupinzidian = {'武器':hero.pack.getWeapon,'防具':hero.pack.getArmor,'食物':hero.pack.getfood}
        packgetType = wupinzidian[guaiwuThings.attribute]
        packgetType(guaiwuThings)
        hero.pack.getMoney(guaiwumoney)
        print('获得金钱%s'%guaiwumoney)
        print('获得%s'%guaiwuThings.name)
        hero.levelUp()
        #作弊，让英雄生命增加
       # hero.health = 10000
        return 'masterIsDeath'
    #英雄死亡
    if  hero.isDeath:
       # hero.health = 10000
        return 'heroIsDeath'








if __name__ == '__main__':
    hero = initAll.iniHero('测试英雄')
    mapTown = initAll.initTown()
    # masterMapList = [('轻松秒杀的地图',1,5),('普通的怪物地图',2,5),('强悍的怪物地图',3,5),
    #             ('低级BOSS',4,1),('高级BOSS',5,1)]
    masterMap = initAll.iniMasterMap(0)
    #masterMap = map('轻松秒杀的地图',1,5)
    for i in masterMap.master.keys():
        cleanPrint()
        masterMap.tell()
        if not i.isDeath:
            cleanPrint()
            print('遭遇怪物...!')
            masterMap.tell()
            time.sleep(0.5)
            master = i
            matchMaster(hero,master)
    print('怪物清除完成...')