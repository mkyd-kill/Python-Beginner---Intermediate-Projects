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
    usr_name = input("Enter username: ")
    password = input("Enter password: ")
    password2 = ""
    try:
        if len(password) < 5:
            print("Password must be greater than 5 characters. Try again...\n")
            sleep(1)
            register()
        else:
            password2 = input("Re-enter password: ")
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
        print("Password does not much. Register Again...\n")
        sleep(2)
        register()

def login():
    """User login function"""
    user = input("Enter username: ")
    password = input("Enter password: ")
    try:
        if len(password) < 5:
            print("Password must be greater than 5 characters. Try again...\n")
            sleep(1)
            login()
        else:
            for username, passwrd in credentials.items():
                if username == user and passwrd == password:
                    print("User Logged in Successfully.\n")
                    sleep(1)
                    print("Redirecting to dashboard...\n")
                    sleep(2)
                    print(f"Welcome {username.title()},\nYou have Successfully Logged in.")
    except Exception:
        print("Invalid user credentials. Try again...\n")
        login()
register()