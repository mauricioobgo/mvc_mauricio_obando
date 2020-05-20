from flask import Flask,render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import or_,and_
from api_consumption import *
import logging
import os
logging.basicConfig(level=logging.DEBUG)
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
        paswword_validation=request.form['pass_word']
        if(validateInfoUser!= ""):
            #para creación de Usuario
            # user_validate = db.user.User(username=validateInfoUser)
            try:
                #validator=db.user.User.query.filter_by(and_(db.user.User.username.like('%'+str(validateInfoUser)+'%'),db.user.User.password==str(paswword_validation))).all()
                validator = database.session.query(db.user.User.id_user).filter_by(username=validateInfoUser,password=paswword_validation).all()
                database.session.close()
                if(len(validator)==0):
                    app.logger.info(print("llegue"))
                    return redirect('/',validation=True)
                else:
                    #retorna el id del usuario
                    app.logger.info(validator[0][0])
                    return redirect('/crud_books_content/')
            except:
                return 'no encontró nada'
        else:
            return redirect('/')

    else:
        return render_template("index.html")


@app.route('/user_creator', methods=['POST','GET'])
def create_users():
    if ( request.method=='POST'):
        try:
            user_name_new=request.form['user_name_new']
            first_name_new=request.form['first_name_new']
            last_name_new=request.form['last_name_new']
            pass_word_new=request.form['pass_word_creator']
            newUser=db.user.User(user_name_new,first_name_new,last_name_new,pass_word_new)
            database.session.add(newUser)
            database.session.commit()
            database.session.close()
            return redirect('/user_creator')
        except:
            return redirect("/")
    else:
        return render_template("user_creator.html")

@app.route('/crud_books_content', methods=['POST','GET'])
def crud_creation_modf():
    if(request.method=='POST'):
        #try:
            new_book_title = request.form['title_book']
            new_book_publication_date=request.form['publication_date_book']
            new_book_publication_date=datetime.strptime(new_book_publication_date,'%Y-%m-%d')
            new_book_add = db.book.Book(new_book_title,new_book_publication_date)
            database.session.add(new_book_add)
            database.session.commit()
            database.session.close()
            last_id=database.session.query(db.book.Book.id_book).orderby()

            return redirect('/crud_books_content')
        #except:
         #   return redirect("/")
    else:
        return render_template("crd_bk_com.html")

@app.route('/api_consumption', methods=['GET','POST'])
def api_consumption_collect():
    if (request.method=="POST"):
        search_tweet="bigdata"
        tweetSearch=api.query_search_api(search_tweet,"2020-01-01",20)
        return render_template("api_consumption.html", tweets=tweetSearch)
    else:
        return render_template("api_consumption.html")

if __name__=="__main__":
    app.run(debug=True)