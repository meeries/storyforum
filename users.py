from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password)
                 VALUES (:username, :password)"""
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    session["user_id"] = user[1]
    session["user_name"] = username

    return True

def user_id():
    return session.get("user_id)")

def logout():
    del session["user_id"]
    del session["user_name"]
def username_available(username):
    sql = "SELECT COUNT(*) FROM users WHERE username=:username"
    result= db.session.execute(sql, {"username":username})
    return result.fetchone()[0]
