from db import db
from flask import session
from datetime import datetime

def add_story(title, content, user_id, category_id):
    sql = """INSERT INTO stories (title, content, visible, user_id, category_id)
            VALUES (:title, :content, TRUE, :user_id, :category_id) RETURNING id"""
    result = db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "category_id":category_id}).fetchone()[0]
    db.session.commit()
    return result

def get_story(story_id):
    sql = "SELECT title, content FROM stories WHERE id=:id"
    result = db.session.execute(sql, {"id":story_id})
    return result.fetchall()

def get_story_comments(story_id):
   sql = "SELECT C.id, C.content, C.user_id, U.username FROM comments C INNER JOIN users U ON C.user_id=U.id WHERE C.story_id=:story_id ORDER BY C.id"
   result = db.session.execute(sql, {"story_id":story_id})
   return result.fetchall()

def search(keyword):
    sql = "SELECT title, id FROM STORIES WHERE LOWER(title) LIKE LOWER(:keyword)"
    result = db.session.execute(sql, {"keyword":"%"+keyword+"%"})
    return result.fetchall()

def like_story(story_id, user_id):
    sql = "INSERT INTO likes (story_id, user_id) VALUES (:story_id, user_id)"
    db.session.execute(sql, {"story_id":story_id, "user_id":user_id})
    db.session.commit()

def has_user_liked(story_id, user_id):
    sql = "SELECT * FROM likes WHERE story_id=:story_id AND user_id=:user_id"
    result = db.session.execute(sql, {"story_id":story_id, "user_id":user_id}).fetchall()
    if len(result) == 0:
        return False
    else:
        return True
