import random

def play(start_amount):

    win_amount = 1
    loss_amount = 1.5

    cur_amount = start_amount
    tosses = 0

    while cur_amount > 0:
        tosses += 1
        toss = random.randint(0, 1)
        if toss == 0:
            cur_amount += win_amount
            print('Heads! Current amount: {0}'.format(cur_amount))
        else:
            cur_amount -= loss_amount
            print('Tails! Current amount: {0}'.format(cur_amount))
    print('Game over :( Current amount: {0}. Coin tosses: {1}'.format(cur_amount, tosses))

if __name__ == '__main__':
    start_amount = float(input('Enter your starting amount: '))
    play(start_amount)
