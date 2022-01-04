import random

def play():
    user = input ("r for rock, p for paper, s for scissor")
    computer = random.choice(['r','p','s'])
    print ('Your choice::::::::{}'.format(user))
    print ('Computer choice::::{}'.format(computer))

    if user == computer:
        return 'Tie'

    if is_win(user,computer):
        return 'You won'

    return 'You lost'
def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

output = play()
print (output)

