from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///site.db"

engine = create_engine(DATABASE_URL, echo=True)
metadata_obj = MetaData()