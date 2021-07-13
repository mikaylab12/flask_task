from flask import Flask

app3 = Flask(__name__)

@app3.route('/')
def home():
    return"<body style=background-color:pink;> Welcome to the Admin page</body>"

@app3.route('/guest/')
def guest():
    return "<body style=background-color:blue;> Welcome to the Guest page</body>"

@app3.route('/username/')
def user():
    return"<body style=background-color:purple;> Welcome to the User page</body>"

if __name__ == '__main__':
    app3.debug = True
    app3.run()
