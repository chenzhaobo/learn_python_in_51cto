import crmOldBoy
import fenxi
import os

ifReverse = False
paiXuKey = '1'
while 1:
    try:
         os.system('cls')
    except:
        os.system('clear')
    print(
        '''本程序可自动爬取http://crm.oldboyedu.com/的成绩
        请选择：
        1，更新成绩
        2，查看成绩
        ''' )
    Choose1 = input('请选择：')
    if '1' == Choose1:
        crmOldBoy.run(paiXuKey,ifReverse)
        temp = input('成绩已更新，按任意键继续...')
        continue
    if '2' == Choose1:
        goon = True
        while goon:
            fenxi.run(paiXuKey,ifReverse)
            print(
                '''
                结果可排序，请选择相应的排序
                1，学号   2，总成绩   3,反向排序  b,返回
                '''
            )
            Choose2 = input('请选择：')
            if '1' == Choose2:
                paiXuKey = '1'
                continue
            elif '3' == Choose2:
                if ifReverse:
                    ifReverse = False
                else:
                    ifReverse = True
                continue
            elif '2' == Choose2:
                paiXuKey = '2'
                continue
            elif 'b' == Choose2:
                goon = False
