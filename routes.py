from app import app
from flask import abort, render_template, redirect, request, session
import users, categories, stories, comments

@app.route("/")
def index():
    return render_template("index.html", categories = categories.get_categories())

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
            return redirect("/")
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
        users.check_csrf()
        story_title = request.form["storytitle"]
        if len(story_title) < 1:
            return render_template("error.html", message="Title can't be empty")
        content = request.form["story"]
        if len(content) < 100:
            return render_template("error.html", message="Please write at least 100 characters")
        category_id = request.form["category_id"]
        stories.add_story(story_title, content, category_id, users.user_id())
        return redirect("/category/" + str(category_id))

@app.route("/story/<int:id>")
def story(id):
    story = stories.get_story(id)
    comments = stories.get_story_comments(id)
    likes = stories.get_story_likes(id)
    return render_template("story.html", story=story, id=id, comments=comments, likes=likes)

###
@app.route("/category/<int:id>")
def category(id):
    category_name = categories.get_category_name(id)
    stories = categories.get_category_stories(id)
    return render_template("category.html", category_name=category_name, id=id, stories=stories)

@app.route("/search", methods=["post"])
def search():
    keyword = request.form["keyword"]
    stories_list = stories.search(keyword)
    return render_template("results.html", stories=stories_list, keyword=keyword)

@app.route("/add_comment", methods=["POST"])
def add_comment():
    if request.method == "POST":
        users.check_csrf()
        story_id = request.form["story_id"]
        content = request.form["content"]
        comments.add_comment(content, users.user_id(), int(story_id))
        return redirect("/story/" + str(story_id))

@app.route("/like_story", methods=["post"])
def like_story():
    if request.method == "POST":
        users.check_csrf()
        story_id = request.form["story_id"]
        if stories.has_user_liked(story_id, users.user_id()) == True:
            return render_template("error.html", message="You have already liked this story")
        else:
            stories.like_story(story_id, users.user_id())
    return redirect("/story/" + str(story_id))
