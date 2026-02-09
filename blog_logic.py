from sqlalchemy import insert, select, update, delete
from models import Blog
from database import engine
def get_all_articles():
    stmt = select(Blog)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchall()
    
def get_article_by_id(article_id):
    stmt = select(Blog).where(Blog.c.article_id == article_id)
    with engine.begin() as conn:
        conn.execute(stmt)

def create_article(article_title, article_body):
    stmt = insert(Blog).values(
        article_title = article_title,
        article_body = article_body
    )
    with engine.begin() as conn:
        conn.execute(stmt)

def delete_article(article_id):
    stmt = delete(Blog).where(Blog.c.article_id == article_id)
    with engine.begin() as conn:
        conn.execute(stmt)

def update_article(article_id, new_title, article_title, article_body, new_body):
    stmt = (
        update(Blog)
        .where(Blog.c.article_id == article_id)
        .values(article_title = new_title)
        .values(article_body = new_body)
    )
    with engine.begin() as conn:
        conn.execute(stmt)