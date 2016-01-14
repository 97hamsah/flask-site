"""Author: Hampus Sahlin, 2015"""

#importerar flask
from flask import Flask, render_template
from wtfors import Form, StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf import Form
import sqlite3 as lite


#
DATABASE = 'flask-site/database/testdb.db'
DEBUG = True
SECRET_KEY = "Swagboi from the hood"
USERNAME = "admin"
PASSWORD = "12345"

#skapa flask-app
app = Flask(__name__)

#init database
def initdb():
    try:
        con = lite.connect(app.config['DATABASE'])
        cur.con.cursor()
        cur.execute("""CREATE TABLE users(
        uid INTEGER PRIMARY KEY NOT NULL,
        username VARCHAR(10),
        email VARCHAR(30),
        password VARCHAR(10),
        role VARCHAR(10),
        )""")
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        return e


@app.route('/')
@app.route('/startpage/')
def startpage():
    flash("This sida uses kakor!")
    return render_template("startpage.html")

class RegistrationForm(Form):
    pass

@app.route('/register/', methods = ['GET', 'POST'])
def register():
    try:
        form = RegistrationForm(request.form)
    except:
        pass

if (__name__ == "__main__"):
    app.run()
