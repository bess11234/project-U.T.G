import random
Player = {'hp': 10, 'mp': 10, 'str': 10, 'agi': 10, 'int': 10}
Name_Boss_random = ['Slime', 'Ant', 'Goblin', 'Orc', 'Lizard', 'Ancient Robot']
Monster = {'Slime': {'hp': 2, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3},\
            'Ant': {'hp': 3, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2},\
            'Goblin': {'hp': 9, 'mp': 7, 'str': 9, 'agi': 8, 'int': 10},\
            'Orc': {'hp': 15, 'mp': 10, 'str': 14, 'agi': 10, 'int': 15},\
            'Lizard': {'hp': 8, 'mp': 20, 'str': 7, 'agi': 19, 'int': 7},\
            'Ancient Robot': {'hp': 30, 'mp': 50, 'str': 25, 'agi': 15, 'int': 50}}

Boss_random = Monster[random.choice(Name_Boss_random)]
#เลือด
#for i in Monster:
        #Monster[i]['hp'] += Monster[i]['str']*5
        #print(Monster[i]['hp'])
