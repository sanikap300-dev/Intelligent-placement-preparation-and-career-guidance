from flask import Flask
from flask import  render_template

app = Flask(__name__,template_folder="templates") #"__main__" #print(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 