### Ask user to first create and account
## save credentials in a dictionary/list
## confirm credentials on login
## redirect to 'home_page'
## We will use functions for different works, this is a terminal script
### NB: This is a demo script, hence, DO NOT ENTER ANY SENSITIVE PERSONAL INFORMATION
from time import sleep
credentials = {}

def register():
    """This is the new user registration function"""
    print("----USER REGISTRATION FORM----")
    usr_name = input("Enter username: ").lower()
    password = input("Enter password: ").lower()
    password2 = ""
    try:
        if len(password) < 5:
            print("Password must be greater than 5 characters. Try again...\n")
            sleep(1)
            register()
        else:
            password2 = input("Re-enter password: ").lower()
    except Exception:
        print("Error detected.")
    if password == password2:
        credentials[usr_name] = password
        print("User Registeration Successful.\n")
        sleep(1)
        print("Redirecting to login page...\n")
        sleep(2)
        login()
    else:
        print("Password does not match. Register Again...\n")
        sleep(2)
        register()

def login():
    """User login function"""
    print("----USER LOGIN FORM----")
    user = input("Enter username: ").lower()
    password = input("Enter password: ").lower()
    try:
        if len(password) < 5:
            print("Password must be greater than 5 characters. Try again...\n")
            sleep(1)
            login()
        elif user not in  credentials.keys() and password not in credentials.values():
                print("User Does not Exist. Please Register First.\n")
                sleep(1)
                print("Redirecting to Register page...")
                sleep(2)
                register()
        else:
            for username, passwrd in credentials.items():
                if username == user and passwrd == password:
                    print("User Logged in Successfully.\n")
                    sleep(1)
                    print("Redirecting to dashboard...\n")
                    sleep(2)
                    print(f"Welcome {username.title()},\nYou have Successfully Logged in.")
                elif user != username or passwrd != password:
                    print("Invalid Input Credentials. Try Again...\n")
                    sleep(1)
    except Exception:
        print("Invalid user credentials. Try again...\n")
        login()
login()