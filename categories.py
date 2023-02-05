from db import db
from flask import session

def get_categories():
    sql = """SELECT id, category_name FROM categories"""
    return db.session.execute(sql).fetchall()

def get_category_name(category_id):
    sql = "SELECT category_name FROM categories WHERE id=:id"
    result = db.session.execute(sql, {"id":category_id})
    return result.fetchone()[0]

def get_category_stories(category_id):
    sql = "SELECT id, title, content, category_id FROM stories WHERE category_id=:id"
    result = db.session.execute(sql, {"id":category_id})
    return result.fetchall()
