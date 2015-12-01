"""Author: Hampus Sahlin, 2015"""

#importerar flask
from flask import Flask

#skapa flask-app
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def startpage():
    return "Hello World"

if (__name__ == "__main__"):
    app.run