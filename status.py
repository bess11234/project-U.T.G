def status():
    
    Player = [{'hp': 10, 'mp': 10, 'str': 10, 'agi': 10, 'int': 10}]
    Tower = 0
    
    Monster = [{'Slime': {'hp': 0, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3}},
               {'Ant': {'hp': 0, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2}},
               {'Goblin': {'hp': 0, 'mp': 7, 'str': 9, 'agi': 8, 'int': 10}},
               {'Orc': {'hp': 0, 'mp': 10, 'str': 14, 'agi': 10, 'int': 15}},
               {'Lizard': {'hp': 0, 'mp': 20, 'str': 7, 'agi': 19, 'int': 7}},
               {'Ancient Robot': {'hp': 0, 'mp': 50, 'str': 25, 'agi': 15, 'int': 50}}]
    Monster[0]['Slime']['hp'] += Monster[0]['Slime']['str']*5
    Monster[1]['Ant']['hp'] += Monster[1]['Ant']['str']*5
    Monster[2]['Goblin']['hp'] += Monster[2]['Goblin']['str']*5
    Monster[3]['Orc']['hp'] += Monster[3]['Orc']['str']*5
    Monster[4]['Lizard']['hp'] += Monster[4]['Lizard']['str']*5
    Monster[5]['Ancient Robot']['hp'] += Monster[5]['Ancient Robot']['str']*5
    while True:
        Tower += 1
        Point = Tower*5
        if Player[0]['hp'] == 0 or Tower == 50:
            break
        if Tower == (5 or 15 or 25 or 35 or 45):
            for buff in Monster[0]:
                print(buff) 
status()
#if Tower == (10 or 20 or 30 or 40 or 50):
            #Point += 10