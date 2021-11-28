import random
from time import sleep

def dice():
    dice_nums = {
        '1': 5,
        '2': 10,
        '3': 15,
        '4': 20,
        '5': 25,
        '6': 30
    }
    user_points = 0
    comp_points = 0
    user = []
    comp = []
    turn = str(input("Press A to roll again, B to quit game: "))
    if turn == 'A' or 'a':
        try:
            for play in range(1, 6):
                user_turn = user.append(random.randint(1, 6))
                comp_turn = comp.append(random.randint(1, 6))

                for dice, points in dice_nums.items():
                    for i in user:
                        if str(i) == dice:
                            user_points =+ points
                    for j in comp:
                        if str(j) == dice:
                            comp_points =+ points

                if user_points >= 100:
                    print("You win")
                elif comp_points >= 100:
                    print("Computer wins")

        except Exception:
            print("Exiting Game...")
    else:
        pass
    return user_points, comp_points


if __name__ == "__main__":
    play = str(input("Press Y to start game, N to leave game: "))
    if play == 'Y' or 'y':
        try:
            print("Rules: You have only 5 tries to play.\nTo win all your points must be more than 100.")
            sleep(1)
            print("Points Awarded on dice rolled:\n1 - 5 points\n2 - 10 points\n3 - 15 points\n4 - 20 points\n5 - 25 points\n6 - 30 points\n")
            sleep(1)
            count = 0
            while True:
                if count <= 5:
                    dice()
                    count += 1
                else:
                    break
                break
        except Exception:
            print("Invalid Input leaving game")
    else:
        print("Leaving game...")
        sleep(.75)
