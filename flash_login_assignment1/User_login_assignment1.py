from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Neel1@paripihu",
    database = "Adityabhaiya"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    query = "INSERT INTO users (username,password) VALUES (%s,%s)"
    cursor.execute(query, (username,password))
    db.commit()

    return "User Registered Successfully!"

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query,(username, password))

    result = cursor.fetchone()

    if result:
        return render_template("success.html", user=username)
    else:
        return "Invalid Username or Password"

if __name__ == "__main__":
    app.run(debug=True)
