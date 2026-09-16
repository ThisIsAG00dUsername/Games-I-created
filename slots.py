import random
import time

slots = ["🍋","🍎","🍇","🍊",'🍓','🍍','7️⃣']
money = 100
bet = 5
speed = 1
while True:
    slot1 = random.choice(slots)
    slot2 = random.choice(slots)
    slot3 = random.choice(slots)
    if money < bet:
            print('u fucking suck at gambling')
            break
    user=input('type a command: ')
    if user == 'help':
        print('help: list of commands\ngamble: plays slots\nmoney: displays money\nspeed: makes the slots faster\nshop: goes to the shop')
    elif user=='gamble' or user == 'g':
        money -= bet
        print(slot1,end='',flush=True)
        time.sleep(speed)
        print(slot2,end='',flush=True)
        time.sleep(speed)
        print(slot3,end='\n',flush=True)
        time.sleep(speed)
        if slot1 == slot2 == slot3:
            money += (bet*20)
        elif slot1 == slot2:
            money += (bet*2)
        elif slot1 == slot3:
            money += (bet*2)
        elif slot2 == slot3:
            money += (bet*2)
        else:
            pass
    elif user =='money'or user=='m':
        print(f'you have ${money}')
    elif user == 'speed'or user=='s':
        if speed <=0.1:
            print('maximum speed reached')
            speed += 0.1
        speed -= 0.1
        round(speed)
        print(f'speed is now {speed}s')
    elif user=='shop':
        print('bet size: $30')
        shop=input('what would you like to buy?: ')
        if shop=='bet size':
            bet += 5
            money -= 30
        else:
            print("that is not an item in the shop")
    else:
        print("you either don't know commands or missplled a command type 'help'")

    time.sleep(0.1)