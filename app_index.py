from flask import Flask,render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from api_consumption import *
import os
#Init app
app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
#DataBase
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'sqlite_api.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
database=SQLAlchemy(app)
api=api_consumption()
#llamado de bases de datos
import db.book
import db.user
import db.comments
@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.method=='POST'):
        validateInfoUser=request.form['user_name_id']
        if(validateInfoUser!= ""):
            try:
                validator=database.session.query(db.user.User.id_user==validateInfoUser).all()
            except:

        else:
            return redirect('/')

    else:
        return render_template("index.html")


@app.route('/user_creator', methods=['POST','GET'])
def create_users():
    return render_template("user_creator.html")

@app.route('/crud_books_content', methods=['POST','GET'])
def crud_creation_modf():
    return render_template("crud_books_comments.html")

@app.route('/api_consumption', methods=['GET','POST'])
def api_consumption_collect():
    if (request.method=="POST"):
        tweetSearch=api.query_search_api(search_tweet,"2020-01-01",20)
        return render_template("api_consumption.html", tweets=tweetSearch)
    else:
        return render_template("api_consumption.html")

if __name__=="__main__":
    app.run(debug=True)