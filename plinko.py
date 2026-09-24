from enum import auto
import random
import sys
import time
import colorama as c
sys.stdout.write('\033[2J')
money = 10000
bet = 5
gravity = 1
lnr = [0,1]
l,r = 1,1
mag_rwd = 5
red_rwd = 3
yel_rwd = 0.5
grn_rwd = 0
buffer = 0.5
auto_gamble = False
brt_auto_gamble = False
while True:
    weight = [l,r]
    sys.stdout.write('\033[H')
    
    if money < bet:
        print('u lost :(')
        break

    user = input('Enter a command: ').lower()
    if user =='gamble' or user =='g':
        O=1
        gamble_num = 1
        if auto_gamble == True:
            gamble_num=input('number of gambles: ')
        try:
            gamble_num = int(gamble_num)
        except ValueError:
            print('that is not a whole number')
            gamble_num = 1
        while O <= gamble_num:
            colmn = 8
            rows = 6
            height = 4
            position = 0
            sys.stdout.write('\033[2J')
            sys.stdout.write('\033[10;1H')
            if money < bet:
                print('u lost')
                break

            money -= bet
            print(
            '       .\n'
            '      . . \n'
            '     . . . \n' 
            '    . . . . \n' 
            '   . . . . . \n'
            '  . . . . . . \n' 
            f' {c.Fore.MAGENTA}■ {c.Fore.RED}■ {c.Fore.YELLOW}■ {c.Fore.GREEN}■ {c.Fore.YELLOW}■ {c.Fore.RED}■ {c.Fore.MAGENTA}■{c.Fore.RESET}\n')
            for row in range(rows):
                bounce = random.choices(lnr,weights=weight)[0]
                if bounce == 0:
                    position -= 1  # bounce left
                    sys.stdout.write(f'\033[{height-1};{colmn-1}H')
                    print('o')
                    time.sleep(gravity)
                    sys.stdout.write(f'\033[{height-1};{colmn-1}H')
                    print(' ')
                    height +=1
                    colmn -=1
                else:
                    position += 1  # bounce right
                    sys.stdout.write(f'\033[{height-1};{colmn+1}H')
                    print('o')
                    time.sleep(gravity)
                    sys.stdout.write(f'\033[{height-1};{colmn+1}H')
                    print(' ')
                    height+=1
                    colmn += 1
                    # g 8 y 6 10 r 4 12 m 2 14
            if height == 10 and colmn == 8:
                money += (bet * grn_rwd)
                sys.stdout.write('\033[5;16H')
                print(f'{c.Fore.RED}-{bet*grn_rwd}{c.Fore.RESET}')
            elif height == 10 and (colmn == 6 or colmn == 10):
                money += (bet * yel_rwd)
                sys.stdout.write('\033[5;16H')
                print(f'{c.Fore.RED}-{bet*yel_rwd}{c.Fore.RESET}')
            elif height == 10 and (colmn == 4 or colmn == 12):
                money += (bet * red_rwd)
                sys.stdout.write('\033[5;16H')
                print(f'{c.Fore.GREEN}+{(bet*red_rwd) - bet}{c.Fore.RESET}')
            elif height == 10 and (colmn == 2 or colmn == 14):
                money += (bet * mag_rwd)
                sys.stdout.write('\033[5;16H')
                print(f'{c.Fore.GREEN}+{(bet*mag_rwd)-bet}{c.Fore.RESET}')
            sys.stdout.write('\033[10;1H')
            time.sleep(buffer)
            sys.stdout.write('\033[2J')
            O+=1
        
        
    elif user=='rewards' or user=='r':
        sys.stdout.write('\033[2J')
        print(f'{c.Fore.MAGENTA}■: x{mag_rwd}\n{c.Fore.RED}■: x{red_rwd}\n{c.Fore.YELLOW}■: x{yel_rwd}\n{c.Fore.GREEN}■: x{grn_rwd}{c.Fore.RESET}')

    elif user == 'money' or user =='m':
        sys.stdout.write('\033[2J')
        print(f'you have ${money}')
        

    elif user=='shop' or user=='s':
        sys.stdout.write('\033[2J')
        print('\nrewards: increase the reward gain\ngravity: increases the falling speed $10\nchance: increase the chance of it going either left or right $50\nball: increases the amount of money per ball $20\nauto gamble: gambles as many times as you want automatically $30')
        shop=input('what would you like to buy?: ')
        if shop=='gravity' or shop=='g':
            money -= 10
            if gravity <= 0.01:
                gravity == 0.01
                gravity = round(gravity,2)
                print('max speed reached')
            elif gravity <=0.2:
                gravity -= 0.01
                gravity = round(gravity,2)
                print('increased speed by 0.05 almost max speed')
                time.sleep(0.3)
            else:
                gravity -= 0.1
                gravity = round(gravity,2)
                print('increased speed by 0.1')
            time.sleep(0.5)
            sys.stdout.write('\033[2J')
        elif shop=='chances' or shop=='c':
            print('\nleft: chances for going left\nright: chances of going right')
            chances=input('\nleft or right chances?: ')
            if chances == 'left'or chances=='l':
                money -= 50
                l += 0.1
                print('\nincreased the chances of going left by 0.1')
            elif chances=='right'or chances=='r':
                money -= 50
                r += 0.1
                print('\nincreased the chances of going right by 0.1')
            else:
                print('\nthat is not a chances of happening')
            time.sleep(buffer)
            sys.stdout.write('\033[2J')

        elif shop=='rewards'or shop=='r':
            print(f'\n{c.Fore.MAGENTA}Magenta box ■: x{mag_rwd} $100\n{c.Fore.RED}Red box ■: x{red_rwd} $50\n{c.Fore.YELLOW}Yellow box ■: x{yel_rwd} $25\n{c.Fore.GREEN}Green box■: x{grn_rwd} $10{c.Fore.RESET}\n')
            pick_rewards=input('what rewards do you want to increase?: ')
            if pick_rewards=='magenta'or pick_rewards=='m':
                money -= 100
                mag_rwd += 0.5
                mag_rwd = round(mag_rwd,1)
                print('\nincreased the reward for the magenta sqaure by 0.5')
            elif pick_rewards=='red'or pick_rewards=='r':
                money -= 50
                red_rwd += 0.2
                red_rwd=round(red_rwd,1)
                print('\nincreased the reward for the red square by 0.2')
            elif pick_rewards=='yellow'or pick_rewards=='y':
                if yel_rwd >= 0.9:
                    print('max yellow reward reached')
                    yel_rwd == 0.9
                else:
                    money -= 25
                    yel_rwd += 0.1
                    yel_rwd = round(yel_rwd,1)
                    print('\nincreased the reward for the yellow square by 0.1')
            elif pick_rewards=='green'or pick_rewards=='g':
                if grn_rwd >=0.9:
                    print('max green reward reached')
                    grn_rwd == 0.9
                else:
                    money -= 10
                    grn_rwd += 0.1
                    grn_rwd = round(grn_rwd,1)
                    print('\nincreased the reward for the green square by 0.1')
            else:
                print('that is not a color')
            bet += 5
            time.sleep(buffer)
            sys.stdout.write('\033[2J')
        elif shop=='ball'or shop=='b':
            money -= 20
            bet += 5
        elif shop=='auto gamble'or shop=='ag':
            if auto_gamble==False:
                money -= 30
                auto_gamble = True
                brt_auto_gamble = True
            else:
                print('you have already bought this')
    elif user=='buffer'or user=='b':
        buf=input('increase or decrease the buffer: ')
        try:
            buffer = float(buf)
            if buffer <0:
                buffer = -buffer
        except ValueError:
            print('that is not a number')
            buffer = 0.5
    elif brt_auto_gamble == True and (user=='auto gamble' or user=='ag'):
        not auto_gamble