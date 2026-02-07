from sqlalchemy import insert, select, update, delete
from models import Blog
from database import engine
def get_all_articles():
    stmt = select(Blog)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchall()

def create_article(article_title):
    stmt = insert(Blog).values(
        article_title = article_title
    )
    with engine.begin() as conn:
        conn.execute(stmt)

def delete_article(article_id):
    stmt = delete(Blog).where(Blog.c.article_id == article_id)
    with engine.begin() as conn:
        conn.execute(stmt)

