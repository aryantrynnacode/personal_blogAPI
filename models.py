from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Text
metadata_obj = MetaData()

Blog = Table(
    "blog",
    metadata_obj,
    Column("article_id", Integer, primary_key=True),
    Column("article_title", String(200), nullable=False),
    Column("article_body", Text, nullable=False)
)