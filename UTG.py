import sys, time, os
import climage
import keyboard
import random
Player = {'name': "", 'hp': 10, 'mp': 10, 'max_hp': 10, 'max_mp': 10, 'str': 10, 'agi': 10, 'int': 10}
Name_Boss_random = ['Slime', 'Ant', 'Goblin', 'Orc', 'Lizard', 'Ancient Robot']
Monster = {'Slime': {'hp': 2, 'mp': 2, 'str': 1, 'agi': 2, 'int': 3, 'skill': {'Rush Attack': (10, 0, 0.3,"s"), 'Spray Mucus': (7, 14, 0.4, "i"), 'Gluttony': (20, 20, 0.5, "s"), 'Savage Bite': (30, 27, 0.8, "s"), 'Explosion Slime': (40, 80, 1, "i")}  },
            'Ant': {'hp': 3, 'mp': 3, 'str': 2, 'agi': 4, 'int': 2, 'skill': {'Regular Attack': (10, 0, 0.4,"s"), 'Bite': (12, 0, 0.6, "s"), 'Dash Attack': (17, 0, 0.8, "s"), 'Spit Poison': (26, 20, 1, "i"), 'Armor Penetration': (30, 70, 3, "s")}},
            'Goblin': {'hp': 5, 'mp': 5, 'str': 4, 'agi': 5, 'int': 4, 'skill': {'Punch': (11, 0, 0.8, "s"), 'Thrash Sheath': (8, 0, 1, "s"), 'Fire Torch': (19, 50, 1.5, "i"), 'Slash': (24, 0, 2, "s"), 'Great Slash': (30, 0, 2.5, "s")}},
            'Orc': {'hp': 15, 'mp': 3, 'str': 6, 'agi': 3, 'int': 0, 'skill': {'Smash': (7, 0, 1, "s"), 'Roar': (12, 20, 2, "i"), 'Giant Arm': (18, 0, 1, "s"), 'Annihilate': (25, 50, 2, "s"), 'Groundbreaking': (35, 70, 2.8, "s")}},
            'Lizard': {'hp': 4, 'mp': 20, 'str': 2, 'agi': 18, 'int': 5, 'skill': {'Backbite': (13, 0, 2, "s"), 'Envenom': (17, 140, 2, "i") , 'Devil Claw': (20, 170, 1.4, "s"), 'Lightning Strike': (27, 200, 2, "i"), 'God Speed': (30, 250, 3, "i")}},
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

rate_drop = ["Poor", "Normal", "Normal", "Normal", "Normal", "Normal", "Rare", "Rare", "Rare", "Legend"]
#ถ้ามีเวลาค่อยใส่ของกวนๆ
potion_drop = ["Potion HP", "Potion HP", "Potion HP", "Potion MP", "Potion MP", "Potion MP", "The shattered glasses of the creator", "The shattered glasses of the creator", "The shattered glasses of the creator", "The shattered glasses of the creator"] #, "ลุงตูบที่อยู่บ้านข้างๆ", "กระป๋องน้ำซ่าชื่นใจ", "ความรักที่คุณให้เขาไปแต่เขาไม่ให้เคยให้อะไรกลับมา"
legen_drop = ["The Stick of Truth", "The Drill of Rule"]
weapon_drop = ["Sword", "Rapier", "Magic Book", "Spear", "Giant Sword", "Three Sword", "Holy Staff", "Magic Lamp", "Magic Wand", "Holy Bomb"]

weapon_legendary = {"The Stick of Truth":{"str": 1000, "int": 1000, "agi": 1000, "skill":{"Shinjitsuwa itsumo hitotsu!": (1000, 2, 5, "i")}}, 
                    "The Drill of Rule":{"str": 1000, "int": 1000, "agi": 1000, "skill":{"Break The Seal!": (1200, 1, 5, "s")}}, "":""}
weapon_secret = {"9 mm Magic Gun":{"str": 2000, "int": 2000, "agi": 2000, "skill":{"This is the best solution": (2000, 1, 5, "i")}}}
weapon = {"Sword": {"str": 5, "int": 0, "agi": 3, "skill": {"Slash Straight": (4, 5, 1.1, "s"), "Wind Slash": (16, 5, 1.5, "s"), "Berserk Slash": (35, 10, 2, "s"), "Asura Slash": (300, 50, 3, "s")}}, 
              "Spear": {"str": 6, "int": 0, "agi": 4, "skill": {"Pierce Straight": (4, 5, 1.1, "s"), "Pierce!": (16, 10, 1.5, "s"), "Wind Spin": (50, 15, 2, "s"), "Helicopter!": (350, 40, 3, "s")}}, 
              "Rapier": {"str": 3, "int": 0, "agi": 9, "skill": {"Yok": (2, 5, 1.1, "s"), "Shit!": (19, 4, 1.5, "s"), "Juwang": (60, 30, 2, "s"), "Tank!": (350, 50, 3, "s")}}, 
              "Giant Sword": {"str": 10, "int": 0, "agi": -1, "skill": {"Savage Slash Straight!": (6, 5, 1.1, "s"), "Slap Flit": (25, 15, 1.5, "s"), "Stomp Break": (70, 30, 2, "s"), "Break Earth": (500, 150, 3, "s")}}, 
              "Three Sword": {"str": 8, "int": 0, "agi": 5, "skill": {"Three Sword Style : Slash": (5, 5, 1.1, "s"), "Three Sword Style : Wind Slash": (15, 6, 1.5, "s"), "Three Sword Style : Wind Sword 36 form": (100, 40, 2, "s"), "Three Sword Style : Asura": (450, 120, 4, "s")}}, 
              "Magic Book": {"str": 0, "int": 5, "agi": 3, "skill": {"Fire Ball": (3, 5, 1.5, "i"), "Lightning Strike": (35, 25, 2, "i"), "Punishment of Darkness": (60, 60, 3, "i"), "Get Some Books!": (400, 125, 4, "i")}}, 
              "Holy Staff": {"str": 0, "int": 10, "agi": -1, "skill": {"Enhance Staff and Slash!!": (4, 5, 1.5, "i"), "Wind Cut": (29, 11, 2, "i"), "Go to Hell!": (80, 70, 3, "i"), "In the name of Monday, I will punish you": (500, 150, 4, "i")}}, 
              "Magic Lamp": {"str": 0, "int": 7, "agi": 1, "skill": {"Magic of Light": (3, 5, 1.5, "i"), "Kameee hameeee haaaa!": (35, 15, 2, "i"), "Sealing Sword of Light": (75, 65, 3, "i"), "Genki Ball": (450, 125, 4, "i")}}, 
              "Magic Wand": {"str": 0, "int": 6, "agi": 7, "skill": {"Steel Inflammable": (4, 5, 1.5, "i"), "Wicked!": (50, 20, 2, "i"), "Expecto Patronum": (100, 65, 3, "i"), "Avada Kedavra": (499, 149, 4, "i")}}, 
              "Holy Bomb": {"str": 0, "int": 8, "agi": 5, "skill": {"Cracker": (3, 5, 1.5, "i"), "Hand Bomb": (30, 21, 2, "i"), "TNT": (100, 60, 3, "i"), "Space and Time Bomb!": (499, 149, 4, "i")}}}

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

god = "\033[1;33;40m[God]\033[0;0;0m"
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
        print("1 : Potion HP %02d"%player_item['HP potion']+"  (\033[0;36;40mPotion HP can recovery 25% of your \033[4;49;31mMax\033[0;49;31m HP\033[0;0;0m)"*guide)
        print("2 : Potion MP %02d"%player_item['MP potion']+"  (\033[0;36;40mPotion MP can recovery 20% of your \033[4;49;34mMax\033[0;49;34m MP\033[0;0;0m)"*guide)
        print("3 : Back\n")

        typing("-"*24+"\n")
        use = input("Select Potion : ").strip()

        if use == "1" and player_item['HP potion'] != 0:
            status_player['hp'] += status_player['max_hp']*25//100
            Player["hp"] += status_player["max_hp"]*25//100
            player_item['HP potion'] -= 1
            os.system("cls")
            typing("-"*24+"\n")
            print("\n%s use Potion HP recovery \033[0;49;31m%d\033[0;0;0m\n"%(Player['name'], (status_player['max_hp']*25//100)))
            typing("-"*24+"\n")
            fixed(status_player)
            if tmp == 1:
                return 1

        elif use == "2" and player_item['MP potion'] != 0:
            status_player['mp'] += status_player['max_mp']*20//100
            Player["mp"] += status_player["max_mp"]*20//100
            player_item['MP potion'] -= 1
            os.system("cls")
            typing("-"*24+"\n")
            print("\n%s use Potion MP recovery \033[0;49;34m%d\033[0;0;0m\n"%(Player['name'],(status_player['max_mp']*20//100)))
            typing("-"*24+"\n")
            fixed(status_player)
            if tmp == 1:
                return 1

        elif (use == "1" or use == "2") and (player_item['HP potion'] == 0 or  player_item['MP potion'] == 0):
            print("\033[0;49;90m**You have no Potion HP**\033[0;0;0m"*(use == "1")+"\033[0;49;90m**You have no Potion MP**\033[0;0;0m"*(use == "2"))
            typing("-"*24+"\n")

        elif use == "3":
            os.system("cls")
            typing("-"*24)
            break

        else:
            print("\033[0;49;90m**Wrong Option**\033[0;0;0m")
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
        print("%d : Back\n"%stop)
        typing("-"*24+"\n")
        action = input("Select Skill : ").strip()
        if action in tmp_skill:
            #ทำปลดล็อคสกิลไว้ด้วย
            if status_player["mp"] >= tmp_skill[action][2]:
                Player["mp"] -= tmp_skill[action][2]
                status_player["mp"] -= tmp_skill[action][2]
                return action
            else:
                print("\033[0;49;34mMP \033[0;0;0mnot enough")
                typing("-"*24+"\n")
        elif action == str(stop):
            os.system('cls')
            return "Back"
        else:
            print("\033[0;49;90m**Wrong Skill**\033[0;0;0m")
            typing("-"*24+"\n\n")
    

def fighting(mon, status_player, status_mon, weapon_status, player_item, unlock_skill, mon_type, guide=0):
    """ต่อสู้"""

    typing("-"*24+"\n")
    print("""\n%s has Appeared!!"""%mon)
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
                print("1 : Normal Attack" + " (\033[0;36;40mDamage will be converted from STR by Normal Attack\033[0;0;0m)"*guide)
                print("2 : Skill" + " (\033[0;36;40mDamage is calculated by multiplying STR or INT by Skill\033[0;0;0m)"*guide)
                print("3 : Open Inventory"+" (\033[0;36;40mUse Potion to recovery \033[0;49;31mHP\033[0;0;0m \033[0;36;40mor \033[0;49;34mMP\033[0;0;0m)"*guide+"\n\033[0;49;90m**Using each option will cost you a number of your turn.**\033[0;0;m"*guide+"\n")
                typing("-"*24+"\n")
                action = input("Select Option : ").strip()

                if action == "1":
                    os.system('cls')
                    typing("-"*24+"\n")
                    action = "\033[1;49;33mNormal Attack\033[0;0;0m"
                    status_mon['hp'] -= atk_player

                elif action == "2":
                    typing("-"*24+"\n")
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
                        atk_player = random.randrange(int(atk_player), int(atk_player)+10)
                        status_mon['hp'] -= atk_player
                        action = "\033[1;49;36m"+tmp_skill[action][0]+"\033[0;0;0m"
                    os.system('cls')
                    typing("-"*24+"\n")

                elif action == "3":
                    check = use_item(status_player, player_item, guide, 1)
                    if check == 1:
                        break
                    else:
                        continue

                else:
                    print("\033[0;49;90m**Wrong Option**\033[0;0;0m")
                    typing("-"*24)
                    continue

                print("\n%s to %s\nDamage %02d"%(action, mon, atk_player))
                typing("\n"+"-"*24)

                if status_mon['hp'] <= 0:
                    typing("""\n\n%s has been \033[0;49;31mkilled\033[0;0;0m.\n\n"""%mon)
                    #***********สุุ่มพวกอาวุธ สุ่ม potion ที่จะได้**********
                    drop = re_potion()
                    for i in drop:
                        print("%s obtain %s"%(Player['name'], i))
                        if i == "Potion HP":
                            item = climage.convert('item\\blood_potion.png', is_unicode=True, width=15)
                            player_item["HP potion"] += 1
                        elif i == "Potion MP":
                            item = climage.convert('item\\mana_potion.png', is_unicode=True, width=15)
                            player_item["MP potion"] += 1
                        else:
                            item = climage.convert('item\\glasses.png', is_unicode=True, width=15)
                        print(item)
                    input("Press Enter\n")
                    typing("-"*24+"\n\n")
                    return
                break

        for _ in range(turn_monster):
            atk_mon = random.randrange(status_mon["str"]-4, status_mon["str"]+2) # มอนตี
            action = [1, 1, 1 ,1 ,1, 2, 2 ,2 ,1 , 1]
            action = random.choice(action)
            if action == 2:
                tmp_skill = mon_use_skill(status_mon, unlock_skill)
                if tmp_skill != [None]:
                    action = "\033[1;49;36m"+tmp_skill[0]+"\033[0;0;0m"
                    atk_mon = tmp_skill[1][0]
                    status_mon["mp"] -= tmp_skill[1][1]
                    if tmp_skill[1][3] == "s":
                        atk_mon += status_mon["str"]*tmp_skill[1][2]
                    if tmp_skill[1][3] == "i":
                        atk_mon += status_mon["int"]*tmp_skill[1][2]
                else:
                    action = 1

            if action == 1:
                action = "\033[0;49;90mNormal Attack\033[0;0;0m"

            status_player["hp"] -= atk_mon
            Player["hp"] -= atk_mon

            print("\n\n%s has used %s to %s\nDamage %02d"%(mon, action, Player["name"], atk_mon))
            typing("\n"+"-"*24+"\n")

            if status_player["hp"] <= 0 :
                return
            time.sleep(0.2)
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

def tutorial(level, weapon_status, stack_mon, stack_weapon, player_item, point_player, weapon_rate, unlock_skill, weapon_name):
    """hello newbie"""
    mon = "Slime"
    power_player_items(weapon_status, weapon_rate, stack_weapon)

    while level <= 10:
        tmp_level = ""
        tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name = "", "", ""
        mon_type = ""
        stack_mon += 1 + level//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        stack_weapon += 1

        if level > 1:
            mon = re_mon() #สุ่มมอนที่จะสู้
            if level%10 == 0:
                mon_type = "Boss"
            elif level%5 == 0:
                mon_type = "Mini-Boss"

        status_mon = Monster[mon].copy()
        
        if str(level)[-1] == "1":
            tmp_level = str(level)+"st"
        elif str(level)[-1] == "2":
            tmp_level = str(level)+"nd"
        elif str(level)[-1] == "3":
            tmp_level = str(level)+"rd"
        else:
            tmp_level = str(level)+"th"

        os.system('cls')
        typing("-"*24+"\n\n")
        typing("\033[0;49;93mYou are currently on the \033[0;0;0m%s\033[0;49;93m floor.\033[0;0;0m\n"%tmp_level)
        typing("\n"+"-"*24+"\n\n")

        if level == 1:
            typing("%s : \"Hmnh... Strange I thought I feel the power but you're not the returnee? if so, I'll teach you since I see that you have a glimpse.\"\n"%god)
            typing("%s : \"Alright, you've entered the 1st floor, try fighting that monster to advance to the next floor!!!\"\n"%god)
            print()
        if level == 5:
            typing("%s : \"Huh.. you've already reached 5th floor, my hunch was right. You could careful every 5th floor, you will encounter \033[1;36;40mMini-Boss\033[0;0;0m and every 10th floor, you will encounter \033[1;31;40mBoss.\033[0;0;0m\"\n"%god)
            typing("%s : \"And after you kill the \033[1;31;40mBoss\033[0;0;0m, you'll unlock a \033[0;49;36mnew skill\033[0;0;0m for your weapon.\"\n"%god)
            typing("%s : \"Be ready before you go.\"\n"%god)
        if level == 10:
            typing("%s : \"I hope you could detroy tower this time... There's nothing that I can teach you. Careful about \033[1;31;40mBoss\033[0;0;0m. I bless you\"\n"%god)

        status_player = Player.copy()
        power_player(status_player, weapon_status)
        mon, mon_type = power_mon(mon, status_mon, stack_mon, mon_type)

        typing("\033[0;49;90m**You can use \"Open Inventory\" for recovery HP, MP or \"Status\" for UP your status before you fight monster**\033[0;0;0m\n\n")
        print("-"*24+"\n")
        point_player, status_player = choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon, 1)

        fighting(mon, status_player, status_mon, weapon_status, player_item, unlock_skill, mon_type, 1)
        if status_player['hp'] <= 0:
            return level, 1, stack_mon, stack_weapon, player_item, point_player

        if level != 1 and random.randrange(10) in [0, 1, 2, 3]:
            tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name = re_item()#สุ่มไอเทม

        if tmp_weapon_name != "":
            print("*"*24)
            print("\033[2;49;34mReceived\033[0;0;0m a %s \033[4;49;39mrank\033[0;0;0m %s"%(tmp_weapon_name, tmp_weapon_rate))
            power_player_items(tmp_weapon_status, tmp_weapon_rate, stack_weapon)
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(tmp_weapon_status['str'], tmp_weapon_status['agi'], tmp_weapon_status["int"]))
            print("*"*24)
            print("\033[2;49;93mYour weapon \033[0;0;0mis a %s \033[4;49;39mrank\033[0;0;0m %s"%(weapon_name, weapon_rate))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(weapon_status['str'], weapon_status['agi'], weapon_status["int"]))
            print("*"*24)
            print("1 : Change\n2 : Reject")
            while True:
                num = input("You want to Change? : ").strip()
                if num == "1":
                    weapon_name = tmp_weapon_name
                    weapon_rate = tmp_weapon_rate
                    weapon_status = tmp_weapon_status
                    print("Change successful")
                    break
                elif num == "2":
                    break
                else:
                    print("\033[0;49;90m**Wrong Choice**\033[0;0;0m")

            print("\n"+"-"*24+"\n")

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
        print("Continue Fight?")
        print("1 : Fight"+" (\033[0;36;40mChoose to continue fight. when you are ready\033[0;0;0m)"*guide)
        print("2 : Open Inventory"+" (\033[0;36;40mChoose to use Potion\033[0;0;0m)"*guide)
        print("3 : Status"+" (\033[0;36;40mChoose to use Point to UP your status \033[0;33;40m**Point will add every 3 point per floor. Point will add 10 point when you kill the Boss**\033[0;0;0m)"*guide)
        print()
        typing("-"*24+"\n")
        select = input("Select Option : ").strip()

        if select == "1":
            return point_player, status_player

        elif select == "2":
            typing("-"*24+"\n")
            use_item(status_player, player_item, guide)
            print("\n")

        elif select == "3":
            point_player, status_player = upgrade_pointplayer(point_player, status_player, weapon_status, weapon_rate, stack_weapon, guide)

        else:
            print("\033[0;49;90m**Wrong Option**\033[0;0;0m")
            typing("-"*24+"\n\n")

def upgrade_pointplayer(point_player, status_player, weapon_status, weapon_rate, stack_weapon, guide=0):
    while True:
        control = 1
        spent_point = "-999"
        typing("-"*24+"\n")
        print("\n\033[0;49;31mHP\033[0;0;0m :\t%02d/%02d\n\033[0;49;34mMP\033[0;0;0m :\t%02d/%02d\nSTR :\t%02d\nAGI :\t%02d\nINT :\t%02d"\
            %(status_player['hp'], status_player['max_hp'], status_player['mp'], status_player['max_mp'], status_player['str'], status_player['agi'], status_player['int']))#ถ้าอัพค่าใดค่าหนึ่งแล้วค่านั้นจะมีผลเลย
        print("\n\033[0;33;40mPoint\033[0;0;0m : %d"%point_player)
        print("\033[0;49;90m**Select Stat to UP**\033[0;0;0m")
        print("1 : STR"+"\t(\033[0;36;40mSTR will increase Physical Damage and \033[4;49;31mMAX\033[0;0;0m \033[0;49;31mHP\033[0;0;0m)"*guide)
        print("2 : AGI"+"\t(\033[0;36;40mAGI will increase Speed that will add your turn to attack\033[0;0;0m)"*guide)
        print("3 : INT"+"\t(\033[0;36;40mINT will increase Magic Damage and \033[4;49;34mMAX\033[0;0;0m \033[0;49;34mMP\033[0;0;0m)"*guide)
        print("4 : Back")
        typing("\n"+"-"*24+"\n")
        want_upgrade = input("Select Stat : ").strip()
    #*****แก้ให้เวลาอัพ แล้วแสดงทันที*****
        if want_upgrade == "1" and point_player != 0:
            print("Type \033[0;49;31mB\033[0;0;0m To go back to status menu")
            spent_point = input("Amount Point : ").lower().strip()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                Player['str'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "2" and point_player != 0:
            print("Type \033[0;49;31mB\033[0;0;0m To go back to status menu")
            spent_point = input("Amount Point : ").lower().strip()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                Player['agi'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "3" and point_player != 0:
            print("Type \033[0;49;31mB\033[0;0;0m To go back to status menu")
            spent_point = input("Amount Point : ").lower().strip()
            if spent_point.isdecimal() and point_player >= int(spent_point):
                Player['int'] += int(spent_point)
                point_player -= int(spent_point)
                control = 0
        elif want_upgrade == "4":
            os.system('cls')
            typing("-"*24+"\n\n")
            return point_player, status_player
        elif (point_player != 0 and want_upgrade not in ("1", "2", "3", "4")) or (point_player == 0 and want_upgrade not in ("1", "2", "3", "4")):
            print("\033[0;49;90m**Wrong Option**\033[0;0;0m")
            continue

        if spent_point.isdecimal():
            spent_point = int(spent_point)

        if point_player == 0:
            typing("\nNot enough points"*control)
        
        elif isinstance(spent_point, str):
            if spent_point.lower() == "b":
                typing("\nBack"*control)
            else:
                typing("\nWrong Word"*control)

        elif point_player < int(spent_point):
            typing("\nNot enough points\n"*control)
        
        else:
            print("\033[0;49;90m\n**Wrong Option**\033[0;0;0m"*control)

        status_player = Player.copy()

        power_player_items(weapon_status, weapon_rate, stack_weapon, 0)
        power_player(status_player, weapon_status)
        time.sleep(0.5)
        os.system('cls')

def power_player_items(weapon_status, weapon_rate, stack_weapon, control=1):
    weapon_status['str'] += stack_weapon*control
    weapon_status['int'] += stack_weapon*control
    weapon_status['agi'] += stack_weapon*control

    if weapon_rate == "Poor" and control == 1:
        weapon_status["str"] += -1
        weapon_status["int"] += -1
        weapon_status["agi"] += -1

    if weapon_rate == "Rare" and control == 1:
        weapon_status["str"] += 5
        weapon_status["int"] += 5
        weapon_status["agi"] += 5

    if weapon_rate == "Legend" and control == 1:
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
        mon_type = "\033[1;49;34m"+mon_type+"\033[0;0;0m"

    if mon_type != "":
        mon = mon_type+" "+mon
    else:
        mon_type = "       "
    return mon.strip(), mon_type

def inside_tower(level, weapon_status, choice, weapon_name, unlock_skill, stack_mon, stack_weapon, player_item, point_player, stack_newgame_mon, stack_newgame_player, weapon_rate):
    """tower"""
    if weapon_name == "9 mm Magic Gun":
        weapon_rate = "Inwza007"
    elif weapon_rate == "":
        weapon_rate = "Normal"
        
    if stack_newgame_mon == 0:
        power_player_items(weapon_status, weapon_rate, stack_weapon)

    while level != 51:
        tmp_level = ""
        if choice == "2":
            level, choice, stack_mon, stack_weapon, player_item, point_player = \
            tutorial(level, weapon_status, stack_mon, stack_weapon, player_item, point_player, weapon_rate, unlock_skill, weapon_name)

        tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name, tmp_legend, tmp_legend_status = "", "", "", "", ""
        mon_type = ""
        mon = re_mon() #สุ่มมอนที่จะสู้

        status_mon = Monster[mon].copy()
        status_player = Player.copy()

        stack_mon += 1 + level//10 + stack_newgame_mon #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
        if level%10 == 0:
            mon_type = "Boss"
        elif level%5 == 0:
            mon_type = "Mini-Boss"
        if level%10 == 1 and level != 1:
            for i in Monster:
                Monster[i]["agi"] += 10
            point_player += 10
            unlock_skill += 1

        power_player(status_player, weapon_status)
        
        if str(level)[-1] == "1":
            tmp_level = str(level+50*stack_newgame_mon)+"st"
        elif str(level)[-1] == "2":
            tmp_level = str(level+50*stack_newgame_mon)+"nd"
        elif str(level)[-1] == "3":
            tmp_level = str(level+50*stack_newgame_mon)+"rd"
        else:
            tmp_level = str(level+50*stack_newgame_mon)+"th"

        if status_player["hp"] <= 0:
            break

        mon, mon_type = power_mon(mon, status_mon, stack_mon, mon_type)
        os.system('cls')
        typing("-"*24+"\n\n")
        typing("\033[0;49;93mYou are currently on the \033[0;0;0m%s\033[0;49;93m floor.\033[0;0;0m\n"%tmp_level)
        typing("\n"+"-"*24+"\n\n")

        stack_weapon += 1

        point_player, status_player = choices_player(status_player, point_player, player_item, weapon_status, weapon_rate, stack_weapon)

        fighting(mon, status_player, status_mon, weapon_status, player_item, unlock_skill, mon_type)
        
        if status_player["hp"] <= 0:
            break

        #สุ่ม Potion ด้วย
        tmp_legend, tmp_legend_status = rate_legend()

        if tmp_legend != "" and level >= 30:
            print("*"*24)
            print("\033[2;49;34mReceived\033[0;0;0m a %s \033[4;49;39mrank\033[0;0;0m Inwza007"%(tmp_legend))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(tmp_legend_status['str'], tmp_legend_status['agi'], tmp_legend_status["int"]))
            print("*"*24)
            print("\033[2;49;93mYour weapon \033[0;0;0mis a %s \033[4;49;39mrank\033[0;0;0m %s"%(weapon_name, weapon_rate))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(weapon_status['str'], weapon_status['agi'], weapon_status["int"]))
            print("*"*24)
            print("1 : Change\n2 : Reject")
            while True:
                num = input("You want to Change? : ").strip()
                if num == "1":
                    weapon_name = tmp_legend
                    weapon_rate = "Inwza007"
                    weapon_status = tmp_legend_status
                    print("Change successful")
                    break
                elif num == "2":
                    break
                else:
                    print("\033[0;49;90m**Wrong Choice**\033[0;0;0m")
            print("\n"+"-"*24+"\n")

        elif level != 1 and random.randrange(10) in [0, 1, 2, 3]:
            tmp_weapon_status, tmp_weapon_rate, tmp_weapon_name = re_item()#สุ่มไอเทม

        if tmp_weapon_name != "":
            print("*"*24)
            print("\033[2;49;34mReceived\033[0;0;0m a %s \033[4;49;39mrank\033[0;0;0m %s"%(tmp_weapon_name, tmp_weapon_rate))
            power_player_items(tmp_weapon_status, tmp_weapon_rate, stack_weapon)
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(tmp_weapon_status['str'], tmp_weapon_status['agi'], tmp_weapon_status["int"]))
            print("*"*24)
            print("\033[2;49;93mYour weapon \033[0;0;0mis a %s \033[4;49;39mrank\033[0;0;0m %s"%(weapon_name, weapon_rate))
            print("STR : %02d\nAGI : %02d\nINT : %02d"%(weapon_status['str'], weapon_status['agi'], weapon_status["int"]))
            print("*"*24)
            print("1 : Change\n2 : Reject")
            while True:
                num = input("You want to Change? : ").strip()
                if num == "1":
                    weapon_name = tmp_weapon_name
                    weapon_rate = tmp_weapon_rate
                    weapon_status = tmp_weapon_status
                    print("Change successful")
                    break
                elif num == "2":
                    break
                else:
                    print("\033[0;49;90m**Wrong Choice**\033[0;0;0m")
            print("\n"+"-"*24+"\n")

        level += 1
        Player["max_hp"] += 5
        Player["hp"] += 5
        point_player += 3+stack_newgame_player

    if stack_newgame_mon != 0 and status_player['hp'] > 0:
        os.system("cls")
        print("-"*24+"\n")
        typing('''%s : "Even if you keep destroying tower. There's no reward for you, you know?\n"'''%god)
        while True:
            print("-"*24+"\n")
            print("1 : New Game+\n2 : Quit")
            choice = input("Select Option : ")
            if choice == "1":
                stack_newgame_mon += 1
                stack_newgame_player += 2
                break
            elif choice == "2":
                break
            else:
                typing("\n\033[0;49;90m**Wrong Option**\033[0;0;0m")
        if choice == "1":
            inside_tower(1, weapon_status, 1, weapon_name, unlock_skill, stack_mon, stack_weapon, player_item, point_player, stack_newgame_mon, stack_newgame_player, weapon_rate)

    elif level == 51 and weapon_name == "9 mm Magic Gun":
        os.system("cls")
        print("-"*24+"\n")
        typing("You have destroyed the tower.\n")
        typing("%s feel that you are so humiliating, and feel pity for you deep down in the heart.\n\n"%god)
        typing('You returned to town for the 3 wishes from The King.\nBut as you entered the town, you was surrounded by soldiers.\n\
            \n[Villager A] : "That\'s him? a Hero who use the Demon Lord\'s art How disgusting."\
            \n[King] : "I order the execution of the Hero use the art of the Demon King Now!"\n\
            \nwhen the king\'s voice has finished. Your neck have rip from your head\nDead...again?\n')
        typing("Bad ending\n\n")
        print("-"*24)
        input("\033[0;49;90m**Press Enter for quit game**\033[0;0;0m")

    elif level == 51:
        os.system("cls")
        print("-"*24+"\n")
        typing("You have destroyed the tower.\n")
        typing("You returned to town for the 3 wishes from The King.\
        \nBut as you going to the town, there is no more that town.\nBecause the time between tower and outside not equal.\
        \nWhen you conquer the tower, 1000 years have already passed.\nHow does the story conclude?\n")
        typing("\nTo be continue\n")
        while True:
            print("\n"+"-"*24+"\n")
            print("1 : New Game+\n2 : Quit")
            choice = input("Select Option : ")
            if choice == "1":
                stack_newgame_mon += 1
                stack_newgame_player += 2
                break
            elif choice == "2":
                break
            else:
                typing("\n\033[0;49;90m**Wrong Option**\033[0;0;0m")
        if choice == "1":
            inside_tower(1, weapon_status, 1, weapon_name, unlock_skill, stack_mon, stack_weapon, player_item, point_player, stack_newgame_mon, stack_newgame_player, weapon_rate)
    else:
        os.system("cls")
        print("-"*24+"\n")
        print("\033[0;49;31m", end="")
        typing("Game Over\n")
        print("\033[0;0;0m", end="")
        typing("%s died on the %s floor\n\n"%(Player['name'], tmp_level))
        typing('\033[0;35;40mMysterious Voice\033[0;0;0m : "Poor lost lamb, what a limp and wistful you are."\n')
        typing('\033[0;35;40mMysterious Voice\033[0;0;0m : "For the sake that I pity you I\'ll tell something good."\n')
        typing('\033[0;35;40mMysterious Voice\033[0;0;0m : "During the moment you choose a weapon cast a \033[0;49;33m\'uuddlrlrab\'\033[0;0;0m and see it will bring a fortune."\n')
        typing('\033[0;35;40mMysterious Voice\033[0;0;0m : "Hah Ha Ha Ha Hah Ha Ha Ha Ha."\n')
        while True:
            print("\n"+"-"*24+"\n")
            print("1 : New Game\n2 : Quit")
            choice = input("Select Option : ")
            if choice == "1":
                print("\n"+"-"*24)
                print("\n1 : Sword\n2 : Magic Book")
                choice2 = input("Select Weapon : ")
                weapon_name = "Old Sword"*(choice2 == "1")+"Dirty Magic Book"*(choice2 == "2")+"9 mm Magic Gun"*(choice2 == "uuddlrlrab")
                if choice2 not in ("1", "2", "uuddlrlrab"):
                    continue
                Player['hp'], Player['max_hp'], Player['max_mp'], Player['mp'], Player['str'], Player['agi'], Player['int'] = 10, 10, 10, 10, 10, 10, 10
                break
            elif choice == "2":
                break
            else:
                typing("\n\033[0;49;90m**Wrong Option**\033[0;0;0m")
        if choice == "1":
            tower(weapon_name, choice)
    return

def tower(object, choice):
    """เล่น"""
    level = 1
    weapon_name = ""
    if object == "Old Sword":
        weapon_name = "Sword"
        object = weapon[weapon_name].copy()
    if object == "Dirty Magic Book":
        weapon_name = "Magic Book"
        object = weapon[weapon_name].copy()
    if object == "9 mm Magic Gun":
        weapon_name = "9 mm Magic Gun"
        object = weapon_secret[weapon_name].copy()

    stack_newgame_mon, stack_newgame_player = 0, 0
    stack_mon, stack_weapon = 0, 0
    player_item = {"HP potion" : 1, "MP potion" : 1}
    point_player = 0

    inside_tower(level, object, choice, weapon_name, 2, stack_mon, stack_weapon, player_item, point_player, stack_newgame_mon, stack_newgame_player, "")

def main_story():
    """main story"""
    os.system("cls")
    choice = ""
    print("\n\033[0;34;40m**Press Esc for Skip**\n\033[0;0;0m")
    typing("In a peaceful world, have evil spirits cast up a tower of evil in hopes of destroy the world.")
    typing("\nSince then, the King has announced that anyone who can destroy tower on all \033[1;35;40m50 floors\033[0;0;0m will be granted 3 wishes.")
    typing("\nThe World has entered the age of brave hero. Everyone gathered to destroy the tower.")
    #เลือกอาวุธ
    typing("\n\nWhat is your weapon?")
    print("\n1 : Old Sword\n2 : Dirty Magic Book")
    while True:
        print("-"*24)
        choice = input("Select Weapon : ").strip()
        if choice == "1":
            weapon = "Old Sword"
            break
        elif choice == "2":
            weapon = "Dirty Magic Book"
            break
        elif choice.lower() == "uuddlrlrab":
            weapon = "9 mm Magic Gun"
            print("""You use a packet of one who returned
%s feel pathetic in you."""%god)
            break
        else:
            print("\033[0;49;90mHey that not in option!!!\033[0;0;0m")
    typing("-"*24+"\n")
    #บอกชื่อและถามว่าจะข้ามบทฝึกสอนรึเปล่า
    typing("\nYou were the one who was about to enter the tower when suddenly a voice came in your head.")
    typing('\n\033[1;30;40mUnknown\033[0;0;0m: "What is your name?"\n')
    name = input("Name : ")
    typing("\n"+"-"*24+"\n")
    Player['name'] = "\033[1;32;40m"+name+"\033[0;0;0m"
    if weapon == "9 mm Magic Gun":
        typing("\n\033[1;30;40mUnknown\033[0;0;0m: \"Wow!!! %s You..look weakly, lame and so pathetic. I am %s. Is this your reincarnation?\""%(Player["name"], god))
        typing("\n\nExplain : Reincarnation, or is it that you've played this game before? If not, the game will teach you the basics of the system.\n")
        print("1 : Yes, I am!!! (\033[0;36;40mHave played\033[0;0;0m)\n2 : No (\033[0;36;40mNever played\033[0;0;0m)\n3 : Leave the tower")
    else:
        typing("\n\033[1;30;40mUnknown\033[0;0;0m: \"Wow!!! %s You look gorgeous. I am %s. Is this your reincarnation?\""%(Player["name"], god))
        typing("\n\nExplain : Reincarnation, or is it that you've played this game before? If not, the game will teach you the basics of the system.\n")
        print("1 : Yes, I am!!! (\033[0;36;40mHave played\033[0;0;0m)\n2 : No (\033[0;36;40mNever played\033[0;0;0m)\n3 : Leave the tower")

    while True:
        print("-"*24)
        choice = input("Select Choice : ").strip()
        if choice == "1":
            break
        elif choice == "2":
            break
        elif choice == "3":
            break
        else:
            print("\033[0;49;90mHey We don't do that here!!!\033[0;0;0m")
    if choice == "3":
        print("So long.")
        return
    typing("-"*24+"\n\n")
    tower(weapon, choice)
main_story()
