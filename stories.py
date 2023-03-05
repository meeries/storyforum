from db import db
from flask import session
from datetime import datetime

def add_story(title, content, user_id, category_id):
    sql = """INSERT INTO stories (title, content, visible, category_id, user_id)
            VALUES (:title, :content, TRUE, :category_id, user_id) RETURNING id"""
    result = db.session.execute(sql, {"title":title, "content":content, "category_id":category_id, "user_id":user_id}).fetchone()[0]
    db.session.commit()
    return result

def get_story(story_id):
    sql = "SELECT S.title, S.content, S.user_id, U.username FROM stories S INNER JOIN users U ON S.user_id=U.id WHERE S.id=:story_id"
    result = db.session.execute(sql, {"story_id":story_id})
    return result.fetchall()

def get_story_comments(story_id):
   sql = "SELECT C.id, C.content, C.user_id, U.username FROM comments C INNER JOIN users U ON C.user_id=U.id WHERE C.story_id=:story_id ORDER BY C.id"
   result = db.session.execute(sql, {"story_id":story_id})
   return result.fetchall()

def get_story_likes(story_id):
    sql = "SELECT COUNT(*) FROM likes WHERE story_id=:story_id"
    result = db.session.execute(sql, {"story_id":story_id})
    return result.fetchone()[0]

def search(keyword):
    sql = "SELECT title, id FROM STORIES WHERE LOWER(title) LIKE LOWER(:keyword)"
    result = db.session.execute(sql, {"keyword":"%"+keyword+"%"})
    return result.fetchall()

def like_story(story_id, liker_id):
    sql = "INSERT INTO likes (story_id, liker_id) VALUES (:story_id, :liker_id)"
    db.session.execute(sql, {"story_id":story_id, "liker_id":liker_id})
    db.session.commit()

def has_user_liked(story_id, liker_id):
    sql = "SELECT * FROM likes WHERE story_id=:story_id AND liker_id=:liker_id"
    result = db.session.execute(sql, {"story_id":story_id, "liker_id":liker_id}).fetchall()
    if len(result) == 0:
        return False
    else:
        return True
