from random import randint

isPlayed = False

def game():
    global isPlayed
    isPlayed = True
    num = randint(1, 10)
    print('I\'ve already guessed one.')

    for i in range(5):
        while(True):
            try:
                x = int(input('Enter your guess: '))
                if x in range(1, 11):
                    break
            except:
                pass
            print('Invalid input')

        d = abs(num - x)
        if d == 0:
            print('Its a match! Congrats')
            return
        elif d in [9, 8]:
            stat = 'very cold'
        elif d in [7, 6]:
            stat = 'cold'
        elif d in [5, 4]:
            stat = 'neutral'
        elif d == 3:
            stat = 'warm'
        elif d < 2:
            stat = 'hot'

        if x < num:
            print(f'Your guess is cold from left and {stat} from right. Try again')
        else:
            print(f'Your guess is {stat} from left and cold from right. Try again')


while(True):
    print('1. Play again' if isPlayed else '1. Start the Game')
    print('2. Exit')
    
    try:
        opt = int(input('> '))
    except:
        print('Invalid input')
        continue

    match opt:
        case 1: game()
        case 2: break
        case _: print('Invalid input')