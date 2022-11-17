import status as st
import item as it
import sys, time
import climage
import keyboard
import random
god = "\033[1;33;40m[พระเจ้า]\033[0;37;40m"
"""Ultimate tower super ultra Character Galaxy of god (UTG)"""
def fighting(mon, status_player, status_mon):
    """ต่อสู้"""
    atk_player = random.randrange(status_player["str"]-4, status_player["str"]+2)
    atk_mon = random.randrange(status_mon["str"]-4, status_mon["str"]+2)
    typing("-"*24)
    print("""\nพบเจอ %s แล้ว!!"""%mon)
    typing("-"*24)
    while True:
        print("\n%s\nHP : %d\n"%(mon, status_mon['hp']))
        print("%s\nHP : %d/%d\nMP : %d/%d\n"%(st.Player["name"], status_player["hp"], status_player["max_hp"], status_player["mp"], status_player["max_mp"]))
        print("1 : โจมตีปกติ")
        print("2 : ใช้สกิล/ท่า")
        print("3 : ใช้ไอเทม")
        action = input("กรุณาเลือกตัวเลือก : ")
        
        if action == "1":
            action = "โจมตีปกติ"
            status_mon['hp'] -= atk_player
        
        if status_mon['hp'] <= 0:
            typing("-"*24)
            print("""\nปราบ %s แล้ว!!"""%mon)
            #***********สุุ่มพวกอาวุธ สุ่ม potion ที่จะได้**********
            typing("-"*24+"\n")
            return
        typing("-"*24)
        print("\nคุณได้ %s ใส่ %s\nทำดาเมจ %d"%(action, mon, atk_player))
        typing("-"*24)

def typing(text):
    """ตัวหนังสือค่อยๆแสดง"""
    for i in text:
        if keyboard.is_pressed("esc"):
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)

def tutorial(level, weapon_status, stack_mon, stack_weapon, player_item, point_player, weapon_rate):
    """hello newbie"""
    mon = "Slime"
    status_mon = st.Monster[mon]
    status_player = st.Player.copy()
    random_image = random.choice(["blue_slime.png", "green_slime.png", "nerd_slime.png", "purple_slime.png", "red_slime.png"])
    output = climage.convert('monster\\'+random_image, is_unicode=True, width=45)
    
    typing("%s : \"ฮึ่มม... แปลกจริงนะข้ารับรู้ได้ถึงพลังที่แข็งแกร่ง แต่เจ้าหาใช่ผู้ย้อนกลับงั้นรึ ถ้าอย่างงั้นข้าจะสอนเจ้าเองนี้เพราะข้าเห็นว่าเจ้ามีแววหรอกนะ\"\n"%god)
    print("\nขณะนี้คุณได้เข้ามสู่ชั้น 1")
    typing("%s : \"เอาล่ะจ้าได้เข้าสู่ชั้นแรกแล้วลองไปสู้กับมอนนั้นเพื่อทะยานไปชั้นต่อไปเลย!!!\"\n"%god)
    print()
    
    while level < 10:
        if level == 0:
            typing("***คุณสามารถที่จะใช้ไอเทม เพื่อเพิ่ม HP, MP หรือคุณสามารถที่จะอัพพอยต์เพื่อเพิ่มความแข็งแกร่งให้ตัวละครคุณ \033[1;31;40mก่อนจะสู้กับมอนเตอร์\033[0;37;40m***\n\n")
            point_player, status_player = choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon, 1)
            print("-"*24)
            print("""พบเจอมอนเตอร์ %s แล้ว!!\nHP :\t%d"""%(mon, status_mon["hp"]))
            print("-"*24)
            print(output)
            
            #print("""
#ท่านจะทำอะไรดี
#1 : ลองเข้าไปลูบ
#2 : แจ้งตำรวจ
#3 : โทรหาแม่
#4 : สวดมนต์""")
#            choice = input()
#            while True:
#                if choice in ["1", "2" , "3", "4"]:
#                    break
#                else:
#                    print("เฮ้ นั้นทำไม่ได้นะ")
#                    break # break แปป ลบบรรทัดนี้ได้
#            print("""สไลม์น้อย ใช้ท่าอัดกระแทกกก!
#%s : \"เดี๋ยวๆๆๆๆๆๆ นี้เจ้าตั้งใจจริงปะเนี่ย รอบหน้าเอาให้จริงขังหน่อยเซ่!\"
#ท่านจะทำอะไรดี?
#1 2 3 4 """%god)
        level += 1
    return level, 1, stack_mon, stack_weapon, player_item, point_player

def choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon, guide=0):
    while True:
        print("สู้ต่อเลยหรือไม่ ?")
        print("1 : สู้เลย"+"\t (เลือกที่จะสู้ต่อเมื่อคุณเตรียมพร้อมเสร็จแล้ว)"*guide)
        print("2 : เปิดกระเป๋า"+"\t(เลือกที่จะเปิดกระเป๋าเพื่อใช้งานไอเทม)"*guide)
        print("3 : อัพสเตตัส"+"\t(เลือกที่จะใช้ พอยต์ ของคุณเพื่อเพิ่มความสามารถของตัวละคร **พอยต์จะเพิ่มทุกๆ 5 หน่วยต่อ 1 ชั้น **พอยต์จะเพิ่ม 10 หน่วยต่อการชนะบอส 1 ตัว)"*guide)
        select = input("กรุณาเลือกตัวเลือก : ")

        if select == "1":
            return point_player, status_player

        elif select == "2":
            while True:
                if status_player['hp'] > status_player['max_hp']:
                    status_player['hp'] = status_player['max_hp']
                if status_player['mp'] > status_player['max_mp']:
                    status_player['mp'] = status_player['max_mp']
                typing("-"*24)
                typing("\nHP : %d/%d"%(status_player["hp"], status_player["max_hp"]))
                typing("\nMP : %d/%d\n"%(status_player["mp"], status_player["max_mp"]))
                typing("-"*24)
                print("\nกรุณาเลือกใช้ไอเทม")
                print("1 : HP Potion\t%d"%player_item['HP potion']+"  (การใช้งานขวดหนึ่งสามารถเพิ่ม HP ได้ 25%)"*guide)
                print("2 : MP Potion\t%d"%player_item['MP potion']+"  (การใช้งานขวดหนึ่งสามารถเพิ่ม MP ได้ 20%)"*guide)
                print("3 : กลับ")

                use = input("กรุณาเลือกใช้งานไอเทม : ")
                if use == "1" and player_item['HP potion'] != 0:
                    status_player['hp'] += status_player['max_hp']*25//100
                    player_item['HP potion'] -= 1
                elif use == "2" and player_item['MP potion'] != 0:
                    status_player['mp'] += status_player['max_mp']*20//100 
                    player_item['MP potion'] -= 1
                elif (use == "1" or use == "2") and (player_item['HP potion'] == 0 or  player_item['MP potion'] == 0):
                    print("คุณไม่มี HP potion ให้ใช้"*(use == "1")+"คุณไม่มี MP potion ให้ใช้"*(use == "2"))
                    time.sleep(1)
                elif use == "3":
                    typing("-"*24+"\n")
                    break
                else:
                    print("ไม่มีตัวเลือกนี้")

        elif select == "3":
            point_player, status_player = upgrade_pointplayer(point_player, status_player, weapon_status, weapon_rate, stack_weapon, guide)

        else:
            print("ไม่มีตัวเลือกนี้")

def upgrade_pointplayer(point_player, status_player, weapon_status, weapon_rate, stack_weapon, guide=0):
    while True:
        control = 1
        typing("-"*24)
        print("\nHP :\t%d/%d\nMP :\t%d/%d\nSTR :\t%d\nAGI :\t%d\nINT :\t%d"\
            %(status_player['hp'], status_player['max_hp'], status_player['mp'], status_player['max_mp'], status_player['str'], status_player['agi'], status_player['int']))#ถ้าอัพค่าใดค่าหนึ่งแล้วค่านั้นจะมีผลเลย
        print("\nPoint : %d"%point_player)
        print("กรุณาเลือกค่าที่จะอัพ")
        print("1 : STR"+"\t(ค่า STR จะเป็นการเพิ่มดาเมจกายภาพ และเพิ่ม MAX HP)"*guide)
        print("2 : AGI"+"\t(ค่า AGI จะเป็นการเพิ่มจำนวนรอบในการโจมตีก่อน หรือใครที่จะได้ตีก่อน)"*guide)
        print("3 : INT"+"\t(ค่า STR จะเป็นการเพิ่มดาเมจเวท และเพิ่ม MAX MP)"*guide)
        print("4 : กลับไปหน้าหลัก")
        typing("-"*24+"\n")
        want_upgrade = input("กรุณาเลือกตัวเลือก : ")
    #*****แก้ให้เวลาอัพ แล้วแสดงทันที*****
        if want_upgrade == "1" and point_player != 0:
            print("\nจะอัพกี่พอยต์ ? \nพิมพ์ b เพื่อกลับไปหน้าอัพสเตตัส")
            spent_point = input("จำนวนพอยต์ที่จะใช้ : ").lower()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                st.Player['str'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "2" and point_player != 0:
            print("\nจะอัพกี่พอยต์ ? \nพิมพ์ b เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input("จำนวนพอยต์ที่จะใช้ : ").lower()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                st.Player['agi'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "3" and point_player != 0:
            print("\nจะอัพกี่พอยต์ ? \nพิมพ์ b เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input("จำนวนพอยต์ที่จะใช้ : ").lower()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                st.Player['int'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "4":
            typing("-"*24+"\n")
            return point_player, status_player

        if point_player == 0:
            typing("\nพอยต์ไม่พอ\n"*control)
        
        elif point_player < int(spent_point):
            typing("\nพอยต์ไม่พอ\n"*control)

        status_player = st.Player.copy()

        power_player_items(status_player, weapon_status, weapon_rate, stack_weapon, 0)
        power_player(status_player)

def power_player_items(status_player, weapon_status, weapon_rate, stack_weapon, control=1):
    weapon_status['str'] += stack_weapon*control
    weapon_status['int'] += stack_weapon*control
    weapon_status['agi'] += stack_weapon*control

    if weapon_rate == "แย่" and control == 1:
        weapon_status["str"] += -1
        weapon_status["int"] += -1
        weapon_status["agi"] += -1

    if weapon_rate == "ดีเยี่ยม" and control == 1:
        weapon_status["str"] += 5
        weapon_status["int"] += 5
        weapon_status["agi"] += 5

    if weapon_rate == "ดีเยี่ยม" and control == 1:
        weapon_status["str"] *= 2
        weapon_status["int"] *= 2
        weapon_status["agi"] *= 2

    status_player['str'] += weapon_status['str']
    status_player['int'] += weapon_status['int']
    status_player['agi'] += weapon_status['agi']

def power_player(status_player):
    status_player['max_hp'] += status_player['str']*5
    status_player['max_mp'] += status_player['int']*5
    status_player['hp'] += status_player['str']*5
    status_player['mp'] += status_player['int']*5
    if status_player["hp"] > status_player["max_hp"]:
        status_player["hp"] = status_player["max_hp"]
    if status_player["mp"] > status_player["max_mp"]:
        status_player["mp"] = status_player["max_mp"]

def power_mon(mon, stack, mon_type):
    mon['str'] += stack
    mon['int'] += stack
    mon['hp'] += mon['str']*5
    mon['mp'] += mon['int']*5

    if mon_type == "Boss":
        mon['hp'] += mon['hp']*50//100
        mon['mp'] += mon['mp']*50//100
        mon['str'] += mon['str']*50//100
        mon['agi'] += mon['agi']*50//100
        mon['int'] += mon['int']*50//100
        mon_type = "\033[1;31;40m"+mon_type+"\033[0;37;40m"

    elif mon_type == "Miniboss":
        mon['hp'] += mon['hp']*25//100
        mon['mp'] += mon['mp']*25//100
        mon['str'] += mon['str']*25//100
        mon['agi'] += mon['agi']*25//100
        mon['int'] += mon['int']*25//100
        mon_type = "\033[1;36;40m"+mon_type+"\033[0;37;40m"

    if mon_type != "":
        mon['name'] = mon_type+" "+mon['name']

def inside_tower(level, weapon_status, choice):
    """tower"""
    weapon_rate = ""
    stack_mon, stack_weapon = 0, 0
    player_item = {"HP potion" : 0, "MP potion" : 0}
    point_player = 0

    while level != 50:
        if choice == "2":
            level, choice, stack_mon, stack_weapon, player_item, point_player = \
            tutorial(level, weapon_status, stack_mon, stack_weapon, player_item, point_player, weapon_rate)
        if level != 0:
            weapon_status, weapon_rate, weapon_name = it.re_item()#สุ่มไอเทม
        mon_type = ""
        mon = st.re_mon() #สุ่มมอนที่จะสู้
        stack_mon += 1 + level//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        stack_weapon += 1
        if level%10 == 0 and level != 0:
            mon_type = "Boss"
        elif level%5 == 0 and level != 0:
            mon_type = "Miniboss"
        if level%10 == 1 and level != 1:
            for i in st.Monster:
                st.Monster[i]["agi"] += 10
            point_player += 10

        status_mon = st.Monster[mon].copy()
        status_player = st.Player.copy()

        power_player_items(status_player, weapon_status, weapon_rate, stack_weapon)
        power_player(status_player)
        power_mon(status_mon, stack_mon, mon_type)

        point_player, status_player = choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon)

        fighting(mon, status_player, status_mon)
        
        
        
        level += 1
        st.Player["max_hp"] += 5
        st.Player["hp"] += 5
        point_player += 5

def tower(object, choice):
    """เล่น"""
    level = 0
    if object == "ดาบเก่าๆ":
        object = it.weapon["ดาบ"].copy()
    if object == "สมุดเวทย์ผุๆ":
        object = it.weapon["สมุดเวทย์"].copy()

    inside_tower(level, object, choice)

def main_story():
    """main story"""
    choice = ""
    print("\n\033[0;34;40m***กดปุ่ม Esc เพื่อ Skip***\n\033[0;37;40m")
    typing("ณ โลกที่แสนสงบสุข ได้มีวิญญาณร้ายกลายร่างเสกหอคอยแห่งความชั่วร้ายขึ้นมาหวังที่จะทำลายร้างโลกทิ้งไป")
    typing("\nพระราชาจึงได้ประกาศว่า ใครที่สามารถทำลายหอคอยนี้ทิ้งได้จะบันดาลคำขอให้ 3 อย่าง นับแต่นั้นเป็นต้นมา")
    typing("\nโลกก็ได้เข้าสู่ยุคสมัยของผู้กล้า ทุกคนต่างรวมตัวกันเพื่อที่จะทำลายหอคอย")
    #เลือกอาวุธ
    typing("\n\nท่านอยากใช้สิ่งใดเป็นอาวุธ")
    print("\n1 : ดาบเก่าๆ\n2 : สมุดเวทย์ผุๆ")
    while True:
        choice = input("กรุณาเลือกอาวุธ : ")
        if choice == "1":
            weapon = "ดาบเก่าๆ"
            break
        elif choice == "2":
            weapon = "สมุดเวทย์ผุๆ"
            break
        elif choice != "":
            print("เฮ้ นั้นมันไม่ใช่อาวุธที่มีอยู่นะ!!!\n")
    typing("-"*24)
    #บอกชื่อและถามว่าจะข้ามบทฝึกสอนรึเปล่า
    typing("\nท่านก็เป็นคนคนหนึ่งที่กำลังจะเข้าสู่หอคอยทันใดนั้นก็มีเสียงเข้ามาในหัว")
    typing('\n\033[1;30;40mเสียงลึกลับ\033[0;37;40m : "ท่านมีนามว่าอะไร?"\n')
    name = input("ชื่อของคุณ : ")
    typing("-"*24)
    st.Player['name'] = "\033[1;32;40m"+name+"\033[0;37;40m"
    typing("\n\033[1;30;40mเสียงลึกลับ\033[0;37;40m : \"ว้าวววว!!! ท่าน %s ท่านช่างดูสง่าราศี ข้าคือ %s ไม่ทราบว่าท่านเป็นผู้กลับชาติมาเกิดใช่รึไม่?\""%(st.Player["name"], god))
    typing("\n\nอธิบาย : ผู้กลับชาติมาเกิดหรือก็คือท่านเคยเล่นเกมนี้หรือไม่ตัวเกมจะได้สอนระบบบื้องต้น\n")
    print("1 : ใช่แล้วฉันนี้้แหละผู้กลับชาติมาเกิด!!! (เคยเล่น)\n2 : อ่อไม่ใช่อะ (ไม่เคยเล่น)\n3 : ออกจากหอคอย")

    while True:
        choice = input("กรุณาเลือกตัวเลือก : ")
        if choice == "1":
            print("\n"+"*"*12)
            break
        elif choice == "2":
            print("\n"+"*"*12)
            break
        elif choice == "3":
            break
        else:
            print("เฮ้ ที่นี้เราไม่ทำกันแบบนั้น!!!\n")
    if choice == "3":
        print("ออกไวจริงเชียว")
        return
    typing("-"*24+"\n")
    tower(weapon, choice)
main_story()