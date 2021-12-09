# This is a script to generate random string, number, sysmbol password of any length
from string import ascii_letters, digits, punctuation
from secrets import choice
from re import search

def getRandPwd():
    alphanumerics = ascii_letters + digits + punctuation
    length = int(input("Enter Length of Password\n:> "))
    if length < 8:
        print("Too Short. Lenght Must be Greater than 8 Characters. Try Again...\n")
        getRandPwd()
    else:
        password = "".join(choice(alphanumerics) for _ in range(length))
        status = ""
        if search(r'(.)\1\1', password):
            status = "Weak Password: Same Character Repeats"
        elif search(r'(..)(.*?)\1', password):
            status = "Weak Password: Same String Pattern Repetition"
        else:
            status = "Strong Password"
        print(f"Your Random Generated Password is\n:> {password}\nStatus: {status.upper()}")

getRandPwd()