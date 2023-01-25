from db import db
import flask
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password):
    password_hash = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username, "password":password_hash})
    except:
        return False
    return login(username, password)

def login(username, password):
    sql = "SELECT password, id, FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    flask.session['user_id'] = user[1]
    flask.session['user_name'] = username
    return True

def logout():
    del flask.session["user_id"]
    del flask.session["user_name"]

def user_id():
    return flask.session.get("user_id)", 0)
