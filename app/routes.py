from app import myobj
from flask import render_template, Flask, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = "Lisa"
city_names = ['Paris','London','Rome','Tahiti'] 

class CityForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@myobj.route("/", methods=['GET','POST'])
def home():
    form = CityForm()
    if form.validate_on_submit():
        newcity = form.city.data
        if newcity is not None: 
            flash(f"{newcity}")
            return render_template('home.html', name=name, city_names=city_names,form=form)
    return render_template('home.html', name=name, city_names=city_names, form=form)
