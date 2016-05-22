import random
class things(object):
    def __init__(self,name,price,thingsLevel='普通的'):
        self.__name = name
        self.__price = price
        self.__thingsLevel = thingsLevel
        # self.__attribute = None
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def thingsLevel(self):
        return self.__thingsLevel
    @thingsLevel.setter
    def thingsLevel(self,values):
        self.__thingsLevel = values
    # @property
    # def attribute(self):
    #     return self.__attribute
    # @attribute.setter
    # def attribute(self,values):
    #     self.__attribute = values

class weapon(things):
    def __init__(self,name,price,minDamage,maxDamage,thingsLevel):
        super(weapon,self).__init__(name,price,thingsLevel)
        self.__minDamage = minDamage
        self.__maxDamage = maxDamage
        self.__attribute = '武器'
    @property
    def minDamage(self):
        return self.__minDamage
    @property
    def maxDamage(self):
        return self.__maxDamage
    @property
    def attribute(self):
        return self.__attribute
    def tell(self):
        print("物品类型：%s\n物品名称：%s\n攻击力：%s-%s\n出售价格：%s\n品质：%s\n"
              %(self.__attribute,self.name,self.__minDamage,self.__maxDamage,self.price,self.thingsLevel))

class armor(things):
    def __init__(self,name,price,defense,thingsLevel):
        super(armor,self).__init__(name,price,thingsLevel)
        self.__defense = defense
        self.__attribute = '防具'
    @property
    def defense(self):
        return self.__defense
    @property
    def attribute(self):
        return self.__attribute
    def tell(self):
        print("物品类型：%s\n物品名称：%s\n防御力：%s\n出售价格：%s\n品质：%s\n"
              %(self.__attribute,self.name,self.__defense,self.price,self.thingsLevel))


class food(things):
    def __init__(self,name,price,restroes,thingsLevel):
        super(food,self).__init__(name,price,thingsLevel)
        self.__restroes = restroes
        self.__attribute = '食物'
    @property
    def restroes(self):
        return  self.__restroes
    @property
    def attribute(self):
        return self.__attribute
    def tell(self):
        print('''物品类型：%s\n名称：%s\n恢复生命值：%s\n出售价格：%s\n品质：%s\n'''
              %(self.__attribute,self.name,self.__restroes,self.price,self.thingsLevel))
if __name__ == '__main__':
    a = armor('衣服',123,15)
    a.tell()
    print(a.attribute)
    print(a.name)
    print(a.price)
    print(a.defense)