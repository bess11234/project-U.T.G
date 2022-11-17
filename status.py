import random
Player = {'name': "", 'hp': 10, 'mp': 10, 'max_hp': 10, 'max_mp': 10, 'str': 10, 'agi': 10, 'int': 10}
Name_Boss_random = ['Slime', 'Ant', 'Goblin', 'Orc', 'Lizard', 'Ancient Robot']
Monster = {'Slime': {'hp': 2, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3, 'skill': {'พุ่งโจมตี': 10, 'พ่นเมือก': (7, 14), 'กลืนกิน': (20, 20), 'กัดรุนแรง': (30, 27), 'ระเบิดเมือก': (40, 80)}  },
            'Ant': {'hp': 3, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2, 'skill': {'โจมตีธรรมดา': 10, 'กัด': 12, 'พุ่งโจมตี': 17, 'พ่นพิษ': (26, 20), 'เจาะเกราะ': (30, 70)}},
            'Goblin': {'hp': 5, 'mp': 5, 'str': 4, 'agi': 5, 'int': 4, 'skill': {'ต่อย': 11, 'ฟาดด้วยสันดาบ': 8, 'คบเพลิงไฟ': (19, 50), 'เฉือนเนื้อ': 24, 'ฟาดฟัน': 30}},
            'Orc': {'hp': 15, 'mp': 3, 'str': 6, 'agi': 3, 'int': 0, 'skill': {'ทุบ': 7, 'คำราม': (12, 20), 'แขนยักษ์': 18, 'ทำลายล้าง': (25, 50), 'พสุธากัมปนาท': (35, 70)}},
            'Lizard': {'hp': 4, 'mp': 20, 'str': 2, 'agi': 18, 'int': 5, 'skill': {'ลอบกัด': 13, 'เคลือบพิษ': (17, 140) , 'กรงเล็บปีศาจ': (20, 170), 'สายฟ้าฟาด': (27, 200), 'ความเร็วเทพ': (30, 250)}},
            'Ancient Robot': {'hp': 10, 'mp': 2, 'str': 5, 'agi': 15, 'int': 20, 'skill': {'D': (5, 40), 'E': (5, 40), 'A': (5, 40), 'T': (5, 40), 'H': (50, 400)}}}
def re_mon():
        random_mon = random.choice(Name_Boss_random)
        return random_mon
#เลือด
#for i in Monster:
        #Monster[i]['hp'] += Monster[i]['str']*5
        #print(Monster[i]['hp'])
