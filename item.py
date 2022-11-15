"""item"""
#ผ่าน 5 ชั้น stat อาวุธ จะเพิ่มขึ้น 5 stat
import random   
"""item in game Ultimate tower super ultra Character Galaxy of god"""
rate_drop = ["แย่", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "ดีเยี่ยม", "ดีเยี่ยม", "ดีเยี่ยม", "ตำนานจนละเอียด"]
#ถ้ามีเวลาค่อยใส่ของกวนๆ
potion_drop = ["Potion HP", "Potion MP"]
legen_drop = ["กิ้งไม้แห่งสัจธรรม", "ไม้แขวนเสื้อที่ลุกโชน"]
weapon_drop = ["ดาบ", "เรเปีย", "สมุดเวทย์", "หอก", "ดาบยักษ์", "ดาบสามมือ", "คฑาเวทย์", "ตะเกียงเวทย์", "ไม้กายสิทธิ์", "ระเบิดเวทย์"]

weapon_legendary = {"กิ้งไม้แห่งสัจธรรม":{"str": 0, "int": 1000, "agi": 20, "skill":{"ความจริงมีเพียงหนึ่งเดียว!!!"}}, 
                    "ไม้แขวนเสื้อที่ลุกโชน":{"str": 0, "int": 1000, "agi": 20, "skill":{"ไปกรอกน้ำเดี๋ยวนี้!!!"}}}
weapon = {"ดาบ": {"str": 5, "int": 0, "agi": 3, "skill": {"ฟันตรง": {}, "ดาบเฉือนลม": {}, "ฟันไม่ยัง": {}, "ดาบสั่งตายใจสั่งมา": {}}}, 
              "หอก": {"str": 6, "int": 0, "agi": 4, "skill": {"แทงตรง": {}, "": {}, "": {}, "": {}}}, 
              "เรเปีย": {"str": 3, "int": 0, "agi": 9, "skill": {"ยก": {}, "ชิด": {}, "จ้วง": {}, "แทง": {}}},
              "ดาบยักษ์": {"str": 10, "int": 0, "agi": -1, "skill": {"ฟันตรงแบบแรง!!!": {}, "": {}, "": {}, "": {}}}, 
              "ดาบสามมือ": {"str": 8, "int": 0, "agi": 5, "skill": {"ฟันสามต่อ": {}, "": {}, "": {}, "": {}}}, 
              "สมุดเวทย์": {"str": 0, "int": 5, "agi": 3, "skill": {"ลูกบอลไฟ": {}, "": {}, "": {}, "": {}}}, 
              "คฑาเวทย์": {"str": 0, "int": 10, "agi": -1, "skill": {"ลมเฉือน": {}, "": {}, "": {}, "": {}}}, 
              "ตะเกียงเวทย์": {"str": 0, "int": 7, "agi": 1, "skill": {"เวทแห่งแสง": {}, "": {}, "": {}, "": {}}}, 
              "ไม้กายสิทธิ์": {"str": 0, "int": 6, "agi": 7, "skill": {"เอสเปรสโซ่ปลาโตนุ่ม": {}, "อะวาเคดาบร้า": {}, "": {}, "": {}}}, 
              "ระเบิดเวทย์": {"str": 0, "int": 8, "agi": 5, "skill": {"แฟลชแบง": {}, "": {}, "": {}, "": {}}}}

def re_item():
    """rate drop item"""
    random_rate = random.choice(rate_drop)
    random_drop = random.choice(weapon_drop)
    gain = weapon[random_drop]
    if random_rate == "แย่":
        gain["str"] += -1
        gain["int"] += -1
        gain["agi"] += -1
    if random_rate == "ดีเยี่ยม":
        gain["str"] += 5
        gain["int"] += 5
        gain["agi"] += 5
    if random_rate == "ดีเยี่ยม":
        gain["str"] *= 2
        gain["int"] *= 2
        gain["agi"] *= 2
    return gain
def rate_legend():
    """rate drop legendary waepon"""
    if random.randrange(10) == random.randrange(10):
        legend = random.choice(legen_drop)
        return legend