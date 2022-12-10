import sys, time, os
import climage
import keyboard
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
                color = ["ant\\ant_blue.png", "ant\\ant_green.png", "ant\\ant_purple.png"]
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
                color = ["lizard\\purple_lizard.png", "lizard\\rainbow_lizard.png", "lizard\\blue_lizard.png"]
                color = random.choice(color)
                return color
        if mon == "Ancient Robot":
                color = ["ruin_guard\\blue_ruin_guard.png", "ruin_guard\\red_ruin_guard.png", "ruin_guard\\christmas_ruin_guard.png"]
                color = random.choice(color)
                return color

rate_drop = ["แย่", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "งั้นๆ", "ดีเยี่ยม", "ดีเยี่ยม", "ดีเยี่ยม", "ตำนานจนละเอียด"]
#ถ้ามีเวลาค่อยใส่ของกวนๆ
potion_drop = ["Potion HP", "Potion HP", "Potion HP", "Potion MP", "Potion MP", "Potion MP", "แว่นตาที่แตกพ่ายของผู้สร้าง", "ลุงตูบที่อยู่บ้านข้างๆ", "กระป๋องน้ำซ่าชื่นใจ", "ความรักที่คุณให้เขาไปแต่เขาไม่ให้เคยให้อะไรกลับมา"]
legen_drop = ["กิ้งไม้แห่งสัจธรรม", "สว่านทะลวงสวรรค์"]
weapon_drop = ["ดาบ", "เรเปีย", "สมุดเวทย์", "หอก", "ดาบยักษ์", "ดาบสามมือ", "คฑาเวทย์", "ตะเกียงเวทย์", "ไม้กายสิทธิ์", "ระเบิดเวทย์"]

weapon_legendary = {"กิ้งไม้แห่งสัจธรรม":{"str": 1000, "int": 1000, "agi": 50, "skill":{"ความจริงมีเพียงหนึ่งเดียว!": (1000, 2, 5, "i")}}, 
                    "สว่านทะลวงสวรรค์":{"str": 1000, "int": 1000, "agi": 60, "skill":{"บุกทะลวงเข้าไป!": (1200, 1, 5, "s")}}, 
                    "":""}
weapon_secret = {"9 มม.ฝังเวทย์":{"str": 2000, "int": 2000, "agi": 20, "skill":{"นี้แหละวิธีแก้ปัญหาที่ดีที่สุด": (2000, 1, 5, "i")}}}
weapon = {"ดาบ": {"str": 5, "int": 0, "agi": 3, "skill": {"ฟันตรง": (4, 5, 1.1, "s"), "ดาบเฉือนลม": (16, 5, 1.5, "s"), "ฟันแหลก": (35, 10, 2, "s"), "ดาบสั่งตายใจสั่งมา": (300, 50, 3, "s")}}, 
              "หอก": {"str": 6, "int": 0, "agi": 4, "skill": {"แทงตรง": (4, 5, 1.1, "s"), "ทะลวงเข้าไป!": (16, 10, 1.5, "s"), "ควงสว่าน": (50, 15, 2, "s"), "เฮลิปเตอร์!": (350, 40, 3, "s")}}, 
              "เรเปีย": {"str": 3, "int": 0, "agi": 9, "skill": {"ยก": (2, 5, 1.1, "s"), "ชิด": (19, 4, 1.5, "s"), "จ้วง": (60, 30, 2, "s"), "แทง!": (350, 50, 3, "s")}}, 
              "ดาบยักษ์": {"str": 10, "int": 0, "agi": -1, "skill": {"ฟันตรงแบบแรง!": (6, 5, 1.1, "s"), "ตบลอย": (25, 15, 1.5, "s"), "ถล่มพสุธา": (70, 30, 2, "s"), "ผ่าปฐพี": (500, 150, 3, "s")}}, 
              "ดาบสามมือ": {"str": 8, "int": 0, "agi": 5, "skill": {"ฟันสามต่อ": (5, 5, 1.1, "s"), "ตัดผ่าอากาศสามต่อ": (15, 6, 1.5, "s"), "เพลงดาบสายลม 36 ประกาศ": (100, 40, 2, "s"), "อาชูรา": (450, 120, 4, "s")}}, 
              "สมุดเวทย์": {"str": 0, "int": 5, "agi": 3, "skill": {"ลูกบอลไฟ": (3, 5, 1.5, "i"), "สายฟ้าฟาด": (35, 25, 2, "i"), "เกมลงทัณฑ์แห่งความมืด": (60, 60, 3, "i"), "อ่านหนังสือซะบ้างเซ่!": (400, 125, 4, "i")}}, 
              "คฑาเวทย์": {"str": 0, "int": 10, "agi": -1, "skill": {"คฑาเสริมเวทย์ฟาดไม่ยั้ง": (4, 5, 1.5, "i"), "ลมเฉือน": (29, 11, 2, "i"), "ไปคุยกับรากมะม่วง!": (80, 70, 3, "i"), "ตัวแทนแห่งวันจันทร์จะลงทัณฑ์แกเอง": (500, 150, 4, "i")}}, 
              "ตะเกียงเวทย์": {"str": 0, "int": 7, "agi": 1, "skill": {"เวทแห่งแสง": (3, 5, 1.5, "i"), "พาาาลังงงคลื่นนเต่าาาา!": (35, 15, 2, "i"), "ดาบผนึกแห่งแสง": (75, 65, 3, "i"), "บอลเกงกิ": (450, 125, 4, "i")}}, 
              "ไม้กายสิทธิ์": {"str": 0, "int": 6, "agi": 7, "skill": {"สติลไวไฟ": (4, 5, 1.5, "i"), "ร้ายกาจจจ": (50, 20, 2, "i"), "เอสเปรสโซ่ปลาโตนุ่ม": (100, 65, 3, "i"), "อะวาเคดาบร้า": (499, 149, 4, "i")}}, 
              "ระเบิดเวทย์": {"str": 0, "int": 8, "agi": 5, "skill": {"ประทัด": (3, 5, 1.5, "i"), "ระเบิดมือ": (30, 21, 2, "i"), "ทีเอ็นที": (100, 60, 3, "i"), "ระเบิดเวลาอ๊ากกกกกก!": (499, 149, 4, "i")}}}

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

god = "\033[1;33;40m[พระเจ้า]\033[0;0;0m"
def fixed(status_player):
    """ปรับ hp"""
    if status_player['hp'] > status_player['max_hp']:
        status_player['hp'] = status_player['max_hp']
    if status_player['mp'] > status_player['max_mp']:
        status_player['mp'] = status_player['max_mp']
    if Player["hp"] > Player["max_hp"]:
        Player["hp"] = Player["max_hp"]
    if Player["mp"] > Player["max_mp"]:
        Player["mp"] = Player["max_mp"]

"""Ultimate tower super ultra Character Galaxy of god (UTG)"""
def mon_use_skill(status_mon, unlock_skill):
    """มอนใช้สกิล"""
    tmp_skill = [i[1] for i in zip(range(1, unlock_skill), status_mon["skill"]) if status_mon["skill"][i[1]][1] <= status_mon["mp"]]
    if tmp_skill == []:
        tmp_skill = [None]
    else:
        tmp_skill = random.choice(tmp_skill)
        tmp_skill = [tmp_skill, status_mon["skill"][tmp_skill]]
    return tmp_skill

def use_item(status_player, player_item, guide=0, tmp=0):
    """ใช้ไอเทม"""
    while True:
        typing("\n\033[0;49;31mHP\033[0;0;0m : %02d/%02d"%(status_player["hp"], status_player["max_hp"]))
        typing("\n\033[0;49;34mMP\033[0;0;0m : %02d/%02d\n"%(status_player["mp"], status_player["max_mp"]))
        typing("\n"+"-"*24)
        print("\n")
        print("1 : Potion HP %02d"%player_item['HP potion']+"  (การใช้งานขวดหนึ่งสามารถฟื้นฟู \033[0;49;31mHP\033[0;0;0m ได้ 25%)"*guide)
        print("2 : Potion MP %02d"%player_item['MP potion']+"  (การใช้งานขวดหนึ่งสามารถฟื้นฟู \033[0;49;34mMP\033[0;0;0m ได้ 20%)"*guide)
        print("3 : กลับ\n")

        typing("-"*24+"\n")
        use = input("กรุณาเลือกใช้งานไอเทม : ").strip()

        if use == "1" and player_item['HP potion'] != 0:
            status_player['hp'] += status_player['max_hp']*25//100
            Player["hp"] += status_player["max_hp"]*25//100
            player_item['HP potion'] -= 1
            typing("-"*24+"\n")
            print("\nคุณได้ใช้ Potion HP ฟื้นฟูเลือด \033[0;49;31m%d\033[0;0;0m\n"%(status_player['max_hp']*25//100))
            typing("-"*24+"\n")
            fixed(status_player)
            if tmp == 1:
                return 1

        elif use == "2" and player_item['MP potion'] != 0:
            status_player['mp'] += status_player['max_mp']*20//100
            Player["mp"] += status_player["max_mp"]*20//100
            player_item['MP potion'] -= 1
            typing("-"*24+"\n")
            print("\nคุณได้ใช้ Potion MP ฟื้นฟูมานา \033[0;49;34m%d\033[0;0;0m\n"%(status_player['max_mp']*20//100))
            typing("-"*24+"\n")
            fixed(status_player)
            if tmp == 1:
                return 1

        elif (use == "1" or use == "2") and (player_item['HP potion'] == 0 or  player_item['MP potion'] == 0):
            print("\033[0;49;90m**คุณไม่มี Potion HP ให้ใช้**\033[0;0;0m"*(use == "1")+"\033[0;49;90m**คุณไม่มี Potion MP ให้ใช้**\033[0;0;0m"*(use == "2"))
            typing("-"*24+"\n")

        elif use == "3":
            typing("-"*24)
            break

        else:
            print("\033[0;49;90m**ไม่มีตัวเลือกนี้**\033[0;0;0m")
            typing("-"*24+"\n")
    return 0

def use_skill(status_player, weapon_status, tmp_skill, unlock_skill):
    """ใช้สกิล"""
    print()
    for num, skill in zip(range(1, unlock_skill), weapon_status["skill"]):
        tmp_skill.update({str(num) : (skill, weapon_status["skill"][skill][0], weapon_status["skill"][skill][1], weapon_status["skill"][skill][2], weapon_status["skill"][skill][3])})
    stop = max(list(map(int, list(tmp_skill))))+1
    while True:
        for i in tmp_skill:
            print("%s : %s \033[0;49;34mMP\033[0;0;0m %d"%(i, tmp_skill[i][0], tmp_skill[i][2]))
        print("%d : ย้อนกลับ\n"%stop)
        typing("-"*24+"\n")
        action = input("กรุณาเลือกสกิลที่จะใช้ : ").strip()
        if action in tmp_skill:
            #ทำปลดล็อคสกิลไว้ด้วย
            if status_player["mp"] >= tmp_skill[action][2]:
                Player["mp"] -= tmp_skill[action][2]
                status_player["mp"] -= tmp_skill[action][2]
                return action
            else:
                print("\033[0;49;34mMP\033[0;0;0mคุณไม่พอ")
                typing("-"*24+"\n")
        elif action == str(stop):
            return "Back"
        else:
            print("\nไม่มีสกิลนี้")
            typing("-"*24+"\n\n")
    

def fighting(mon, status_player, status_mon, weapon_status, player_item, unlock_skill, mon_type, guide=0):
    """ต่อสู้"""

    typing("-"*24+"\n")
    print("""\nพบเจอ %s แล้ว!!"""%mon)
    typing("\n"+"-"*24)
    image_mon = imagemon(mon.replace(mon_type+" ", ""))
    image_mon = climage.convert('monster\\'+image_mon, is_unicode=True, width=35)
    time.sleep(0.3)
    os.system('cls')
    typing("-"*24)
    turn_player = status_player["agi"]//status_mon["agi"]
    turn_monster = status_mon["agi"]//status_player["agi"]
    turn_player += 1*(turn_player == 0)
    turn_monster += 1*(turn_monster == 0)

    while True:
        for _ in range(turn_player):
            atk_player = random.randrange(status_player["str"]-4, status_player["str"]+2)
            while True:
                print("\n\n%s\n\033[2;49;31mHP\033[0;0;0m : %02d\n"%(mon, status_mon['hp']))
                print(image_mon)
                print("%s\n\033[0;49;31mHP\033[0;0;0m : %02d/%02d\n\033[0;49;34mMP\033[0;0;0m : %02d/%02d\n"%(Player["name"], status_player["hp"], status_player["max_hp"], status_player["mp"], status_player["max_mp"]))
                print("1 : โจมตีปกติ" + " (การโจมตีปกติจะคิด ดาเมจ จาก STR ทั้งหมดที่มี)"*guide)
                print("2 : ใช้สกิล" + " (การใช้สกิลจะคูณ ดาเมจ จาก STR หรือ INT ทั้งหมดที่มี)"*guide)
                print("3 : ใช้ไอเทม"+" (ใช้ไอเทมเพื่อฟื้นฟู \033[0;49;31mHP\033[0;0;0m หรือ \033[0;49;34mMP\033[0;0;0m)"*guide+"\n\033[0;49;90m**การใช้แต่ละตัวเลือกจะเสียจำนวนรอบ**\033[0;0;m"*guide+"\n")
                typing("-"*24+"\n")
                action = input("กรุณาเลือกตัวเลือก : ").strip()
                typing("-"*24+"\n")

                if action == "1":
                    action = "\033[1;49;33mโจมตีปกติ\033[0;0;0m"
                    status_mon['hp'] -= atk_player

                elif action == "2":
                    tmp_skill = {}
                    action = use_skill(status_player, weapon_status, tmp_skill, unlock_skill)
                    if action == "Back":
                        typing("-"*24)
                        continue
                    else:
                        atk_player = tmp_skill[action][1]
                        if tmp_skill[action][4] == "s":
                            atk_player += tmp_skill[action][3]*status_player["str"]
                        if tmp_skill[action][4] == "i":
                            atk_player += tmp_skill[action][3]*status_player["int"]
                        status_mon['hp'] -= int(atk_player)
                        action = "\033[1;49;34mสกิล"+tmp_skill[action][0]+"\033[0;0;0m"
                    typing("-"*24+"\n")

                elif action == "3":
                    check = use_item(status_player, player_item, guide, 1)
                    if check == 1:
                        break
                    else:
                        continue

                else:
                    print("\033[0;49;90m\n**ไม่มีตัวเลือกนี้**\n\033[0;0;0m")
                    typing("-"*24)
                    continue

                print("\nคุณได้ใช้ %s ใส่ %s\nดาเมจ %02d"%(action, mon, atk_player))
                typing("\n"+"-"*24)

                if status_mon['hp'] <= 0:
                    typing("""\n\n\033[0;49;31mคุณปราบ\033[0;0;0m %s \033[0;49;31mแล้ว!!\033[0;0;0m\n\n"""%mon)
                    #***********สุุ่มพวกอาวุธ สุ่ม potion ที่จะได้**********
                    drop = re_potion()
                    for i in drop:
                        print("คุณได้รับ %s"%i)
                        if i == "Potion HP":
                            item = climage.convert('item\\blood_potion.png', is_unicode=True, width=15)
                            player_item["HP potion"] += 1
                        elif i == "Potion MP":
                            item = climage.convert('item\\mana_potion.png', is_unicode=True, width=15)
                            player_item["MP potion"] += 1
                        else:
                            item = climage.convert('item\\glasses.png', is_unicode=True, width=15)
                        print(item)
                    input("กด Enter เพื่อรับ")
                    typing("\n"+"-"*24+"\n\n")
                    return
                break

        for _ in range(turn_monster):
            atk_mon = random.randrange(status_mon["str"]-4, status_mon["str"]+2) # มอนตี
            action = [1, 1, 1 ,1 ,1, 2, 2 ,2 ,1 , 1]
            action = random.choice(action)
            if action == 2:
                tmp_skill = mon_use_skill(status_mon, unlock_skill)
                if tmp_skill != [None]:
                    action = "\033[2;49;31mสกิล"+tmp_skill[0]+"\033[0;0;0m"
                    atk_mon = tmp_skill[1][0]
                    status_mon["mp"] -= tmp_skill[1][1]
                    if tmp_skill[1][3] == "s":
                        atk_mon += status_mon["str"]*tmp_skill[1][2]
                    if tmp_skill[1][3] == "i":
                        atk_mon += status_mon["int"]*tmp_skill[1][2]
                else:
                    action = 1

            if action == 1:
                action = "\033[0;49;90mโจมตีปกติ\033[0;0;0m"

            status_player["hp"] -= atk_mon
            Player["hp"] -= atk_mon

            print("\n\n%s ได้ใช้ %s ใส่ %s\nดาเมจ %02d"%(mon, action, Player["name"], atk_mon))
            typing("\n"+"-"*24+"\n")

            if status_player["hp"] <= 0 :
                return
        print("\033[0;49;90m\n"+"*"*128+"\n\033[0;0;0m")
        time.sleep(0.7)
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

def tutorial(level, weapon_status, stack_mon, stack_weapon, player_item, point_player, weapon_rate, unlock_skill):
    """hello newbie"""
    mon = "Slime"
    power_player_items(weapon_status, weapon_rate, stack_weapon)

    while level <= 10:
        tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name, tmp_legend, tmp_legend_status = "", "", "", "", ""
        mon_type = ""
        stack_mon += 1 + level//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        stack_weapon += 1

        if level > 1:
            mon = re_mon() #สุ่มมอนที่จะสู้
            if level%10 == 0:
                mon_type = "Boss"
            elif level%5 == 0:
                mon_type = "Miniboss"

        status_mon = Monster[mon].copy()

        os.system('cls')
        typing("-"*24+"\n\n")
        typing("\033[0;49;93mขณะนี้คุณได้เข้าสู่ชั้น\033[0;0;0m %d\n"%level)
        typing("\n"+"-"*24+"\n\n")
        if level == 1:
            typing("%s : ฮึ่มม... แปลกจริงนะข้ารับรู้ได้ถึงพลังที่แข็งแกร่ง แต่เจ้าหาใช่ผู้ย้อนกลับงั้นรึ ถ้าอย่างงั้นข้าจะสอนเจ้าเองนี้เพราะข้าเห็นว่าเจ้ามีแววหรอกนะ\n"%god)
            typing("%s : เอาล่ะเจ้าได้เข้าสู่ชั้นแรกแล้วลองไปสู้กับมอนนั้นเพื่อทะยานไปชั้นต่อไปเลย!!!\n"%god)
            print()
        if level == 5:
            typing("%s : หึ เจ้ามาถึงชั้นที่ 5 ได้หรือนี้ การที่เจ้ามาถึงจุดนี้ได้แปลว่า ลางสังหรณ์ของข้าถูกต้อง ก่อนข้าจะไป ข้าจะบอกทริคให้หอคอยนี้ทุกๆ 5 ชั้นจะมี \033[1;36;40mMini-Boss\033[0;0;0m และทุกๆ 10 ชั้นจะมี \033[1;31;40mBoss\033[0;0;0m\n"%god)
            typing("%s : เตรียมตัวของเจ้าให้พร้อมก่อนจะสู้\n"%god)
        if level == 10:
            typing("%s : หึ เจ้ามาถึงชั้นที่ 5 ได้หรือนี้ การที่เจ้ามาถึงจุดนี้ได้แปลว่า ลางสังหรณ์ของข้าถูกต้อง ก่อนข้าจะไป ข้าจะบอกทริคให้หอคอยนี้ทุกๆ 5 ชั้นจะมี \033[1;36;40mMini-Boss\033[0;0;0m และทุกๆ 10 ชั้นจะมี \033[1;31;40mBoss\033[0;0;0m\n"%god)
            typing("%s : เตรียมตัวของเจ้าให้พร้อมก่อนจะสู้\n"%god)
        status_player = Player.copy()
        power_player(status_player, weapon_status)
        mon, mon_type = power_mon(mon, status_mon, stack_mon, mon_type)

        typing("\033[0;49;90m**คุณสามารถที่จะใช้ไอเทม เพื่อเพิ่ม HP, MP หรือคุณสามารถที่จะอัพพอยต์เพื่อเพิ่มความแข็งแกร่งให้ตัวละครคุณ ก่อนจะสู้กับมอนเตอร์**\033[0;0;0m\n\n")
        print("-"*24+"\n")
        point_player, status_player = choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon, 1)

        fighting(mon, status_player, status_mon, weapon_status, player_item, unlock_skill, mon_type, 1)
        if status_player['hp'] <= 0:
            return level, 1, stack_mon, stack_weapon, player_item, point_player

        Player["max_hp"] += 5
        Player["hp"] += 5
        point_player += 3

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
        print("1 : สู้เลย"+" (เลือกที่จะสู้ต่อเมื่อคุณเตรียมพร้อมเสร็จแล้ว)"*guide)
        print("2 : ใช้ไอเทม"+" (เลือกที่จะใช้งานไอเทม)"*guide)
        print("3 : อัพสเตตัส"+" (เลือกที่จะใช้ พอยต์ ของคุณเพื่อเพิ่มความสามารถของตัวละคร \033[0;33;40m**พอยต์จะเพิ่มทุกๆ 3 หน่วยต่อ 1 ชั้น พอยต์จะเพิ่ม 10 หน่วยต่อการชนะบอส 1 ตัว**\033[0;0;0m)"*guide)
        print()
        typing("-"*24+"\n")
        select = input("กรุณาเลือกตัวเลือก : ").strip()

        if select == "1":
            return point_player, status_player

        elif select == "2":
            typing("-"*24+"\n")
            use_item(status_player, player_item, guide)
            print("\n")

        elif select == "3":
            point_player, status_player = upgrade_pointplayer(point_player, status_player, weapon_status, weapon_rate, stack_weapon, guide)

        else:
            print("\033[0;49;90m\n**ไม่มีตัวเลือกนี้**\033[0;0;0m")
            typing("-"*24+"\n\n")

def upgrade_pointplayer(point_player, status_player, weapon_status, weapon_rate, stack_weapon, guide=0):
    while True:
        control = 1
        spent_point = "-999"
        typing("-"*24+"\n")
        print("\n\033[0;49;31mHP\033[0;0;0m :\t%02d/%02d\n\033[0;49;34mMP\033[0;0;0m :\t%02d/%02d\nSTR :\t%02d\nAGI :\t%02d\nINT :\t%02d"\
            %(status_player['hp'], status_player['max_hp'], status_player['mp'], status_player['max_mp'], status_player['str'], status_player['agi'], status_player['int']))#ถ้าอัพค่าใดค่าหนึ่งแล้วค่านั้นจะมีผลเลย
        print("\n\033[0;33;40mPoint\033[0;0;0m : %d"%point_player)
        print("\033[0;49;90m**กรุณาเลือกค่าที่จะอัพ**\033[0;0;0m")
        print("1 : STR"+"\t(ค่า STR จะเป็นการเพิ่มดาเมจกายภาพ และเพิ่ม \033[4;49;31mMAX\033[0;0;0m \033[0;49;31mHP\033[0;0;0m)"*guide)
        print("2 : AGI"+"\t(ค่า AGI จะเป็นการเพิ่มเร็วของตัวเอง ช่วยเพิ่มจำนวนรอบของการเลือกโจมตี)"*guide)
        print("3 : INT"+"\t(ค่า INT จะเป็นการเพิ่มดาเมจเวท และเพิ่ม \033[4;49;34mMAX\033[0;0;0m \033[0;49;34mMP\033[0;0;0m)"*guide)
        print("4 : กลับไปหน้าหลัก")
        typing("\n"+"-"*24+"\n")
        want_upgrade = input("กรุณาเลือกตัวเลือก : ").strip()
    #*****แก้ให้เวลาอัพ แล้วแสดงทันที*****
        if want_upgrade == "1" and point_player != 0:
            print("พิมพ์ \033[0;49;31mB\033[0;0;0m เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input("จำนวนพอยต์ที่จะใช้ : ").lower().strip()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                Player['str'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "2" and point_player != 0:
            print("พิมพ์ \033[0;49;31mB\033[0;0;0m เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input("จำนวนพอยต์ที่จะใช้ : ").lower().strip()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                Player['agi'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "3" and point_player != 0:
            print("พิมพ์ \033[0;49;31mB\033[0;0;0m เพื่อกลับไปหน้าอัพสกิล")
            spent_point = input("จำนวนพอยต์ที่จะใช้ : ").lower().strip()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                Player['int'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "4":
            typing("-"*24+"\n\n")
            return point_player, status_player
        elif (point_player != 0 and want_upgrade not in ("1", "2", "3", "4")) or (point_player == 0 and want_upgrade not in ("1", "2", "3", "4")):
            print("\033[0;49;90m**ไม่มีตัวเลือกนี้**\033[0;0;0m")
            continue

        if spent_point.isdecimal():
            spent_point = int(spent_point)

        if point_player == 0:
            typing("\nพอยต์ไม่พอ"*control)
        
        elif isinstance(spent_point, str):
            if spent_point.lower() == "b":
                typing("\nย้อนกลับ"*control)
            else:
                typing("\nคุณใส่ผิด"*control)

        elif point_player < int(spent_point):
            typing("\nพอยต์ไม่พอ\n"*control)
        
        else:
            print("\033[0;49;90m\n**ไม่มีตัวเลือกนี้**\033[0;0;0m"*control)

        status_player = Player.copy()

        power_player_items(weapon_status, weapon_rate, stack_weapon, 0)
        power_player(status_player, weapon_status)
        time.sleep(0.5)
        os.system('cls')

def power_player_items(weapon_status, weapon_rate, stack_weapon, control=1):
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

    if weapon_rate == "ตำนานจนละเอียด" and control == 1:
        weapon_status["str"] *= 2
        weapon_status["int"] *= 2
        weapon_status["agi"] *= 2

def power_player(status_player, weapon_status):
    status_player['str'] += weapon_status['str']
    status_player['int'] += weapon_status['int']
    status_player['agi'] += weapon_status['agi']

    status_player['max_hp'] += status_player['str']*5
    status_player['max_mp'] += status_player['int']*5
    status_player['hp'] += status_player['str']*5
    status_player['mp'] += status_player['int']*5

    if status_player["hp"] > status_player["max_hp"]:
        status_player["hp"] = status_player["max_hp"]
    if status_player["mp"] > status_player["max_mp"]:
        status_player["mp"] = status_player["max_mp"]
    
    if status_player["mp"] < 0:
        status_player["mp"] = 0

def power_mon(mon, status_mon, stack, mon_type):
    status_mon['str'] += stack
    status_mon['int'] += stack
    status_mon['agi'] += stack
    status_mon['hp'] += status_mon['str']*5
    status_mon['mp'] += status_mon['int']*5

    if mon_type == "Boss":
        status_mon['hp'] += status_mon['hp']*100//100
        status_mon['mp'] += status_mon['mp']*100//100
        status_mon['str'] += status_mon['str']*100//100
        status_mon['agi'] += status_mon['agi']*100//100
        status_mon['int'] += status_mon['int']*100//100
        mon_type = "\033[1;31;40m"+mon_type+"\033[0;0;0m"

    elif mon_type == "Mini-Boss":
        status_mon['hp'] += status_mon['hp']*50//100
        status_mon['mp'] += status_mon['mp']*50//100
        status_mon['str'] += status_mon['str']*50//100
        status_mon['agi'] += status_mon['agi']*50//100
        status_mon['int'] += status_mon['int']*50//100
        mon_type = "\033[1;36;40m"+mon_type+"\033[0;0;0m"

    if mon_type != "":
        mon = mon_type+" "+mon
    else:
        mon_type = "       "
    return mon.strip(), mon_type

def inside_tower(level, weapon_status, choice, weapon_name, unlock_skill):
    """tower"""
    if weapon_name == "9 มม.ฝังเวทย์":
        weapon_rate = "Inwza007"
    else:
        weapon_rate = "งั้นๆ"

    stack_mon, stack_weapon = 0, 0
    player_item = {"HP potion" : 1, "MP potion" : 1}
    point_player = 0
    
    power_player_items(weapon_status, weapon_rate, stack_weapon)

    while level != 51:
        if choice == "2":
            level, choice, stack_mon, stack_weapon, player_item, point_player = \
            tutorial(level, weapon_status, stack_mon, stack_weapon, player_item, point_player, weapon_rate, unlock_skill)

        tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name, tmp_legend, tmp_legend_status = "", "", "", "", ""
        mon_type = ""
        mon = re_mon() #สุ่มมอนที่จะสู้
        stack_mon += 1 + level//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        if level%10 == 0:
            mon_type = "Boss"
        elif level%5 == 0:
            mon_type = "Mini-Boss"
        if level%10 == 1 and level != 1:
            for i in Monster:
                Monster[i]["agi"] += 10
            point_player += 10
            unlock_skill += 1

        status_mon = Monster[mon].copy()
        status_player = Player.copy()

        power_player(status_player, weapon_status)

        if status_player["hp"] <= 0:
            os.system("cls")
            print("-"*24+"\n")
            print("\033[0;49;31m", end="")
            typing("Game Over\n")
            print("\033[0;0;0m", end="")
            typing("คุณตายที่ชั้น %d แล้ว\n\n"%level)
            typing('\033[0;35;40mเสียงปริศนา\033[0;0;0m : ลูกแกะหลงทางที่น่าสงสารเจ้าช่างปวกเปียกและเหยาะแหยะเสียจริง\n')
            typing('\033[0;35;40mเสียงปริศนา\033[0;0;0m : เห็นแก่ที่ข้าสงสารเจ้า ข้าจะบอกอะไรดีๆให้ฟังก็แล้วกัน\n')
            typing('\033[0;35;40mเสียงปริศนา\033[0;0;0m : ในช่วงที่เจ้าเลือกอาวุธคู่กายเจ้าลองท่องคาถา [uuddlrlrab] ดูสิแล้วมันจะบังเกิดอภินิหารขึ้น\n')
            typing('\033[0;35;40mเสียงปริศนา\033[0;0;0m : ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า ฮ่า\n')
            print("\n"+"-"*24)
            break

        mon, mon_type = power_mon(mon, status_mon, stack_mon, mon_type)
        os.system('cls')
        typing("-"*24+"\n\n")
        typing("\033[0;49;93mขณะนี้คุณได้เข้าสู่ชั้น\033[0;0;0m %d\n"%level)
        typing("\n"+"-"*24+"\n\n")

        stack_weapon += 1

        point_player, status_player = choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon)

        fighting(mon, status_player, status_mon, weapon_status, player_item, unlock_skill, mon_type)

        #สุ่ม Potion ด้วย
        tmp_legend, tmp_legend_status = rate_legend()

        if tmp_legend != "" and level >= 30:
            print("*"*24)
            print("\033[2;49;34mคุณได้รับ\033[0;0;0m%s ระดับ Inwza007"%(tmp_legend))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(tmp_legend_status['str'], tmp_legend_status['agi'], tmp_legend_status["int"]))
            print("*"*24)
            print("\033[2;49;93mอาวุธเดิม\033[0;0;0m%s ระดับ %s"%(weapon_name, weapon_rate))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(weapon_status['str'], weapon_status['agi'], weapon_status["int"]))
            print("*"*24)
            print("1 : เปลี่ยน\n2 : ยกเลิก")
            while True:
                num = input("ต้องการจะเปลี่ยนไหม : ").strip()
                if num == "1":
                    weapon_name = tmp_legend
                    weapon_rate = "Inwza007"
                    weapon_status = tmp_legend_status
                    print("เปลี่ยนเสร็จสิ้น")
                    break
                elif num == "2":
                    break
                else:
                    print("คุณป้อนผิด")
            print("\n"+"-"*24+"\n")

        elif level != 1 and random.randrange(10) in [0, 1, 2, 3]:
            tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name = re_item()#สุ่มไอเทม

        if tmp_weapon_name != "":
            print("*"*24)
            print("\033[2;49;34mคุณได้รับ\033[0;0;0m%s ระดับ %s"%(tmp_weapon_name, tmp_weapon_rate))
            power_player_items(tmp_weapon_status, tmp_weapon_rate, stack_weapon)
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(tmp_weapon_status['str'], tmp_weapon_status['agi'], tmp_weapon_status["int"]))
            print("*"*24)
            print("\033[2;49;93mอาวุธเดิม\033[0;0;0m%s ระดับ %s"%(weapon_name, weapon_rate))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(weapon_status['str'], weapon_status['agi'], weapon_status["int"]))
            print("*"*24)
            print("1 : เปลี่ยน\n2 : ยกเลิก")
            while True:
                num = input("ต้องการจะเปลี่ยนไหม : ").strip()
                if num == "1":
                    weapon_name = tmp_weapon_name
                    weapon_rate = tmp_weapon_rate
                    weapon_status = tmp_weapon_status
                    print("เปลี่ยนเสร็จสิ้น")
                    break
                elif num == "2":
                    break
                else:
                    print("คุณป้อนผิด")
            print("\n"+"-"*24+"\n")

        level += 1
        Player["max_hp"] += 5
        Player["hp"] += 5
        point_player += 3
    
    if level == 51 and weapon_name == "9 มม.ฝังเวทย์":
        print("คุณทำลายหอคอยได้แล้ว")
        print("[%s]รู้สึกว่าคุณช่างน่าอดสูและรู้สึกสงสารคุณจนสุดห้วงลึกในหัวใจ"%god)
        print('คุณกำลังกลับเมืองเพื่อไปรับพร 3 ข้อจากพระราชา\nแต่ทว่าเมื่อคุณกำลังเข้าเมืองก็โดนพวกทหารล้อมจับ\
            \nชาวบ้านต่างพากันซุบซิบ\n[ชาวบ้าน]:"นั้นนะเหรอ ผู้กล้าที่ใชศาสตร์จอมมารนะ ช่างน่ารังเกียจเสียจริง" \
            \n[พระราชา]:"ข้าขอสั่งประหารผู้กล้าผู้ริอาจใช้ศาสตร์แห่งจอมมาร บัดเดี๋ยวนี้!"\
            \nสิ้นเสียงพระราชาคอคุณได้ขาดสะบั่นด้วยฝีมืออัศวินผู้มากฝีมือแห่งอณาจักร')
        print("Bad ending")
    elif level == 51:
        print("คุณทำลายหอคอยได้แล้ว")
        print("คุณกำลังกลับเมืองเพื่อไปรับพร 3 ข้อจากพระราชา\
        \nแต่ทว่าไม่มีใครอยู่อีกแล้ว\nเพราะเวลาในหอคอยกับชีวิตจริงนั้นไม่เท่ากัน\
        \nกว่าคุณจะพิชิตหอคอยได้มันก็ผ่านไปราว 1000 ปีได้แล้ว\nเรื่องราวจะเป็นอย่างไรต่อไป\nTo be continue")
    else:
        return

def tower(object, choice):
    """เล่น"""
    level = 1
    weapon_name = ""
    if object == "ดาบเก่าๆ":
        weapon_name = "ดาบ"
        object = weapon["ดาบ"].copy()
    if object == "สมุดเวทย์ผุๆ":
        weapon_name = "สมุดเวทย์"
        object = weapon["สมุดเวทย์"].copy()
    if object == "9 มม.ฝังเวทย์":
        weapon_name = "9 มม.ฝังเวทย์"
        object = weapon_secret["9 มม.ฝังเวทย์"].copy()

    inside_tower(level, object, choice, weapon_name, 2)

def main_story():
    """main story"""
    os.system("cls")
    os.system("chcp 874")
    choice = ""
    print("\n\033[0;34;40m***กดปุ่ม Esc เพื่อ Skip***\n\033[0;0;0m")
    typing("ณ โลกที่แสนสงบสุข ได้มีวิญญาณร้ายกลายร่างเสกหอคอยแห่งความชั่วร้ายขึ้นมาหวังที่จะทำลายร้างโลกทิ้งไป")
    typing("\nพระราชาจึงได้ประกาศว่า ใครที่สามารถทำลายหอคอย \033[1;35;40m50 ชั้น\033[0;0;0m นี้ทิ้งได้จะบันดาลคำขอให้ 3 อย่าง นับแต่นั้นเป็นต้นมา")
    typing("\nโลกก็ได้เข้าสู่ยุคสมัยของผู้กล้า ทุกคนต่างรวมตัวกันเพื่อที่จะทำลายหอคอย")
    #เลือกอาวุธ
    typing("\n\nท่านอยากใช้สิ่งใดเป็นอาวุธ")
    print("\n1 : ดาบเก่าๆ\n2 : สมุดเวทย์ผุๆ")
    while True:
        choice = input("กรุณาเลือกอาวุธ : ").strip()
        if choice == "1":
            weapon = "ดาบเก่าๆ"
            break
        elif choice == "2":
            weapon = "สมุดเวทย์ผุๆ"
            break
        elif choice.lower() == "uuddlrlrab":
            weapon = "9 มม.ฝังเวทย์"
            print("""คุณได้ใช้แพ็คเกจของผู้ย้อนกลับ
[พระเจ้า]รูัสึกสมเพชในตัวคุณ""")
            break
        elif choice != "":
            print("เฮ้ นั้นมันไม่ใช่อาวุธที่มีอยู่นะ!!!\n")
    typing("-"*24+"\n")
    #บอกชื่อและถามว่าจะข้ามบทฝึกสอนรึเปล่า
    typing("\nท่านก็เป็นคนคนหนึ่งที่กำลังจะเข้าสู่หอคอยทันใดนั้นก็มีเสียงเข้ามาในหัว")
    typing('\n\033[1;30;40mเสียงลึกลับ\033[0;0;0m: "ท่านมีนามว่าอะไร?"\n')
    name = input("ชื่อของคุณ : ")
    typing("\n"+"-"*24+"\n")
    Player['name'] = "\033[1;32;40m"+name+"\033[0;0;0m"
    if weapon == "9 มม.ฝังเวทย์":
        typing("\n\033[1;30;40mเสียงลึกลับ\033[0;0;0m: \"ว้าวววว!!! ท่าน %s ท่านช่างดูเหยาะแหยะ ปวกเปียกและน่าสมเพชเหลือเกิน ข้าคือ %s ไม่ทราบว่าท่านเป็นไก่อ่อนผู้กลับชาติมาเกิดรึเปล่า?\""%(Player["name"], god))
        typing("\n\nอธิบาย : ผู้กลับชาติมาเกิดหรือก็คือท่านเคยเล่นเกมนี้หรือไม่ตัวเกมจะได้สอนระบบบื้องต้น\n")
        print("1 : ใช่แล้วฉันนี้้แหละผู้กลับชาติมาเกิด!!! (เคยเล่น)\n2 : อ่อไม่ใช่อะ (ไม่เคยเล่น)\n3 : ออกจากหอคอย")
    else:
        typing("\n\033[1;30;40mเสียงลึกลับ\033[0;0;0m: \"ว้าวววว!!! ท่าน %s ท่านช่างดูสง่าราศี ข้าคือ %s ไม่ทราบว่าท่านเป็นผู้กลับชาติมาเกิดใช่รึไม่?\""%(Player["name"], god))
        typing("\n\nอธิบาย : ผู้กลับชาติมาเกิดหรือก็คือท่านเคยเล่นเกมนี้หรือไม่ตัวเกมจะได้สอนระบบบื้องต้น\n")
        print("1 : ใช่แล้วฉันนี้้แหละผู้กลับชาติมาเกิด!!! (เคยเล่น)\n2 : อ่อไม่ใช่อะ (ไม่เคยเล่น)\n3 : ออกจากหอคอย")

    while True:
        choice = input("กรุณาเลือกตัวเลือก : ").strip()
        if choice == "1":
            break
        elif choice == "2":
            break
        elif choice == "3":
            break
        else:
            print("เฮ้ ที่นี้เราไม่ทำกันแบบนั้น!!!\n")
    if choice == "3":
        print("ออกไวจริงเชียว")
        return
    typing("\n"+"-"*24+"\n\n")
    tower(weapon, choice)
main_story()