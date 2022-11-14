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