import random

def dice_roll():
    roll = random.randint(1,100)

    if roll == 100:
        print(f"{roll} You lose!")
        return False
    elif roll <= 50:
        print(f"{roll} You Lose!")
        return False
    else:
        print("%s You win!" % roll)
        return True

def simple_better(funds, initial_wager, count):
    value = funds
    wager = initial_wager

    current_wager = 0

    while current_wager < count:
        if dice_roll():
            value += wager
        else:
            value -= wager

        current_wager +=1
        print("Funds: %d" % value)

simple_better(10000, 100,100)