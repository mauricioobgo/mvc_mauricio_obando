from app_index import database
import db.user
import db.book
import db.comments
database.create_all()
print("database created with success...")