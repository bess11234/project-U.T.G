import random
Player = {'name': "", 'hp': 10, 'mp': 10, 'max_hp': 10, 'max_mp': 10, 'str': 10, 'agi': 10, 'int': 10}
Name_Boss_random = ['Slime', 'Ant', 'Goblin', 'Orc', 'Lizard', 'Ancient Robot']
Monster = {'Slime': {'hp': 2, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3, 'skill': {'พุ่งโจมตี': (10, 0, 0.3,"s"), 'พ่นเมือก': (7, 14, 0.4, "i"), 'กลืนกิน': (20, 20, 0.5, "s"), 'กัดรุนแรง': (30, 27, 0.8, "s"), 'ระเบิดเมือก': (40, 80, 1, "i")}  },
            'Ant': {'hp': 3, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2, 'skill': {'โจมตีธรรมดา': (10, 0, 0.4,"s"), 'กัด': (12, 0, 0.6, "s"), 'พุ่งโจมตี': (17, 0, 0.8, "s"), 'พ่นพิษ': (26, 20, 1, "i"), 'เจาะเกราะ': (30, 70, 3, "s")}},
            'Goblin': {'hp': 5, 'mp': 5, 'str': 4, 'agi': 5, 'int': 4, 'skill': {'ต่อย': (11, 0, 0.8, "s"), 'ฟาดด้วยสันดาบ': (8, 0, 1, "s"), 'คบเพลิงไฟ': (19, 50, 1.5, "i"), 'เฉือนเนื้อ': (24, 0, 2, "s"), 'ฟาดฟัน': (30, 0, 2.5, "s")}},
            'Orc': {'hp': 15, 'mp': 3, 'str': 6, 'agi': 3, 'int': 0, 'skill': {'ทุบ': (7, 0, 1, "s"), 'คำราม': (12, 20, 2, "i"), 'แขนยักษ์': (18, 0, 1, "s"), 'ทำลายล้าง': (25, 50, 2, "s"), 'พสุธากัมปนาท': (35, 70, 2.8, "s")}},
            'Lizard': {'hp': 4, 'mp': 20, 'str': 2, 'agi': 18, 'int': 5, 'skill': {'ลอบกัด': (13, 0, 2, "s"), 'เคลือบพิษ': (17, 140, 2, "i") , 'กรงเล็บปีศาจ': (20, 170, 1.4, "s"), 'สายฟ้าฟาด': (27, 200, 2, "i"), 'ความเร็วเทพ': (30, 250, 3, "i")}},
            'Ancient Robot': {'hp': 10, 'mp': 2, 'str': 5, 'agi': 15, 'int': 20, 'skill': {'D': (5, 40, 2, "i"), 'E': (5, 40, 2, "i"), 'A': (5, 40, 2, "i"), 'T': (5, 40, 2, "i"), 'H': (50, 400, 5, "i")}}}
def re_mon():
        random_mon = random.choice(Name_Boss_random)
        return random_mon
def imagemon(mon):
        color = []
        if mon == "Slime":
                color = ["slime\\blue_slime.png", "slime\\green_slime.png", "slime\\nerd_slime.png", "slime\\purple_slime.png", "slime\\red_slime.png"]
                color = random.choice(color)
                return color
        if mon == "Ant":
                color = ["ant.png"]
                color = random.choice(color)
                return color
        if mon == "Goblin":
                color = ["Goblin.png"]
                color = random.choice(color)
                return color
        if mon == "Orc":
                color = ["Orc_gere.png"]
                color = random.choice(color)
                return color
        if mon == "Lizard":
                color = ["lizard\\purple_lizard.png", "lizard\\rainbow_lizard.png"]
                color = random.choice(color)
                return color
        if mon == "Ancient Robot":
                color = ["ruin_guard.png"]
                color = random.choice(color)
                return color
        