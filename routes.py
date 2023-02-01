from app import app
from flask import abort, render_template, redirect, request, session
import users, categories, stories, comments

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        available = users.username_available(username)
        if available > 0:
            return render_template("error.html", message="Username is taken")
        if len(username) > 0:
            render_template("error.html", message="Username can't be empty")
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if len(password1) < 5:
            return render_template("error.html", message="Password must be at least 5 characters")
        if users.register(username, password1):
            return redirect("/login")
        else:
            return render_template("error.html", message="Registering failed")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="Wrong username or password")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

###
@app.route("/newstory", methods=["GET", "POST"])
def newstory():
    if request.method == "GET":
        return render_template("newstory.html", categories=categories.get_categories())
    if request.method == "POST":
        story_title = request.form["storytitle"]
        if len(story_title) < 1:
            return render_template("error.html", message="Title can't be empty")

        content = request.form["story"]
        if len(content) < 100:
            return render_template("error.html", message="Please write at least 100 characters")
        return redirect("/")

@app.route("/story/<int:story_id>")
def story(id):
    story = stories.get_story(id)
    comments = stories.get_story_comments
    return render_template("story.html", story=story, id=id, comments=comments)

###
@app.route("/category/<int:id>")
def category(id):
    category_name = categories.get_category_name(id)
    stories = categories.get_category_stories(id)
    return render_template("category.html", category_name=category_name, id=id, stories=stories)