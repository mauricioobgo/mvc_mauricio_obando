from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime,Text
from app_index import  database

class Comments(database.Model):

    id_comment=Column(Integer, primary_key=True)
    id_book=Column(Integer,ForeignKey('book.id_book'))
    text=Column(Text)
    id_user=Column(Integer,ForeignKey('user.id_user'))
    created_date=Column(DateTime, default=datetime.utcnow())
    def __init__(self,id_book,text,id_user):
        self.id_book=id_book
        self.text=text
        self.id_user=id_user
    def __repr__(self):
        return self.id_comment