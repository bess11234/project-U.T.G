import status as st
import item as it
import tutorial as tu
"""Ultimate tower super ultra Character Galaxy of god (UTG)"""
def choice(status_player, point_player, player_item):
    while True:
        print("จะกลับไปสู้ต่อหรือไม่ ? \n1 = สู้ต่อ\n2 = เปิดไอเทม\n3 = อัพพ๊อยต์ \n4 = ออก")
        select = input()
        if select == "1":
            return
        elif select == "2":
            while True:
                print("จะเลือกใช้อะไร 1 = HP Potion:\t%d\n2 = MP:\t%d\n3 = กลับ"%(player_item['HP potion'], player_item['MP potion']))
                use = input()
                if use == "1" and player_item['HP potion'] != 0:
                    status_player['hp'] += status_player['hp']*25//100
                    player_item['HP potion'] -= 1
                elif use == "2" and player_item['MP potion'] != 0:
                    status_player['mp'] += status_player['mp']*20//100 
                    player_item['MP potion'] -= 1
                elif use == "3":
                    choice(status_player, point_player, player_item)
                else:
                    print("คุณป้อนผิด")
        elif select == "3":
            pointplayer = upgrade_pointplayer(point_player,status_player )
        elif select == "4":
            return point_player
        else:
            choice(status_player, point_player, player_item)
def upgrade_pointplayer(point_player,status_player ):
    while True:
        print("HP =\t%d\nMP =\t%d\nSTR =\t%d\nAGI =\t%d\nINT =\t%d"%(status_player['hp'],status_player['mp'],st.Player['str'],st.Player['agi'],st.Player['int']))#ถ้าอัพค่าใดค่าหนึ่งแล้วค่านั้นจะมีผลเลย
        print("Point : %d\nกรุณาเลือกค่าที่จะอัพ \n1 = str \n2 = agi\n3 = int\n4 = กลับไปหน้าหลัก"%point_player)
        want_upgrade = input()
        if want_upgrade == "1":
            print("จะอัพกี่พอยต์ ? \n พิมพ์ Back เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input().lower()
            if spent_point.isdecimal():
                st.Player['str'] += int(spent_point)
                point_player -= int(spent_point)
            else:
                upgrade_pointplayer(point_player)

        elif want_upgrade == "2":
            print("จะอัพกี่พอยต์ ? \n พิมพ์ Back เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input().lower()
            if spent_point.isdecimal():
                st.Player['agi'] += int(spent_point)
                point_player -= int(spent_point)
            else:
                upgrade_pointplayer(point_player)

        elif want_upgrade == "3":
            print("จะอัพกี่พอยต์ ? \n พิมพ์ Back เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input().lower()
            if spent_point.isdecimal():
                st.Player['int'] += int(spent_point)
                point_player -= int(spent_point)
            else:
                upgrade_pointplayer(point_player)

        elif want_upgrade == "4":
            return point_player

        else:
            upgrade_pointplayer(point_player)

def power_player_items(status_player, weapon_status, weapon_rate, stack_weapon):
    weapon_status['str'] += stack_weapon
    weapon_status['int'] += stack_weapon
    weapon_status['agi'] += stack_weapon

    if weapon_rate == "แย่":
        weapon_status["str"] += -1
        weapon_status["int"] += -1
        weapon_status["agi"] += -1

    if weapon_rate == "ดีเยี่ยม":
        weapon_status["str"] += 5
        weapon_status["int"] += 5
        weapon_status["agi"] += 5

    if weapon_rate == "ดีเยี่ยม":
        weapon_status["str"] *= 2
        weapon_status["int"] *= 2
        weapon_status["agi"] *= 2

    status_player['str'] += weapon_status['str']
    status_player['int'] += weapon_status['int']
    status_player['agi'] += weapon_status['agi']

def power_player(status_player, weapon_status):
    st.Player["hp"] += 5
    status_player['hp'] += status_player['str']*5 - weapon_status['str']*5
    status_player['mp'] += status_player['int']*5 - weapon_status['int']*5

def power_mon(mon, stack, mon_type):
    mon['str'] += stack
    mon['int'] += stack
    mon['hp'] += mon['str']*5
    mon['mp'] += mon['int']*5

    if mon_type == "Superboss":
        mon['hp'] += mon['hp']*50//100
        mon['mp'] += mon['mp']*50//100
        mon['str'] += mon['str']*50//100
        mon['agi'] += mon['agi']*50//100
        mon['int'] += mon['int']*50//100

    elif mon_type == "Miniboss":
        mon['hp'] += mon['hp']*25//100
        mon['mp'] += mon['mp']*25//100
        mon['str'] += mon['str']*25//100
        mon['agi'] += mon['agi']*25//100
        mon['int'] += mon['int']*25//100

def inside_tower(level, weapon_status, name):
    """tower"""
    weapon_rate = ""
    stack_mon, stack_weapon = 0, 0
    player_item = {"HP potion" : 0, "MP potion" : 0}
    point_player = 0

    while level != 50:
        if level != 0:
            weapon_status, weapon_rate, weapon_name = it.re_item()#สุ่มไอเทม
        mon_type = ""
        mon = st.re_mon() #สุ่มมอนที่จะสู้
        stack_mon += 1 + level//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        stack_weapon += 1

        if level%10 == 0 and level != 0:
            mon_type = "Superboss"
        elif level%5 == 0 and level != 0:
            mon_type = "Miniboss"
        if level%10 == 1 and level != 1:
            for i in st.Monster:
                st.Monster[i]["agi"] += 10
            point_player += 10

        status_mon = st.Monster[mon].copy()
        status_player = st.Player.copy()
        
        choice(status_player, point_player, player_item)

        power_player_items(status_player, weapon_status, weapon_rate, stack_weapon)
        power_mon(status_mon, stack_mon, mon_type)
        power_player(status_player, weapon_status)

        print("""พบเจอมอนเตอร์ %s แล้ว!!\nHP : \t%d\n"""%(mon, status_mon["hp"]))

        level += 1
        point_player += 5

def tower(object, choice, name):
    """เล่น"""
    level = 0
    if object == "ดาบเก่าๆ":
        object = it.weapon["ดาบ"].copy()
    if object == "สมุดเวทย์ผุๆ":
        object = it.weapon["สมุดเวทย์"].copy()

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
    print("1 ดาบเก่าๆ, 2 สมุดเวทย์ผุๆ")
    while True:
        choice = input("กรุณาเลือกอาวุธ : ")
        if choice == "1":
            weapon = "ดาบเก่าๆ"
            break
        elif choice == "2":
            weapon = "สมุดเวทย์ผุๆ"
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
