### We will create a simple login page using flask
## User credentials will be stored in a dictionary/list
## If credentials are a match, redirect to main\dashboard
### NB: This is a demo webpage, hence, DO NOT ENTER ANY SENSITIVE PERSONAL INFORMATION

# importations
from flask import Flask, request, render_template, redirect, flash, sessions

# application initialisation
app = Flask(__name__)

# global dictionary for storing user credentials
usr_credential = {'coolkid': '12345678'}

# register route
@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        user_details = request.form
        username = user_details.get('username')
        password = user_details.get('password')
        confirm = user_details.get('password_confirm')
        # check if password is the same as the confirmed password, hence, information validity
        if username and password in usr_credential:
            flash("User Already Exists", category='error')
        elif len(username) < 5:
            flash("Username MUST be greater than 5 characters.", category="error")
        elif len(password) < 7:
            flash("Password is too short. Password must be greater that 7 characters long.", category="error")
        else: # add details to usr_credentials
            pass
    return render_template("register.html") # default user view

# login route
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        pass
    return render_template("login.html")

@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")


# prevent this script from being used by other scripts
if __name__ == "__main__":
    app.debug = True # app status set to development
    app.run()