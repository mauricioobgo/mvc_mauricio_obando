from datetime import datetime
from sqlalchemy import  Column, Integer, String, DateTime
from app_index import  database

class User(database.Model):
        id_user=Column(Integer, primary_key=True, nullable=False  )
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

        def __repr__(self):
            return self.id_user