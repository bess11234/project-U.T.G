"""item"""
#ผ่าน 5 ชั้น stat อาวุธ จะเพิ่มขึ้น 5 stat
def item():
    """item in game Ultimate tower super ultra Character Galaxy of god"""
    import random
    rate_drop = ["แย่", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "ดีเยี่ยม", "ดีเยี่ยม", "ดีเยี่ยม", "ตำนานจนละเอียด"]
    weapon = {"ดาบ": {"str": 5, "int": 0, "agi": 3, "skill": ["ฟันตรง", "ยกชิดจ้วงแทง"]}, 
              "สมุดเวท": {"str": 0, "int": 5, "agi": 3, "skill": ["เวทธาตุ", ""]}, 
              "หอก": {"str": 6, "int": 0, "agi": 4, "skill": ["แทงตรง", "ยกชิดจ้วงแทง"]}, 
              "ดาบยักษ์": {"str": 10, "int": 0, "agi": -1, "skill": ["ฟันตรงแบบแรง!!!", ""]}, 
              "ดาบสามมือ": {"str": 8, "int": 0, "agi": 5, "skill": ["ฟันสามต่อ", ""]}}