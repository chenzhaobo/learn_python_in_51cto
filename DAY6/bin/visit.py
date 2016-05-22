import os
from DAY6.bin.initAll import *
import prettytable
def cleanPrint():
    try:
        os.system('cls')
    except:
        os.system('clear')
class visitTown(object):
    def __init__(self,mapTown,heroOBJ):
        self.hero = heroOBJ #角色对象
        self.mapTown = mapTown #town地图对象
        self.__ArmsMerchant = None #武器商人
        self.__armorMerchant = None #防具商人
        self.__SupplyMerchant = None #补给商人
        self.__checkMerchantName = None #被查询商人的名字
        self.__checkMerchant = None #被查询商人对象
        self.__thingNameList = []  #添加被查询商人商品对象名到列表
        self.__thinsSeq = []   #获取被查询商人对应商品对象到列表，在顺序选择时用到
        self.__thingsPrice =[] #被查询商人商品价格
        self.__heroBuyThinsType = None #角色购买的方式
        self.iniBussinessMan() #初始化商品
        self.returnMessage = None
        self.showTown()
    def showTown(self):
        while 1:
            cleanPrint()
            TownChoose = None
            TownChoose = input('''\
            地图信息：
            1，拜访武器商人
            2，拜访防具商人
            3，拜访补给商人
            4，查看角色
            5, 出城
            请选择：''')
            #访问NPC
            visitDict = {'1':'武器商人','2':'防具商人','3':'补给商人'}
            if TownChoose == '4':
                self.returnMessage =  'checkHero'
                break
            elif TownChoose == '5':
                self.returnMessage =  'outTown'
                break
            elif visitDict.get(TownChoose):
                self.visitNpc(visitDict.get(TownChoose))
            #visitDict.get(TownChoose.split())
            #self.visitNpc('武器商人')

    def visitNpc(self,Npcname):
        MerchantDict = {'武器商人':self.__ArmsMerchant,'防具商人':self.__armorMerchant,'补给商人':self.__SupplyMerchant}
        heroBuyThinsTypeDict = {'武器商人':self.hero.pack.getWeapon,'防具商人':self.hero.pack.getArmor,'补给商人':self.hero.pack.getfood}
        self.__heroBuyThinsType = heroBuyThinsTypeDict[Npcname]
        self.__checkMerchantName = Npcname
        self.__checkMerchant =MerchantDict[self.__checkMerchantName]
        k = self.showThings()
        while 1:
            cleanPrint()
            print('''\
            %s售卖列表：
            '''%self.__checkMerchant.name)
            print(k)
            choose = input('''\
            B，购买结束
            请根据序号选择：''')
            if choose.isdigit():
                if int(choose) <= len(self.__thinsSeq) and self.hero.pack.takeMoney(self.__thingsPrice[int(choose)-1]):
                    self.__heroBuyThinsType(self.__thinsSeq[int(choose)-1])
                    print('购买%s成功！'%self.__thingNameList[int(choose)-1])
            elif choose == 'b' or choose == 'B':
                break
                    #print('')
    def iniBussinessMan(self):
        #初始化商人
        for i in self.mapTown.npcProject:
            if i.name == '武器商人':
                self.__ArmsMerchant = i
            if i.name == '防具商人':
                self.__armorMerchant = i
            if i.name == '补给商人':
                self.__SupplyMerchant = i
    def showThings(self):
        #查看商人的背包
        checkMerchantThings = {'武器商人':self.__ArmsMerchant.pack.weapon,'防具商人':self.__armorMerchant.pack.armor,
                               '补给商人':self.__SupplyMerchant.pack.food}
        #遍历商人销售商品列表
        for i in checkMerchantThings[self.__checkMerchantName]:
            self.__thingNameList.append(i.name)
            self.__thinsSeq.append(i)
            self.__thingsPrice.append(i.price)
        # print('''\
        # %s售卖列表：
        # '''%self.__checkMerchant.name)
        k = prettytable.PrettyTable(['序号','名称','价格'])
        for  i in range(len(self.__thinsSeq)):
            #s = self.__thinsSeq
            p = self.__thingsPrice
            n = self.__thingNameList
            k.add_row([i+1,n[i],p[i]])
        return k
if __name__ == '__main__':
    hero1 = iniHero('测试英雄')
    mapTown = initTown()
    test = visitTown(mapTown,hero1)