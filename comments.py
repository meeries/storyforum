from db import db
from flask import session
from datetime import datetime

def add_comment(content, user_id, story_id):
    sql = """INSERT INTO comments (content, user_id, story_id)
            VALUES (:content, :user_id, :story_id)"""
    db.session.execute(sql, {"content":content, "user_id":user_id, "story_id":story_id})
    db.session.commit()
