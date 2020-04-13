#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者:赵凯隆
日期：2020.4，12
"""
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
import random
def name_to_number(name):#将游戏对象对应到不同的整数
    if name=='石头':
        return 0
    elif name=='史波克':
        return 1
    elif name=='纸':
        return 2
    elif name=='蜥蜴':
        return 3
    elif name=='剪刀':
        return 4
    else:
        print("Error: No Correct Name")
    
def number_to_name(number):#将整数对应到不同的游戏对象
    if number==0:
        return '石头'
    elif number==1:
        return '史波克'
    elif number==2:
        return '纸'
    elif number==3:
        return '蜥蜴'
    elif number==4:
        return '剪刀'
    else:
        print("Error: No Correct Name")
def rpsls(player_choice):#用户给出选择，根据游戏规则，屏幕上输出结果
    print("您的选择为：",player_choice)
    player_number=name_to_number(player_choice)
    print("----------------")
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print("计算机的选择为：" , comp_choice)
    diff=(comp_number-player_number)%5
    if diff==1 or diff==2:
        print('计算机赢了')
    elif diff==3 or diff==4:
        print('您赢了')
    elif diff==0:
        print("平局")
    else:
        print('游戏错误')
    
rpsls('石头')
rpsls('史波克')
rpsls('纸')
rpsls('蜥蜴')
rpsls('剪刀')







print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


