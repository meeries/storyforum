from app import app
import flask
import users
import stories
import comments

@app.route("/")
def index():
    list = stories.get_list()
    return flask.render_template("index.html", count=len(list), messages=list)

@app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "GET":
        return flask.render_template("register.html")
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password1 = flask.request.form["password1"]
        password2 = flask.request.form["password2"]
#TODO: CHECKING PASSWORD AND USERNAME

@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html")
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]
#TODO: CHECKING PASSWORD AND USERNAME 
