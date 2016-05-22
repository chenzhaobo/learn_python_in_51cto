from  DAY6.conf import map
from DAY6.conf.pack import *
TownNpcList = ['防具商人','武器商人','补给商人']
masterMapList = [('轻松秒杀的地图',1,5),('普通的怪物地图',2,5),('强悍的怪物地图',3,5),
                ('低级BOSS',4,1),('高级BOSS',5,1)]
def initTown():
    mapTown = map.town()
    for i in TownNpcList:
        mapTown.loadNpc(i)
    return mapTown
def iniMasterMap(mapSeq):
     mapNmae,mapLevel,masterUnm =  masterMapList[mapSeq]
     return map.map(mapNmae,mapLevel,masterUnm)
def iniHero(name):
    __a = map.hero(name,1)
    __p = pack()
    __p.setOwner(__a)
    __a.pack = __p
    return  __a
