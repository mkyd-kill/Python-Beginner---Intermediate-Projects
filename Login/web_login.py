### We will create a simple login page using flask
## User credentials will be stored in a dictionary/list
## If credentials are a match, redirect to main\dashboard
### NB: This is a demo webpage, hence, DO NOT ENTER ANY SENSITIVE PERSONAL INFORMATION

# importations
from flask import Flask, request, render_template, redirect, flash, url_for

# application initialisation
app = Flask(__name__)
app.config['SECRET_KEY'] = "ThisIsAn_Amazing_flask_App"
app.config['SESSION_TYPE'] = 'filesystem'

# global dictionary for storing user credentials
usr_credential = {}

# register route
@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        user_details = request.form
        username = user_details.get('username')
        password = user_details.get('password')
        confirm = user_details.get('password_confirm')
        # check if password is the same as the confirmed password, hence, information validity
        for usrname, passwrd in usr_credential.items():
            if usrname == username and passwrd == password:
                flash("User Already Exists. Please Log in", category='error')
                return redirect(url_for('login'))
        if len(username) < 5:
            flash("Username MUST be greater than 5 characters.", category="error")
        elif len(password) < 7:
            flash("Password is too short. Password must be greater that 7 characters long.", category="error")
        else: # add details to usr_credentials
            usr_credential[username] = password
            flash("User Registration Successfull.")
            return redirect(url_for('login'))
    return render_template("register.html") # default user view

# login route
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user_details = request.form
        username = user_details.get('username')
        password = user_details.get('password')
        # check if input user credentials match the ones in the database
        for usr, pwd in usr_credential.items():
            if username == usr and password == pwd:
                flash("User Logged In Successfully.", category="success")
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid User Credentials. Please Register First!", category="error")
    return render_template("login.html")

@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")


# prevent this script from being used by other scripts
if __name__ == "__main__":
    app.debug = True # app status set to development
    app.run()