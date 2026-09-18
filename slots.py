import random
import time
import colorama as c
from art import tprint
print('\033[1m')
print('\033[2J')
print(f'{c.Fore.LIGHTRED_EX}')
tprint('casino')
print(f'{c.Fore.WHITE}')
slots = ["🍋","🍎","🍇","🍊",'🍓','🍍','🍒','☠️']
# variables
lc,ac,gc,oc,sc,pc,cc,dc=1,1,1,1,1,1,1,0.1
money = 100
bet = 5
speed = 1.5
reward=2
big_reward=20
bet_size_cost = 25
reward_cost=100
big_reward_cost=300
fruit_chance_cost=50

while True:
    slots_weights=[lc,ac,gc,oc,sc,pc,cc,dc]
    slot1 = "".join(random.choices(slots,weights=slots_weights))
    slot2 = "".join(random.choices(slots,weights=slots_weights))
    slot3 = "".join(random.choices(slots,weights=slots_weights))
    if money < bet: # checks weather you have lost
            print('u suck at gambling')
            break

    user=input('type a command: ').lower()
    if user == 'help':  # prints out all the commands
        print('\nhelp: list of commands\ngamble: plays slots\nmoney: displays money\nshop: goes to the shop\n'
              'clear: clears the terminal\nchances: displays chances of fruit\n')

    elif user=='gamble' or user == 'g': # runs the slots code
        print('\n')
        money -= bet
        print("⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n|  |  |  |\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜") # prints the slot machine

        print("\033[3A", end='', flush=True)    # moves the cursor up 3
        print("\033[2G", end='', flush=True)    # moves clomn to the right into the first slot
        print(slot1, end='', flush=True)    # prints the first slot
        time.sleep(speed)

        print("\033[5G", end='', flush=True)  # moves comn to the right js after the second #
        print(slot2, end='', flush=True)    # prints the second slot
        time.sleep(speed)

        print("\033[8G", end='', flush=True)  # moves colmn to the third #
        print(slot3, end='', flush=True)    # prints the thrid slot
        time.sleep(speed)

        if slot1=='☠️'and slot2=='☠️'and slot3=='☠️':
            print('\033[12G', end='',flush=False)
            print(f'{c.Fore.RED}-{money - bet}{c.Fore.WHITE}')
            money = (money*0)+bet

        elif slot1=='☠️'and slot2=='☠️' or slot1=='☠️' and slot3=='☠️' or slot2=='☠️' and slot3=='☠️':
            money=money / 2
            print('\033[12G',end='',flush=False)    # moves cursor to the 12th colmn then prints the money made in a green color
            print(f'{c.Fore.RED}-{money}{c.Fore.WHITE}')

        elif slot1 == slot2 == slot3: # if all the slots are the same gives you the money for it
            money += (bet*big_reward)
            print('\033[12G',end='',flush=False)    # moves cursor to the 12th colmn then prints the money made in a green color
            print(f'{c.Fore.LIGHTGREEN_EX}+{bet*big_reward}{c.Fore.WHITE}')

        elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:    # if slots 1 & 2 are the same gives you the corrasponding money
            money += (bet*reward)
            print('\033[12G',end='',flush=False)
            print(f'{c.Fore.LIGHTGREEN_EX}+{bet*reward}{c.Fore.WHITE}')

        else:   # if none are the same doesn't give you a reward
            print('\033[12G',end='',flush=False)    # moves it to the 12th colmn and prints money lost in a red color
            print(f'{c.Fore.RED}-{bet}{c.Fore.WHITE}')            
            
        print("\033[3B",end='',flush=False) # brings back to the bottom line
        print('\n')

    elif user =='money'or user=='m':    # print the money you have
        print(f'you have ${money}')

    elif user=='shop'or user=='s':  # prints the shop
        print(f"\nbet size: ${bet_size_cost}\nslots speed: $10\nreward: increases the gain per win ${reward_cost}\n"
              f"big reward: increase the reward of the big win ${big_reward_cost}\n" \
              f"fruit chance: increases the odds of getting a single fruit ${fruit_chance_cost} each\n" \
              f"hit 'ENTER' if you don't want to buy anything")
        shop=input('\nwhat would you like to buy?: ')
        if shop=='bet size'or shop=='bs':
            if money - bet_size_cost < bet:
                print('not enough money come back later')
            else:
                bet += 5
                money -= 25
                bet_size_cost=bet_size_cost*1.1
                bet_size_cost=round(bet_size_cost,1)
                print(f'\nbet size is now: {bet} cost is now: ${bet_size_cost}\n')
        elif shop=='slots speed'or shop=='ss':
            if money - 10 < bet:
                print('not enough money come back later')
            else:
                round(speed)
                if speed <= 0.1:
                    print("\nmax speed reached\n")
                    speed += 0.1
                    money += 10
                speed -= 0.1
                money -= 10
                print(f'\nspeed is now: {speed}s cost is $10\n')
        elif shop=='reward'or shop=='r':
            if money - reward_cost < bet:
                print('not enough money come back later')
            else:
                money -=100
                reward+=0.1
                reward_cost=reward_cost*1.1
                reward_cost=round(reward_cost,1)
                reward=round(reward,1)
                print(f'\nreward is now: {reward} cost is now: ${reward_cost}\n')
        elif shop=='big reward'or shop=='br':
            if money - big_reward_cost < bet:
                print('not enough money come back later')
            else:
                money -=300
                big_reward+=0.5
                big_reward_cost=big_reward_cost*1.1
                big_reward=round(big_reward,1)
                big_reward_cost=round(big_reward_cost,1)
                print(f'\nbig reward is now: {big_reward} cost is now: ${big_reward_cost}\n')
        elif shop=='fc'or shop=='fruit chance':
            if money - fruit_chance_cost < bet:
                print('i need more buulets')
            else:
                print(f'\nlemon chances: {lc}\napple chances: {ac}\ngrape chances: {gc}\norange chances: {oc}\nstrawberry chances: {sc}\npineapple chances: {pc}\ncherry chances: {cc}')
                fruit=input('\nwhat chances do you want increased?: ')    # prints the chances of the fruit also allows you to buy a better chance
                if fruit=='lemon'or fruit=='l':
                    lc += 0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    lc=round(lc,1)
                    print(f'\nchance is now: {lc} cost is now ${fruit_chance_cost}\n')
                elif fruit=='apple'or fruit=='a':
                    ac += 0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    fruit_chance_cost=round(fruit_chance_cost)
                    ac=round(ac,1)
                    print(f'\nchance is now: {ac} cost is now ${fruit_chance_cost}\n')
                elif fruit=='grape'or fruit=='g':
                    gc += 0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    fruit_chance_cost=round(fruit_chance_cost)
                    gc=round(gc,1)
                    print(f'\nchance is now: {gc} cost is now ${fruit_chance_cost}\n')
                elif fruit=='orange'or fruit=='o':
                    oc+= 0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    fruit_chance_cost=round(fruit_chance_cost)
                    oc=round(oc,1)
                    print(f'\nchance is now: {oc} cost is now ${fruit_chance_cost}\n')
                elif fruit=='strawberry'or fruit=='s':
                    sc+=0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    fruit_chance_cost=round(fruit_chance_cost)
                    sc=round(sc,1)
                    print(f'\nchance is now: {sc} cost is now ${fruit_chance_cost}\n')
                elif fruit=='pineapple'or fruit=='p':
                    pc+=0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    fruit_chance_cost=round(fruit_chance_cost)
                    pc=round(pc,1)
                    print(f'\nchance is now: {pc} cost is now ${fruit_chance_cost}\n')
                elif fruit=='cherry'or fruit=='c':
                    cc+=0.2
                    money-=50
                    fruit_chance_cost=fruit_chance_cost*1.1
                    fruit_chance_cost=round(fruit_chance_cost)
                    cc=round(cc,1)
                    print(f'\nchance is now: {cc} cost is now ${fruit_chance_cost}\n')
                else:
                    print('\nthat is not a fruit\n')
        elif shop=='':
            print('\nha, fucking broki\n')
        else:
            print("\nthat is not an item in the shop\n")    # if the user does not input a correct shop item prints this then returns to the type a command

    elif user=="bet size":  # prints the bet size
        print(f'bet size is ${bet} per')

    elif user=='clear'or user=='c': # clears the terminal
        print("\033[2J")
        print(f'{c.Fore.LIGHTRED_EX}')
        tprint('casino')
        print(f'{c.Fore.WHITE}') 
   
    elif user=='chances':
        print(f'\nlemon: {lc}\napple: {ac}\ngrape: {gc}\norange: {oc}\nstrawberry: {sc}\npineapple: {pc}\ncherry: {cc}\ndeath: {dc}\n')

    else:
        print("you either don't know commands or misspelled a command type 'help'")  # if a person mistypes a command this will print

    time.sleep(0.5) # a little buffer so people dont spam
