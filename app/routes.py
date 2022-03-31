from app import myobj
from flask import render_template, Flask, flash, request

name = "Lisa"
city_names = ['Paris','London','Rome','Tahiti']

@myobj.route("/", methods=['GET','POST'])
def home():
    if request.method == "POST":
        newcity = request.form.get('city')
        if newcity is not None:
            flash(f"{newcity}")
            return render_template('home.html', name=name, city_names=city_names)
    return render_template('home.html', name=name, city_names=city_names)
