# from  NPC import master
import random
from DAY6.conf.NPC import master,hero
from DAY6.conf.pack import *
from DAY6.conf import randomThings
class map(object):
    def __init__(self,name,mapLevel,masterNumber):
        self.master = {}
        self.name = name
        self.mapLevel = mapLevel
        self.masterNumber = masterNumber
        self.masterInfo()
        self.setmapLevel()

    @property
    def masterMinDamage(self):
        return self.__masterLevel * 5 + 50
    @property
    def masterMaxDamage(self):
        return self.__masterLevel * 5 + 70
    @property
    def masterDefense(self):
        return 25 + self.__masterLevel * 5
    @property
    def masterHealth(self):
        return 550 + self.__masterLevel * 5
    @property
    def masterExperience(self):
        return 45 + self.__masterLevel * 5
    @property
    def MasterDropMoney(self):
        return 60 + self.__masterLevel * 5

    def setmapLevel(self):
        #生成地图中的怪物，存放到字典中
        for i in range(self.masterNumber):
            self.masterLevel()
            a = master(self.masterNmae,self.__masterLevel,self.masterHealth,self.masterMinDamage,self.masterMaxDamage,
                       self.masterDefense,self.masterExperience,self.MasterDropMoney)
            self.master.setdefault(a,a.isDeath)

    def masterLevel(self):
        self.__masterLevel = random.randint(self.masterMinLevel,self.MasterMaxLevel)

    def masterInfo(self):
        if self.mapLevel == 1:
            self.masterNmae = '虚弱的小兵'
            self.masterMinLevel = 1
            self.MasterMaxLevel = 5
        elif self.mapLevel == 2:
            self.masterNmae = '强壮的小兵'
            self.masterMinLevel = 5
            self.MasterMaxLevel = 15
        elif self.mapLevel == 3:
            self.masterNmae = '疯狂的小兵'
            self.masterMinLevel = 50
            self.MasterMaxLevel = 55
        elif self.mapLevel == 4:
            self.masterNmae = '银角大王'
            self.masterMinLevel = 70
            self.MasterMaxLevel = 80
        elif self.mapLevel == 5:
            self.masterNmae = '金角大王'
            self.masterMinLevel = 100
            self.MasterMaxLevel = 100
    def tell(self):
        print('*'*40)
        print('欢迎来到%s冒险!\n'%self.name)
        print('*'*40)
class town(object):
    def __init__(self):
        self.npcProject = {}
    def loadNpc(self,name):
        self.npcname = name
        a = hero(name,100)
        p = pack()
        p.setOwner(a)
        self.initPack(p)
        a.pack = p
        self.npcProject.setdefault(a)
    def initPack(self,p):
        for i in range(5):
            if self.npcname == '武器商人':
                product = randomThings.randomWeapon()
            elif self.npcname == '防具商人':
                product = randomThings.randomArmor()
            elif self.npcname == '补给商人':
                product = randomThings.randomFood()

            p.getWeapon(product)



if __name__ == '__main__':
    # a = map('低级地图',5,1)
    # a.tell()
    # for i in a.master:
    #     print(i.tell())
    x = town()
    x.loadNpc('武器商人')
    for i in x.npcProject:
        print(i.name)
        i.pack.tell()
    # x.loadNpc('武器商人')
    x.loadNpc('防具商人')
    x.loadNpc('补给商人')
    for i in x.npcProject:
        print(i.name)
        i.pack.tell()