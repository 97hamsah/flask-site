"""Author: Hampus Sahlin, 2015"""

#importerar flask
from flask import Flask, render_template

#skapa flask-app
app = Flask(__name__)

@app.route('/')
@app.route('/startpage/')
def startpage():
    flash("Hello World!"")
    return render_template("startpage.html")

if (__name__ == "__main__"):
    app.run
