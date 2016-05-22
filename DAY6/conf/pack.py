from DAY6.conf import randomThings
from   DAY6.conf.NPC import hero
class pack(object):
    def __init__(self):
        self.__weapon = {}
        self.__armor = {}
        self.__food = {}
        self.__money = 0
        self.__owner = None
    @property
    def weapon(self):
        return self.__weapon
    @property
    def armor(self):
        return self.__armor
    @property
    def food(self):
        return self.__food
    def tell(self):
        ljustlenth = 15
        print('*'*40)
        print('''背包情报：''')
        print('武器列表:')
        print('名称'.center(ljustlenth,' '),'攻击力'.center(ljustlenth,' '),'数量')
        for x,y in self.__weapon.items():
            damage = str(x.minDamage)+'-'+str(x.maxDamage)
            print(x.name.center(ljustlenth,' '),damage.center(ljustlenth,' '),y)
        print('防具列表：')
        print('名称'.center(ljustlenth,' '),'防御力'.center(ljustlenth,' '),'数量')
        for x,y in self.__armor.items():
            print(x.name.center(ljustlenth,' '),str(x.defense).center(ljustlenth,' '),y)
        print('补给品列表：')
        print('名称'.center(ljustlenth,' '),'回复力'.center(ljustlenth,' '),'数量')
        for x,y in self.__food.items():
            print(x.name.center(ljustlenth,' '),str(x.restroes).center(ljustlenth,' '),y)
        print('金钱：',self.__money)

        print('*'*40)
    def setOwner(self,values):
        self.__owner = values
    def getMoney(self,values):
        self.__money += values
        #print('获得金钱：',values)
    def getWeapon(self,values):
        if not self.__weapon.get(values):
            self.__weapon.setdefault(values,1)
        else:
            self.__weapon[values] +=1
        #print('获得%s'%values.name)
    def getArmor(self,values):
        if not self.__armor.get(values):
            self.__armor.setdefault(values,1)
        else:
            self.__armor[values] +=1
        #print('获得%s'%values.name)
    def getfood(self,values):
        if not self.__food.get(values):
            self.__food.setdefault(values,1)
        else:
            self.__food[values] +=1
        #print('获得%s'%values.name)
    def takeMoney(self,values):
        if self.__money - values >=0:
            self.__money -= values
            print('失去金钱：%s'%values)
            return True
        else:
            print('金钱不足！')
            return
    def takeWeapon(self,values):
        if self.__weapon.get(values):
            self.__weapon[values] -=1
            if self.__weapon[values] == 0:
                self.__weapon.pop(values)
                return True
        else:
            print(values.name,'不存在')
    def takeArmor(self,values):
        if self.__armor.get(values):
            self.__armor[values] -=1
            if self.__armor[values] == 0:
                self.__armor.pop(values)
        else:
            print(values.name,'不存在')
    def takefood(self,values):
        if self.__food.get(values):
            self.__food[values] -=1
            if self.__food[values] == 0:
                self.__food.pop(values)
        else:
            print(values.name,'不存在')
if __name__ == "__main__":
    a = randomThings.randomArmor()
    a1 = randomThings.randomArmor()
    w = randomThings.randomWeapon()
    f = randomThings.randomFood()
    w1 = randomThings.randomWeapon()
    f1 = randomThings.randomFood()
    p = pack()
    h = hero('美国队长',1,health=100,minDamage=100,maxDamage=120,defense=10)
    print('sss')
    p.setOwner(h)
    p.getWeapon(w)
    p.getWeapon(w)
    p.getWeapon(w1)
    p.getWeapon(w1)
    p.getArmor(a)
    p.getArmor(a1)
    p.getfood(f)
    p.getfood(f1)
    p.getMoney(100)
    p.tell()
    p.takeArmor(a1)
    p.takeWeapon(w1)
    p.takeWeapon(w)
    p.takefood(f1)
    p.takeMoney(50)
    p.tell()
