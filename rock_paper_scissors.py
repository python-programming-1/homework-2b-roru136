
def rps():
    human_score = 0
    computer_score = 0
    return human_score, computer_score

human = 0
computer =0

while True:
        h,c=rps()
        human += h
        computer += c
        print ('Your score:', str(human)+ ', Computer score:', computer)
        print('make a move!(r/s/p)')
        from random import choice
        h = input()
        c = choice(['r','s','p'])
        h = choice(['r','s','p'])
        if h == c:
            print('Draw')
        elif h == 's' and c == 'r':
            computer += 1
            print('you lose')
        elif h == 'r' and c == 's':
            human += 1
            print('you win!')
        elif h == 'p' and c == 's':
            computer += 1
            print('you lose')
        elif h == 'p' and c == 'r':
            human += 1
            print('you win!')
        elif h == 'r' and c == 'p':
            computer += 1
            print('you lose')
        elif h == 's' and c == 'p':
            human += 1
            print('you win!')
        else:
            print ('Try again')

        print('Do you want to play again? (y/n)')
        if input() == 'y':
            continue
            if input()== 'n':
                continue
        print('come back soon!')
         
        if input() == 'sc':
            print('Your score:', str(human)+ ', Computer score:', computer)
            
        if input() == 'bye':
            break
    


