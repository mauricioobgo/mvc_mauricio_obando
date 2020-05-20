from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime,Text
from app_index import  database

class Book(database.Model):
    id_book = Column(Integer, primary_key=True,nullable=False)
    title = Column(String(400), nullable=False)
    publication_date = Column(DateTime, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow())

    def __init__(self, title, publication_date):
        self.title = title
        self.publication_date = publication_date

    def __repr__(self):
        return self.id_book

