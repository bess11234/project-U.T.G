import random
Player = {'hp': 10, 'mp': 10, 'str': 10, 'agi': 10, 'int': 10}
Name_Boss_random = ['Slime', 'Ant', 'Goblin', 'Orc', 'Lizard', 'Ancient Robot']
Monster = {'Slime': {'hp': 2, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3, 'skill': {'พุ่งโจมตี': (8, 1), 'พ่นเมือก': (7, 3), 'กลืนกิน': (20, 10), 'กัดรุนแรง': (30, 70), 'ระเบิดเมือก': (40, 130)}  },
            'Ant': {'hp': 3, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2, 'skill': {'โจมตีธรรมดา': 8, 'กัด': 7, 'พุ่งโจมตี': (17, 10), 'พ่นพิษ': (26, ), 'เจาะเกราะ': 30}},
            'Goblin': {'hp': 5, 'mp': 5, 'str': 4, 'agi': 5, 'int': 4, 'skill': {'ต่อย': 9, 'ฟาดด้วยสันดาบ': 8, 'คบเพลิงไฟ': 19, 'เฉือนเนื้อ': 24, 'ฟาดฟัน': 30}},
            'Orc': {'hp': 15, 'mp': 3, 'str': 6, 'agi': 3, 'int': 0, 'skill': {'คำราม': 10, 'ทุบ': 7, 'แขนยักษ์': 18, 'ทำลายล้าง': 25, 'พสุธากัมปนาท': 35}},
            'Lizard': {'hp': 7, 'mp': 20, 'str': 2, 'agi': 18, 'int': 5, 'skill': {'ลอบกัด': 11, 'เคลือบพิษ': 5, 'กรงเล็บปีศาจ': 11, 'สายฟ้าฟาด': 17, 'ความเร็วเทพ': 25}},
            'Ancient Robot': {'hp': 10, 'mp': 10, 'str': 5, 'agi': 15, 'int': 50, 'skill': {'D': 10, 'E': 10, 'A': 10, 'T': 10, 'H': 50}}}
def re_mon():
        random_mon = random.choice(Name_Boss_random)
        return random_mon
#เลือด
#for i in Monster:
        #Monster[i]['hp'] += Monster[i]['str']*5
        #print(Monster[i]['hp'])
