from random import choice

word_list = ['python', 'java', 'php', 'geeks', 'computer', 'rainbow', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'choice', 'keypad', 'movie', 'javascript', 'development', 'quite', 'queen', 'zigzag', 'abort', 'brilliant']

choosen_word = choice(word_list)

print("Welcome to Guess the Word Game")
print("Instructions: Your role is to guess a word. If it is correct you win, else you loss")

guesses = ''

count = int(input("Enter Number of turns you wish to play: "))

while count > 0:
    fails = 0
    for char in choosen_word:
        if char in guesses:
            print(char)
        else:
            print("__")
            fails += 1
    if fails == 0:
        print("****-YOU WIN-****")
        print(f"The word is: {choosen_word}")
        break

    guess = input("Guess a character: ")
    guesses += guess
    
    if guess not in choosen_word:
        count -= 1
        print("Wrong")
        print(f"You have {count} more guesses")

        if count == 0:
            print("****-YOU LOOSE-****")