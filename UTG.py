import status as st
def power_player(status_player, stack_player):
    status_player['hp'] += stack_player
    status_player['hp'] += status_player['str']*5
    status_player['mp'] += status_player['int']*5
    
def power_mon(mon, stack):
    mon['str'] += stack
    mon['int'] += stack
    mon['hp'] += mon['str']*5
    mon['mp'] += mon['int']*5
def main():
    """main story"""
    
    print(st.random_mon,st.Monster[st.random_mon])
    stack_mon, stack_player = 0, 0
    Tower = 1
    stack_mon += 1 + Tower//10 #ถ้าจะฟาร์มต่อจะไม่บวกเพิ่ม
    stack_player += 5
    status_mon = st.Monster[st.random_mon].copy()
    status_player = st.Player.copy()
    power_mon(status_mon, stack_mon)
    power_player(status_player, stack_player)
main()
"""Ultimate tower super ultra Character Galaxy of god (UTG)"""
def main_story():
    """main story"""
    print("ณ โลกที่แสนสงบสุข ได้มีวิญญาณร้ายกลายร่างเสกหอคอยแห่งความชั่วร้ายขึ้นมาหวังที่จะทำลายร้างโลกทิ้งไป\n\
        พระราชาจึงได้ประกาศใครที่สามารถทำลายหอคอยนี้ทิ้งไปได้จะบันดาลคำขอให้ 3 อย่าง\n\
            นับแต่นั้นเป็นต้นมา โลกก็ได้เข้าสู่ยุคสมัยของผู้กล้า ทุกคนต่างรวมตัวกันเพื่อที่จะเคลียร์หอคอย")
    #เลือกอาวุธ
    print("ท่านอยากใช้สิ่งใดเป็นอาวุธ")
    print("1 ดาบเก่าๆ, 2 สมุดเวทผุๆ")
    while True:
        choice = input()
        if choice == "1":
            weapon = "ดาบเก่าๆ"
            break
        elif choice == "2":
            weapon = "สมุดเวทผุๆ"
            break
        else:
            print("เฮ้ นั้นมันไม่ใช่อาวุธที่นายมีอยู่นะ!!!")
    #บอกชื่อและถามว่าจะข้ามบทฝึกสอนรึเปล่า
    print("ท่านก็เป็นคนคนนึงที่กำลังจะเข้าสู่หอคอทันใดนั้นก็มีเสียงเข้ามาในหัวท่าน")
    print('เสียงลึกลับ: "ท่านมีนามว่าอะไร?"')
    name = input()
    print("เสียงลึกลับ: \"ว้าวววว!!! ท่าน %s ท่านช่างดูสง่าราศี ข้าคือ [พระเจ้า] ไม่ทราบว่าท่านเป็นผู้กลับชาติมาเกิดใช่รึไม่?\""%name)
    print("อธืบาย:ผู้กลับชาติมาเกิดหรือก็คือท่านเคยเล่นเกมนี้หรือไม่ตัวเกมจะได้สอนระบบบื้องต้น")
    print("1 ใช่แล้วฉันนี้้แหละผู้กลับชาติมาเกิด!!!, 2 อ่อไม่ใช่อะ")
    while True:
        choice = input()
        if choice == "1":
            print()
            break
        elif choice == "2":
            print()
            break
        else:
            "เฮ้ ที่นี้เราไม่ทำกันแบบนั้น!!!"
main_story()
