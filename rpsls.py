#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
����:�Կ�¡
���ڣ�2020.4��12
"""
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
import random
def name_to_number(name):#����Ϸ�����Ӧ����ͬ������
    if name=='ʯͷ':
        return 0
    elif name=='ʷ����':
        return 1
    elif name=='ֽ':
        return 2
    elif name=='����':
        return 3
    elif name=='����':
        return 4
    else:
        print("Error: No Correct Name")
    
def number_to_name(number):#��������Ӧ����ͬ����Ϸ����
    if number==0:
        return 'ʯͷ'
    elif number==1:
        return 'ʷ����'
    elif number==2:
        return 'ֽ'
    elif number==3:
        return '����'
    elif number==4:
        return '����'
    else:
        print("Error: No Correct Name")
def rpsls(player_choice):#�û�����ѡ�񣬸�����Ϸ������Ļ��������
    print("����ѡ��Ϊ��",player_choice)
    player_number=name_to_number(player_choice)
    print("----------------")
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ��" , comp_choice)
    diff=(comp_number-player_number)%5
    if diff==1 or diff==2:
        print('�����Ӯ��')
    elif diff==3 or diff==4:
        print('��Ӯ��')
    elif diff==0:
        print("ƽ��")
    else:
        print('��Ϸ����')
    
rpsls('ʯͷ')
rpsls('ʷ����')
rpsls('ֽ')
rpsls('����')
rpsls('����')







print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


