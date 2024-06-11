import asyncio
import random
import time
moni = list(range(100,501))
money = (random.choice(moni))

def spinning():
    symbols = ['💩', '💀', '🥶', '🐍', '🗿']
    return [random.choice(symbols) for _ in range(3)]
def results(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def winner(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '💩':
            return bet * 2
        elif row[0] == '💀':
            return bet * 3
        elif row[0] == '🥶':
            return bet * 5
        elif row[0] == '🐍':
            return bet * 10
        elif row[0] == '🗿':
            return bet * 25
    return 0
def main():
    global money
    print("********************************************")
    print("welcome to this clhp'xwlhtlhplhhsktws slots!")
    print("********************************************")

    while money > 0:
        print(f"Current balance: ${money}")
        print('how much are you betting?')
        bet = input("Bet Amount:")
        bet = int(bet)
        if bet > money:
            debt = bet - money
            print(f"You're off by ${debt}! Try winning some games first!")
            continue
        if bet <= 0:
            print('Bet must be greater than $0')
            continue

        money = money - bet
        print(f' new balance ${money}')
        row = spinning()
        print("spinning...")
        time.sleep(0.5)
        results(row)
        profit = winner(row,bet)

        if profit > 0:
            print(f'Winner! You won ${profit}')
            money = money + profit
            print('play again? y/n')
            play_again = input()
            if play_again == 'y':
                continue
            elif play_again == 'n':
                print(f"You ended with ${money}, see you next time!")

        elif money <= 0:
            print('You have no money, please come again!')
            time.sleep(1)
            exit()

        else:
            print('Unlucky... Try Again? y/n')
            leaving = input()
            if leaving == 'n':
                print('bye bye!')
                time.sleep(1)
                exit()

main()



