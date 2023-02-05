from db import db
from flask import session
from datetime import datetime

def add_story(title, content, user_id, category_id):
    sql = """INSERT INTO stories (title, content, visible, user_id, category_id, created_at)
            VALUES (:title, :content, TRUE, :user_id, :category_id, NOW()) RETURNING id"""
    result = db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "category_id":category_id}).fetchone()[0]
    db.session.commit()
    return result

def get_story(story_id):
    sql = "SELECT S.title, S.content, S.user_id, U.username, S.created_at, S.visible FROM stories S INNER JOIN users U ON S.user_id=U.id WHERE S.id=:id"
    result = db.session.execute(sql, {"id":story_id})
    return result.fetchall()

def get_story_comments(story_id):
   sql = "SELECT C.id, C.content, C.user_id, U.username, C.sent_at FROM comments C INNER JOIN users U ON C.user_id=U.id WHERE C.story_id=:story_id ORDER BY C.id"
   result = db.session.execute(sql, {"story_id":story_id})
   return result.fetchall()

def get_all_story_titles(story_id):
    sql = "SELECT title, created_at FROM stories ORDER BY created_at DESC"
    result = db.session.execute(sql, {"story_id":story_id})
    return result.fetchall()
