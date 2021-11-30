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

    user = []
    user_points = 0
    for steps in range(5, 0, -1):
        turn = str(input("Press A to roll dice, B to quit game: "))
        if turn == 'A' 'a':
            scores = random.randint(1, 6)
            print(f"You have {steps} remaining. Good Luck!")
            print(f'You rolled a {scores}\n')
            user.append(scores)
        else:
            print("Exiting Game...")
            sleep(1)
            break

    for diceFace, diceScore in dice_nums.items():
        for faceRolled in range(len(user)):
            if int(diceFace) == user[faceRolled]:
                user_points += diceScore
    print(f"Total Points: {user_points}")

if __name__ == "__main__":
    play = str(input("Press Y to start game, N to leave game: "))
    if play == 'Y' or 'y':
        try:
            print("Rules: You have only 5 tries to play.\nTo win all your points must be more than 100.")
            sleep(1)
            print("Points Awarded on dice rolled:\n1 - 5 points\n2 - 10 points\n3 - 15 points\n4 - 20 points\n5 - 25 points\n6 - 30 points\n")
            sleep(1)
            dice()
        except Exception as error:
            print(f"Error Detected: {error}\nInvalid. Aborting Game...")
    else:
        print("Leaving game...")
        sleep(.75)
