import random
#import time

# TIC TAC TOE
# by: Cavalex

a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "


def map():
    print("   #   #   ")
    print(" {} # {} # {} ".format(a, b, c))
    print("   #   #   ")
    print("###########")
    print(" {} # {} # {} ".format(d, e, f))
    print("   #   #   ")
    print("###########")
    print(" {} # {} # {} ".format(g, h, i))
    print("   #   #   ")
    print("   #   #   ")


# 0 means its free, 1 means its occupied by the player and 2 means its occupied by the AI.
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0

result = 0


# 0 means the game is running, 1 means the player won, 2 the AI won and 3 its a draw.
def final_result():
    if result == 1:
        print("You won!")

    elif result == 2:
        print("You lost!")

    elif result == 3:
        print("It's a draw!")


def rep():
    print("Block is already occupied!\nYou are going to repeat you turn.")


def blocksFree(block):
    if block == 0:
        return True
    else:
        return False


def reload_blocks():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i

    if b1 == 1:
        a = "X"
    if b1 == 2:
        a = "O"
    if b2 == 1:
        b = "X"
    if b2 == 2:
        b = "O"
    if b3 == 1:
        c = "X"
    if b3 == 2:
        c = "O"
    if b4 == 1:
        d = "X"
    if b4 == 2:
        d = "O"
    if b5 == 1:
        e = "X"
    if b5 == 2:
        e = "O"
    if b6 == 1:
        f = "X"
    if b6 == 2:
        f = "O"
    if b7 == 1:
        g = "X"
    if b7 == 2:
        g = "O"
    if b8 == 1:
        h = "X"
    if b8 == 2:
        h = "O"
    if b9 == 1:
        i = "X"
    if b9 == 2:
        i = "O"

def checkResult():

    global result

    # check if the game is won, if it is then result = 1:
    # horizontal
    if b1 == 1:
        if b3 == 1 and b2 == 1:
            result = 1
    if b4 == 1:
        if b6 == 1 and b5 == 1:
            result = 1
    if b7 == 1:
        if b9 == 1 and b8 == 1:
            result = 1

    # vertical
    if b1 == 1:
        if b7 == 1 and b4 == 1:
            result = 1
    if b2 == 1:
        if b8 == 1 and b5 == 1:
            result = 1
    if b3 == 1:
        if b9 == 1 and b6 == 1:
            result = 1

    # across
    if b1 == 1:
        if b5 == 1 and b9 == 1:
            result = 1
    if b3 == 1:
        if b5 == 1 and b7 == 1:
            result = 1

    # for the ai
    if b1 == 2:
        if b3 == 2 and b2 == 2:
            result = 2
    if b4 == 2:
        if b6 == 2 and b5 == 2:
            result = 2
    if b7 == 2:
        if b9 == 2 and b8 == 2:
            result = 2

    if b1 == 2:
        if b7 == 2 and b4 == 2:
            result = 2
    if b2 == 2:
        if b8 == 2 and b5 == 2:
            result = 2
    if b3 == 2:
        if b9 == 2 and b6 == 2:
            result = 2

    if b1 == 2:
        if b5 == 2 and b9 == 2:
            result = 2
    if b3 == 2:
        if b5 == 2 and b7 == 2:
            result = 2


def ai_move():
    random13 = random.randint(1, 9)
    tick = 0

    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9

    while True:

        # Some help to the ai so it doesn't always do random things:
        # I will need to get a neural network or something lol.
        if blocksFree(b2):
            if b1 == 2 and b3 == 2:
                b2 = 2
                break
            if b5 == 2 and b8 == 2:
                b2 = 2
                break

        if blocksFree(b5):
            if b4 == 2 and b6 == 2:
                b5 = 2
                break

        if blocksFree(b8):
            if b7 == 2 and b9 == 2:
                b8 = 2
                break



        # To repeat the random movement if the tile is occupied:
        # Could have used "continue" at the end but oh well.
        if tick % 2 == 0:
            random13 = random.randint(1, 9)

        # To check if the tile is occupied and play there if it isn't.
        if blocksFree(b1):
            if random13 == 1:
                b1 = 2
                break

        if blocksFree(b2):
            if random13 == 2:
                b2 = 2
                break

        if blocksFree(b3):
            if random13 == 3:
                b3 = 2
                break

        if blocksFree(b4):
            if random13 == 4:
                b4 = 2
                break

        if blocksFree(b5):
            if random13 == 5:
                b5 = 2
                break

        if blocksFree(b6):
            if random13 == 6:
                b6 = 2
                break

        if blocksFree(b7):
            if random13 == 7:
                b7 = 2
                break

        if blocksFree(b8):
            if random13 == 8:
                b8 = 2
                break

        if blocksFree(b9):
            if random13 == 9:
                b9 = 2
                break

        tick += 2


print("\n\n#### TIC TAC TOE ####")
print("#### by Cavalex ####")

print("Choose between the 9 blocks to play.")
print("Write its number to play there.")

# game loop
while result == 0:

    map()

    checkResult()
    final_result()
    if result != 0:
        break

    # player's turn:
    player_move = input("Your turn: ")

    if player_move == "1":
        if blocksFree(b1):
            b1 = 1
        else:
            rep()
            continue

    if player_move == "2":
        if blocksFree(b2):
            b2 = 1
        else:
            rep()
            continue

    if player_move == "3":
        if blocksFree(b3):
            b3 = 1
        else:
            rep()
            continue

    if player_move == "4":
        if blocksFree(b4):
            b4 = 1
        else:
            rep()
            continue

    if player_move == "5":
        if blocksFree(b5):
            b5 = 1
        else:
            rep()
            continue

    if player_move == "6":
        if blocksFree(b6):
            b6 = 1
        else:
            rep()
            continue

    if player_move == "7":
        if blocksFree(b7):
            b7 = 1
        else:
            rep()
            continue

    if player_move == "8":
        if blocksFree(b8):
            b8 = 1
        else:
            rep()
            continue

    if player_move == "9":
        if b9 == 0:
            b9 = 1
        else:
            rep()
            continue

    if player_move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid Block!\nWrite a number between 1 and 9 to\nplay in that respective block.")
        continue

    reload_blocks()

    # so the ai doesn't play after you won.
    checkResult()
    final_result()
    if result != 0:
        map()
        break

    # draw
    if not blocksFree(b1) and not blocksFree(b2):
        if not blocksFree(b3) and not blocksFree(b4):
            if not blocksFree(b5) and not blocksFree(b6):
                if not blocksFree(b7) and not blocksFree(b8):
                    if not blocksFree(b9):
                        if result == 0:
                            result = 3
                            continue

                        continue

    # time.sleep(0.5)

    ai_move()

    reload_blocks()

if not blocksFree(b1) and not blocksFree(b2):
    if not blocksFree(b3) and not blocksFree(b4):
        if not blocksFree(b5) and not blocksFree(b6):
            if not blocksFree(b7) and not blocksFree(b8):
                if not blocksFree(b9):
                    reload_blocks()
                    map()
                    if result == 0:
                        result = 3
                        final_result()
                    else:
                        final_result()
