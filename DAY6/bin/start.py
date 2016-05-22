import os,sys
projectPath = os.path.abspath(os.path.dirname('..\..\..'))
sys.path.append(projectPath)
import time
from DAY6.bin import initAll
from DAY6.bin.fight import matchMaster
from DAY6.bin.visit import visitTown
from  DAY6.conf import map
import DAY6.bin.initAll
zuobi = True
def cleanPrint():
    try:
        os.system('cls')
    except:
        os.system('clear')
def chooseInHeroInfo():
    while 1:
        cleanPrint()
        choose2 = input('''\
                你可选择：
                1、返回城镇
                2、出城
                3、使用物品
                ''')
        if choose2 == '1':
            #checkHeroOroutTown = visitTown(mapTown,hero1)
            x1  = visitTown(mapTown,hero1)
            checkHeroOroutTown = x1.returnMessage
            return checkHeroOroutTown
        elif choose2 == '2':
            return 'outTown'
        elif choose2 == '3':
            print('使用背包物品功能未完成,敬请期待...')
if __name__ == '__main__':
    newloadFlag = True
    while newloadFlag:
        cleanPrint()
        print('''\
        欢迎来到【打怪世界】!
        这个世界存在1个城镇及5个怪物地图。
        城镇中可以购买装备及补给。
        通关条件：打败【高级BOOS】地图中的【金角大王】
        ''')
        choose1 = input('''\
        1，新游戏
        2，读取存档
        ''')
        if choose1 == '1':
            cleanPrint()
            HeroNmae = input('''\
            欢迎你，勇敢的英雄！
            请输入你的英雄的名字：
            ''')
            HeroNmae = HeroNmae.strip()
            hero1 = initAll.iniHero(HeroNmae)
            #作弊，使英雄非常强大
            if zuobi == True:
                hero1.minDamagee = 1000
                hero1.maxDamage = 1000
                hero1.defense = 1000
                hero1.health = 10000
                print("作弊开启，英雄很牛逼")
            mapTown = initAll.initTown()
            x1  = visitTown(mapTown,hero1)
            checkHeroOroutTown = x1.returnMessage
            newloadFlag = False
        elif choose1 == '2':
            print('存档功能未完成!敬请期待....')
            continue
        else:
            continue
    showTownOver = True
    while showTownOver:
        if checkHeroOroutTown == 'checkHero':
            cleanPrint()
            hero1.tell()
            hero1.pack.tell()
            input("按任意键继续.....")
            checkHeroOroutTown = chooseInHeroInfo()
            continue
        elif checkHeroOroutTown == 'visitTown':
            x1  = visitTown(mapTown,hero1)
            checkHeroOroutTown = x1.returnMessage
            continue
        elif checkHeroOroutTown == 'outTown':
            while 1:
                print('''你可选择： ''')
                masterMapListLen = len(initAll.masterMapList)
                for i in range(masterMapListLen):
                    print(i+1,'、',initAll.masterMapList[i][0])
                choose3 = input('请输入你的选择')
                if choose3.isdigit():
                    choose3 = int(choose3)
                    if choose3 <= masterMapListLen:
                        mastermap = initAll.iniMasterMap(choose3-1)
                        for i in mastermap.master.keys():
                            cleanPrint()
                            mastermap.tell()
                            if not i.isDeath:
                                cleanPrint()
                                print('遭遇怪物...!')
                                mastermap.tell()
                                time.sleep(0.5)
                                master = i
                                herostatus = matchMaster(hero1,master)
                                if herostatus == 'heroIsDeath':
                                    break
                                input('按任意键继续...')
                        #大BOSS被干掉
                        if mastermap.name == '高级BOSS' and herostatus == 'masterIsDeath':
                            print('恭喜你，通关了！')
                            showTownOver = False
                            #跳出checkHeroOroutTown == 'outTown':循环
                            break
                        elif herostatus == 'masterIsDeath':
                            print('怪物清除完成...')
                        elif  herostatus == 'heroIsDeath':
                            checkHeroOroutTown == 'visitTown'
                            continue


