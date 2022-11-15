import status as st
import item as it
import tutorial as tu
"""Ultimate tower super ultra Character Galaxy of god (UTG)"""
def power_player_items(status_player, weapon_status):
    status_player['str'] += weapon_status["str"]
    status_player['int'] += weapon_status["int"]
    status_player['agi'] += weapon_status["agi"]

def power_player(status_player, stack_player, weapon_status):
    status_player['hp'] += stack_player
    status_player['hp'] += status_player['str']*5 - weapon_status['str']*5
    status_player['mp'] += status_player['int']*5 - weapon_status['int']*5
    
def power_mon(mon, stack):
    mon['str'] += stack
    mon['int'] += stack
    mon['hp'] += mon['str']*5
    mon['mp'] += mon['int']*5

def inside_tower(level, weapon_status, name):
    """tower"""
    stack_mon, stack_player = 0, 0

    while level != 51:
        stack_mon += 1 + level//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        stack_player += 5
        status_mon = st.Monster[st.random_mon].copy()
        status_player = st.Player.copy()
        power_player_items(stack_player, weapon_status)
        power_mon(status_mon, stack_mon)
        power_player(status_player, stack_player, weapon_status)

        level += 1
def tower(object, choice, name):
    """เล่น"""
    level = 1
    if object == "ดาบเก่าๆ":
        object = it.weapon["ดาบ"].copy()
    if object == "สมุดเวทผุๆ":
        object = it.weapon["สมุดเวท"].copy()
    if choice == "2":
        tu.tutorial(level, object, name)
    else:
        inside_tower(level, object, name)
def main_story():
    """main story"""
    print("""ณ โลกที่แสนสงบสุข ได้มีวิญญาณร้ายกลายร่่างเสกหอคอยแห่งความชั่วร้ายขึ้นมาหวังที่จะทำลายร้างโลกทิ้งไป
พระราชาจึงได้ประกาศว่า ใครที่สามารถทำลายหอคอยนี้ทิ้งได้จะบันดาลคำขอให้ 3 อย่าง นับแต่นั้นเป็นต้นมา
โลกก็ได้เข้าสู่ยุคสมัยของผู้กล้า ทุกคนต่างรวมตัวกันเพื่อที่จะทำลายหอคอย\n""")
    #เลือกอาวุธ
    print("ท่านอยากใช้สิ่งใดเป็นอาวุธ")
    print("1 ดาบเก่าๆ, 2 สมุดเวทผุๆ")
    while True:
        choice = input("กรุณาเลือกอาวุธ : ")
        if choice == "1":
            weapon = "ดาบเก่าๆ"
            break
        elif choice == "2":
            weapon = "สมุดเวทผุๆ"
            break
        else:
            print("เฮ้ นั้นมันไม่ใช่อาวุธที่นายมีอยู่นะ!!!")
    #บอกชื่อและถามว่าจะข้ามบทฝึกสอนรึเปล่า
    print("ท่านก็เป็นคนคนหนึ่งที่กำลังจะเข้าสู่หอคอยทันใดนั้นก็มีเสียงเข้ามาในหัว")
    print('เสียงลึกลับ: "ท่านมีนามว่าอะไร?"')
    name = input("ชื่อของคุณ : ")
    print("เสียงลึกลับ: \"ว้าวววว!!! ท่าน %s ท่านช่างดูสง่าราศี ข้าคือ [พระเจ้า] ไม่ทราบว่าท่านเป็นผู้กลับชาติมาเกิดใช่รึไม่?\""%name)
    print("อธืบาย:ผู้กลับชาติมาเกิดหรือก็คือท่านเคยเล่นเกมนี้หรือไม่ตัวเกมจะได้สอนระบบบื้องต้น\n")
    print("1 ใช่แล้วฉันนี้้แหละผู้กลับชาติมาเกิด!!!, 2 อ่อไม่ใช่อะ")
    while True:
        choice = input("กรุณาเลือกตัวเลือก : ")
        if choice == "1":
            print()
            break
        elif choice == "2":
            print()
            break
        else:
            print("เฮ้ ที่นี้เราไม่ทำกันแบบนั้น!!!")
    tower(weapon, choice, name)
main_story()
