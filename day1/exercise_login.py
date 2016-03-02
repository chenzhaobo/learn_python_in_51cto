#!/usr/bin/python
#coding: utf8
'''
编写登录接口
1，输入用户名、密码
2，认证成功后显示欢迎信息
3，输错三次后锁定
方案1：
用户名及密码保存在字典中，用户名为KEY，密码为VALUE
定义一个3次循环》输入用户名及密码》用户名在字典中存在》判断密码是否相等》用户名及密码正确提示认证成功
                                 》for name in dict is False 》print ‘用户名不存在’ continue
                                 》for name in dict is True  》for passwd == dict[name] is False > print '密码错误' continue
输错三次后   print 错误次数过多，您已被锁定  break
方案2
将用户名密码保存到文件中
程序从文件中一次性读取所有用户名和密码保存到字典中
判断用户名密码是否正确可复用方案1的while循环
'''
##------------------------------------------------------------------------------------------
# #方案1
# num = 0
# num_max = 3
# username_passwd_dict = {'zhaobo':'zhaobo','xiaoguang':'xiaoguang','hongbing':'hongbing'}
# #设置循环次数 num_max 为可配置。
# while num < num_max:
#     username = input('请输入用户名：')
#     passwd = input('请输入密码：')
#     #判断用户名是否存在。
#     if username in username_passwd_dict:
#         #判断用户名对应的密码是否正确。
#         if passwd == username_passwd_dict[username]:
#             print('验证通过！您已成功登陆！')
#             break
#         else:
#             print('密码错误！请重新输入')
#             num += 1
#     else:
#         print('用户名不存在！请重新输入')
#         num += 1
# #当用户验证次数超过3次时，提示错误。验证通过时循环break，esle将不被执行。
# else:
#     print('登陆错误次数超过%s次，您已被kick！'%num)
#-----------------------------------------------------------------------
#方案2
#初始化文件
def initialization(filename,add_new = False):
    import os
    if os.path.exists(filename):
        openfile = open(filename,'a')
    else:
        openfile = open(filename,'w')
    openfile.write('\nzhaobo:zhaobo')
    openfile.write('\nzhaobo1:zhaobo1')
    #手动添加数据
    if add_new:
        loop = True
        while loop:
            username = input('请输入要要添加的用户名：')
            passwd = input('请输入该用户名的密码：')
            openfile.write('\n'+username+':'+passwd)
            goOn = input('是否继续添加？（按任意键继续添加/N不添加）')
            if goOn.lower() == 'n':
                loop = False
    openfile.close()
#读取文件中的用户名和密码，文件中每一行存入一对用户名和密码，并使用”：“分隔
def get_userinfo(filename):
    username_passwd_dict = {}
    openfile = open(fileName,'r')
    #遍历文件中的所有行
    for line in openfile:
        #将每一行的信息转换为列表
        username_passwd_list_temp = line.strip().split(':')
        #去除空行，列表中第一个元素为用户名，第二个元素为密码，保存到字典中
        if username_passwd_list_temp != ['']:
            username_passwd_dict[username_passwd_list_temp[0]] = username_passwd_list_temp[1]
    openfile.close()
    print('系统中存在的用户名及密码：',username_passwd_dict)
    return username_passwd_dict
#判断用户登录的逻辑函数
def login(username_passwd_dict,num=0,num_max=3):
    while num < num_max:
        username = input('请输入用户名：')
        passwd = input('请输入密码：')
        #判断用户名是否存在。
        if username in username_passwd_dict:
            #判断用户名对应的密码是否正确。
            if passwd == username_passwd_dict[username]:
                print('验证通过！您已成功登陆！')
                break
            else:
                print('密码错误！请重新输入')
                num += 1
        else:
            print('用户名不存在！请重新输入')
            num += 1
    #当用户验证次数超过3次时，提示错误。验证通过时循环break，esle将不被执行。
    else:
        print('登陆错误次数超过%s次，您已被kick！'%num)
if __name__ == '__main__':
    fileName = 'userInfo2.txt'
    #初始化参数add_new = True 时手动添加数据
    initialization(fileName,add_new = False)
    #获取参数
    userInfo = get_userinfo(fileName)
    #执行登录函数
    login(userInfo)
#-----------------------方案2结束-------------------------------------------