"""item"""
#ผ่าน 5 ชั้น stat อาวุธ จะเพิ่มขึ้น 5 stat
import random   
"""item in game Ultimate tower super ultra Character Galaxy of god"""
rate_drop = ["แย่", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "ดีเยี่ยม", "ดีเยี่ยม", "ดีเยี่ยม", "ตำนานจนละเอียด"]
#ถ้ามีเวลาค่อยใส่ของกวนๆ
potion_drop = ["Potion HP", "Potion HP", "Potion HP", "Potion MP", "Potion MP", "Potion MP", "แว่นตาที่แตกพ่ายของผู้สร้าง", "ลุงตูบที่อยู่บ้านข้างๆ", "กระป๋องน้ำซ่าชื่นใจ", "ความรักที่คุณให้เขาไปแต่เขาไม่ให้เคยให้อะไรกลับมา"]
legen_drop = ["กิ้งไม้แห่งสัจธรรม", "สว่านทะลวงสวรรค์"]
weapon_drop = ["ดาบ", "เรเปีย", "สมุดเวทย์", "หอก", "ดาบยักษ์", "ดาบสามมือ", "คฑาเวทย์", "ตะเกียงเวทย์", "ไม้กายสิทธิ์", "ระเบิดเวทย์"]

weapon_legendary = {"กิ้งไม้แห่งสัจธรรม":{"str": 1000, "int": 1000, "agi": 50, "skill":{"ความจริงมีเพียงหนึ่งเดียว!": (1000, 2, 2.5, "i")}}, 
                    "สว่านทะลวงสวรรค์":{"str": 1000, "int": 1000, "agi": 60, "skill":{"บุกทะลวงเข้าไป!": (1200, 1, 2.5, "s")}}, 
                    "":""}
weapon_secret = {"9 มม.ฝังเวทย์":{"str": 2000, "int": 2000, "agi": 20, "skill":{"นี้แหละวิธีแก้ปัญหาที่ดีที่สุด": (2000, 1, 2.5, "i")}}}
weapon = {"ดาบ": {"str": 5, "int": 0, "agi": 3, "skill": {"ฟันตรง": (4, 5, 0.1, "s"), "ดาบเฉือนลม": (16, 5, 0.5, "s"), "ฟันแหลก": (35, 10, 1.5, "s"), "ดาบสั่งตายใจสั่งมา": (300, 50, 2, "s")}}, 
              "หอก": {"str": 6, "int": 0, "agi": 4, "skill": {"แทงตรง": (4, 5, 0.1, "s"), "ทะลวงเข้าไป!": (16, 10, 0.5, "s"), "ควงสว่าน": (50, 15, 1.5, "s"), "เฮลิปเตอร์!": (350, 40, 2, "s")}}, 
              "เรเปีย": {"str": 3, "int": 0, "agi": 9, "skill": {"ยก": (2, 5, 0.1, "s"), "ชิด": (19, 4, 0.5, "s"), "จ้วง": (60, 30, 1.5, "s"), "แทง!": (350, 50, 2, "s")}}, 
              "ดาบยักษ์": {"str": 10, "int": 0, "agi": -1, "skill": {"ฟันตรงแบบแรง!": (6, 5, 0.1, "s"), "ตบลอย": (25, 15, 0.5, "s"), "ถล่มพสุธา": (70, 30, 1.5, "s"), "ผ่าปฐพี": (500, 150, 2, "s")}}, 
              "ดาบสามมือ": {"str": 8, "int": 0, "agi": 5, "skill": {"ฟันสามต่อ": (5, 5, 0.1, "s"), "ตัดผ่าอากาศสามต่อ": (15, 6, 0.5, "s"), "เพลงดาบสายลม 36 ประกาศ": (100, 40, 1.5, "s"), "อาชูรา": (450, 120, 2, "s")}}, 
              "สมุดเวทย์": {"str": 0, "int": 5, "agi": 3, "skill": {"ลูกบอลไฟ": (3, 5, 0.1, "i"), "สายฟ้าฝาด": (35, 25, 0.5, "i"), "เกมลงทัณฑ์แห่งความมืด": (60, 90, 1.5, "i"), "อ่านหนังสือซะบ้างเซ่!": (400, 201, 2, "i")}}, 
              "คฑาเวทย์": {"str": 0, "int": 10, "agi": -1, "skill": {"คฑาเสริมเวทย์ฟาดไม่ยั้ง": (4, 5, 0.1, "i"), "ลมเฉือน": (29, 11, 0.5, "i"), "ไปคุยกับรากมะม่วง!": (80, 101, 1.5, "i"), "ตัวแทนแห่งวันจันทร์จะลงทัณฑ์แกเอง": (500, 250, 2, "i")}}, 
              "ตะเกียงเวทย์": {"str": 0, "int": 7, "agi": 1, "skill": {"เวทแห่งแสง": (3, 5, 0.1, "i"), "พาาาลังงงคลื่นนเต่าาาา!": (35, 20, 0.5, "i"), "ดาบผนึกแห่งแสง": (75, 95, 1.5, "i"), "บอลเกงกิ": (450, 200, 2, "i")}}, 
              "ไม้กายสิทธิ์": {"str": 0, "int": 6, "agi": 7, "skill": {"สติลไวไฟ": (4, 5, 0.1, "i"), "ร้ายกาจจจ": (50, 31, 0.5, "i"), "เอสเปรสโซ่ปลาโตนุ่ม": (100, 120, 1.5, "i"), "อะวาเคดาบร้า": (390, 190, 2, "i")}}, 
              "ระเบิดเวทย์": {"str": 0, "int": 8, "agi": 5, "skill": {"ประทัด": (3, 5, 0.1, "i"), "ระเบิดมือ": (30, 21, 0.5, "i"), "ทีเอ็นที": (100, 100, 1.5, "i"), "ระเบิดเวลาอ๊ากกกกกก!": (499, 299, 2, "i")}}}

def re_item():
    """rate drop item"""
    random_rate = random.choice(rate_drop)
    random_drop = random.choice(weapon_drop)
    gain = weapon[random_drop].copy()
    return gain, random_rate, random_drop

def rate_legend():
    """rate drop legendary waepon"""
    legend = ""
    if random.randrange(100) == random.randrange(100):
        legend = random.choice(legen_drop)
    return legend, weapon_legendary[legend]

def re_potion():
    """rate drop item"""
    number_rate = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
    random_number = random.choice(number_rate)
    get = [random.choice(potion_drop) for _ in range(random_number)]
    return get