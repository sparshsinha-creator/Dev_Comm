from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/myfirstendpoint')
def my_first_endpoint():
    return "Hello, Sparsh!"

@app.route('/userlogin')
def user_login():
    return render_template('user_login.html')

if __name__ == '__main__':
    app.run(debug=True)