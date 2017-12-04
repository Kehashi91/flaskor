# includes flask   Downloading Flask_Moment-0.5.2-py2.py3-none-any.whl
#   Using cached Flask_WTF-0.14.2-py2.py3-none-any.whl

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "faHD^kd&^djflhdJASHG1"
WTF_CSRF_SECRET_KEY = 'das90d8sa342gDDF!$!'
Bootstrap(app)
moment = Moment(app)

titles = [("rumak", "lorem ipsum", "avek1.jpg"), ("nie znam laciny", "dis sucks", "avek2.jpg")]

class NameForm(FlaskForm):
    name = StringField("Whats ur name", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        oldname = session.get('name')
        if oldname is not None and oldname != form.name.data:
            flash("Looks like new name!")
        session['name'] = form.name.data
        # form.name.data = ""
        return redirect(url_for('index'))
    return render_template("index.html", current_time=datetime.utcnow(), form=form, name=session.get('name'))

@app.route("/sandbox.html")
def sandbox():
    return render_template("sandbox.html", contents=titles)

@app.route("/template.html")
def template():
    return render_template("template.html")

@app.errorhandler(404)
def err404(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
