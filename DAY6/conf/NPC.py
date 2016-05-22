import random,time
from DAY6.conf import randomThings
import logging
class npc(object):
    def __init__(self,name,level,health,minDamage,maxDamage,defense,experience):
        self.__name = name
        self.__minDamagee = minDamage
        self.__maxDamage = maxDamage
        self.__defense = defense
        self.__experience = experience
        self.__health = health
        self.__level = level
        self.__isDeath = False
    @property
    def name(self):
        '''
        名
        :return:
        '''
        return self.__name

    #攻击力
    @property
    def minDamagee(self):
        return self.__minDamagee
    @minDamagee.setter
    def minDamagee(self,values):
        self.__minDamagee = values

    @property
    def maxDamage(self):
        return self.__maxDamage
    @maxDamage.setter
    def maxDamage(self,values):
        self.__maxDamage = values

    def randomDamage(self):
        '''
        攻击力
        :return:
        '''
        damage = random.randint(self.minDamagee,self.maxDamage)
        return damage

    @property
    def defense(self):
        '''
        防御力
        :return:
        '''
        return self.__defense
    @defense.setter
    def defense(self,values):
        '''
        防御力
        :return:
        '''
        self.__defense = values

    @property
    def experience(self):
        '''
        经验
        :return:
        '''
        return self.__experience
    @experience.setter
    def experience(self,values):
        '''
        经验
        :return:
        '''
        self.__experience = values

    @property
    def level(self):
        '''
        等级
        :return:
        '''
        return self.__level
    @level.setter
    def level(self,values):
        '''
        等级
        :return:
        '''
        self.__level = values
    @property
    def health(self):
        '''
        生命值
        :return:
        '''
        if self.__health < 0:
            self.__health = 0
        return self.__health
    @health.setter
    def health(self,values):
        self.__health = values

    @property
    def isDeath(self):
        '''
        死亡状态
        :return: 死亡返回True
        '''
        if self.__health <= 0:
            self.__isDeath = True
        else :
            self.__isDeath = False

        return self.__isDeath
    def attack(self):
        shanghai = self.randomDamage()
        print("%s发动了攻击！"%self.__name)
        return shanghai
    def getHurt(self,values):
        if isinstance(values,int):
            factHurt  =  values - self.__defense
            if factHurt <= 0:
                factHurt = 0
            self.__health -= factHurt
            print('%(name)s受到了%(values)s点攻击,%(name)s抵挡了%(defense)s点伤害，%(name)s失去%(factHurt)s点生命！'
                  %{"name":self.__name,"values":values,'defense':self.__defense,'factHurt':factHurt})
            print('%(name)s生命值:%(health)s'%{'name':self.__name,"health":self.health})
            if self.__health <= 0:
                self.__isDeath = True
                print('%s死亡！'%self.__name)
        else:
            raise TypeError('受到伤害出错，伤害值应为int,实际为%s,values = %s'%(type(values),values))
            logging.exception('受到伤害出错，伤害值应为int,实际为%s,values = %s'%(type(values),values))

class master(npc):
    def __init__(self,name,level,health,minDamage,maxDamage,defense,experience,dropMoney):
        super(master,self).__init__(name,level,health,minDamage,maxDamage,defense,experience)
        # self.minDamage = minDamage + level * 1
        # self.maxDamage = maxDamage + level * 2
        # self.defense = defense + level * 2
        # self.health = health + level * 10
        self.__dropMoney = dropMoney

    @property
    def dropThings(self):
        '''
        掉落物品
        :return:
        '''
        temp = random.randint(1,100)%2
        if temp == 0:
            self.__dropThings = randomThings.randomWeapon()
        if temp == 1:
            self.__dropThings = randomThings.randomFood()
        if temp == 2:
            self.__dropThings = randomThings.randomArmor()
        return self.__dropThings


    def dropMoney(self):
        temp = random.randint(1,100)
        money = random.randint(self.__dropMoney - temp,self.__dropMoney + temp)
        return money
    def tell(self):
        print('*'*50)
        print('情报：\n名称:%s\n攻击力：%s-%s\n生命值：%s\n等级：%s'
              %(self.name,self.minDamagee,self.maxDamage,self.health,self.level))
        time.sleep(0.5)
        print('%s:小子，你胆敢冒犯我！你会死的！'%self.name)
        print('*'*50)

class hero(npc):
    def __init__(self,name,level,health=550,minDamage=33,maxDamage=35,defense=10,experience=0):
        super(hero,self).__init__(name,experience=0,level=1,health=1000,minDamage=50,maxDamage=75,defense=5)
    def levelUp(self):
        while True:
            if self.experience >= 100:
                self.level += 1
                self.experience -= 100
                print('%s已升级，当前等级：%s'%(self.name,self.level))
            else:
                break

    def getExperience(self,values):
        self.experience += values
        print('%s获得经验值%s'%(self.name,values))

    def getThings(self,project):
        '''
        装备物品
        :param project: class tings 的实例对象
        :return:
        '''
        print('%s获得物品：%s'%(self.name,project.name))
        if project.attribute == '防具':
            self.defense += project.defense
            print('%s防御提升：防御+%s'%(self.name,project.defense))
        if project.attribute == '武器':
            self.minDamagee += project.minDamage
            self.maxDamage += project.maxDamage
            print('%s攻击力提升：攻击力提升%s-%s'%(self.name,project.minDamage,project.maxDamage))
        if project.attribute == '食物':
            self.health += project.restroes
            print('%s生命恢复：生命值+%s'%(self.name,project.restroes))
    def tell(self):
        #self.health = self.health
        print('*'*50)
        print('人物情报：\n名称:%s\n攻击力：%s-%s\n生命值：%s\n经验值：%s\n等级：%s'
              %(self.name,self.minDamagee,self.maxDamage,self.health,self.experience,self.level))
        print('*'*50)

if __name__ == '__main__':
    a = master('小兵',1,100,14,16,2,10,300)
    a.tell()
    guaiwushanghai = a.attack()
    a.getHurt(guaiwushanghai)
    guaiwumoney = a.dropMoney()
    print('怪物掉落了金钱：%s'%guaiwumoney)
    guaiwuThings = a.dropThings
    print('怪物掉落了物品：',guaiwuThings.name)
    h = hero('美国队长',1,health=100,minDamage=100,maxDamage=120,defense=10)
    h.tell()
    heroshanghai = h.attack()
    h.getHurt(heroshanghai)
    h.getExperience(a.experience)
    h.levelUp()
    h.getExperience(200)
    h.levelUp()
    h.getThings(guaiwuThings)
    h.getHurt(10000)
    h.tell()