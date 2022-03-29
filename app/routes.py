from app import myobj
from flask import render_template, Flask, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = "Lisa"
city_names = ['Paris','London','Rome','Tahiti'] 

class cityForm(FlaskForm):
    cityname = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
  
@myobj.route("/", methods=['GET','POST'])
def home(): 
    form = cityForm()
    if form.validate_on_submit():
        newcity = ""
        newcity = newcity + f'{form.cityname.data}'
        if newcity is not None: 
            flash(f"{form.cityname.data}")
            return render_template('home.html', name=name, city_names=city_names,form=form)
    return render_template('home.html', name=name, city_names=city_names, form=form)
