from app import myobj
from flask import render_template, Flask, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

@myobj.route("/", methods=['GET','POST'])
def home():
    user = {'username': "Lisa"}
    cities = ['Paris','London','Rome','Tahiti']
    class cityForm(FlaskForm):
        cityname = StringField('City Name', validators=[DataRequired()])
        submit = SubmitField('Submit')

    form = cityForm()
    if form.validate_on_submit():
        newcity = ""
        newcity = newcity + f'{form.cityname.data}'
        if newcity is not None: 
            flash(f"{form.cityname.data}")
            return render_template('home.html', name=user['username'], city_names=cities,form=form)
    return render_template('home.html', name=user['username'], city_names=cities, form=form)
