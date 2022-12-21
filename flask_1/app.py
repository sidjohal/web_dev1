from flask import Flask
from flask import render_template
from flask import request
import time
app = Flask(__name__)

@app.route("/")
def home():
    return (
        render_template("index.html", user='Sid')
    )

@app.route("/new", methods=['GET', 'POST'])
def new_user():
    if request.method=='GET':
        return (
            render_template("create.html")
        )
    elif request.method=='POST':
        new_name = request.form['user_name']
        return (
                render_template("display.html", name=new_name)
            ) 

@app.route("/user")
def show_user():
    return (
        render_template("display.html")
    )

@app.route("/redirect", methods=['POST'])
def redirect():
    time.sleep(1)
    name = request.form['user_name']
    return(
        render_template("index.html", user='name')
    )

if __name__=='__main__':
    app.run(debug=True)