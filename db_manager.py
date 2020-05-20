from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime,Text
from flask_sqlalchemy import SQLAlchemy

class User(SQLAlchemy):

        id_user=Column(Integer, primary_key=True)
        username=Column(String(400),nullable=False, unique=True)
        first_name=Column(String(400),nullable=False)
        last_name=Column(String(400),nullable=False)
        password=Column(String(300),nullable=False)
        date_created=Column(DateTime,default=datetime.utcnow())
        def __init__(self,username,first_name,last_name,password):
            self.username=username
            self.first_name=first_name
            self.last_name=last_name
            self.password=password




class Book(SQLAlchemy):

        id_book=Column(Integer, primary_key=True)
        title=Column(String(400),nullable=False)
        publication_date=Column(DateTime, nullable=False)
        date_created = Column(DateTime, default=datetime.utcnow())
        def __init__(self,title,publication_date):
            self.title=title
            self.publication_date=publication_date





class Comments(SQLAlchemy):

    id_comment=Column(Integer, primary_key=True)
    id_book=Column(Integer,ForeignKey('Book.id_book'))
    text=Column(Text)
    id_user=Column(Integer,ForeignKey('User.id_user'))
    created_date=Column(DateTime, default=datetime.utcnow())
    def __init__(self,id_book,text,id_user):
        self.id_book=id_book
        self.text=text
        self.id_user=id_user
