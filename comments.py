from db import db
from flask import session
from datetime import datetime

def add_comment(comment, user_id, story_id):
    sql = """INSERT INTO messages (comment, user_id, story_id)
            VALUES (:comment, :user_id, :story_id"""
    db.session.execute(sql, {"comment":comment, "user_id":user_id, "story_id:":story_id})
    db.session.commit()
