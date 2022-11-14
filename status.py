def status():
    
    Player = [{'hp': 10, 'mp': 10, 'str': 10, 'agi': 10, 'int': 10}]
    Tower = 0
    
    Monster = [{'Slime': {'hp': 2, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3}},
               {'Ant': {'hp': 3, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2}},
               {'Goblin': {'hp': 9, 'mp': 7, 'str': 9, 'agi': 8, 'int': 10}},
               {'Orc': {'hp': 15, 'mp': 10, 'str': 14, 'agi': 10, 'int': 15}},
               {'Lizard': {'hp': 8, 'mp': 20, 'str': 7, 'agi': 19, 'int': 7}},
               {'Ancient Robot': {'hp': 30, 'mp': 50, 'str': 25, 'agi': 15, 'int': 50}}]
    while True:
        Tower += 1
        Point = Tower*5
        if Player[0]['hp'] == 0 or Tower == 50:
            break
        
        print(Tower, Point)
status()
#if Tower == (10 or 20 or 30 or 40 or 50):
            #Point += 10 