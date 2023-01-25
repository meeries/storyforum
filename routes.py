from app import app
from flask import abort, render_template, redirect, request, session
import users
import stories

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", error="Passwords do not match")
        if len(password1) < 5:
            return render_template("error.html", error="Password must be at least 5 characters")
        if len(username) < 1:
            render_template("error.html", error="Username can't be empty")
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    return redirect("/")

