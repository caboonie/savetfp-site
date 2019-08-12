#!/usr/bin/python
from databases import *
from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session as login_session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lkjdflaskjdyou-will-never-guess'

@app.route('/')
def home():
	events=query_events()
	events.sort(key=lambda x:x.start)
	return render_template('homeLayout.html', imgs=query_images(), events=events)

@app.route('/members')
def members():
    return render_template('membersLayout.html', members=query_members()) 

@app.route('/faq')
def faq():
    return render_template('faq.html') 

@app.route('/contact')
def contact():

	return render_template('contact.html') 

@app.route('/message', methods=["POST"])
def message():
	flash("Thank you for the feedback!")
	return render_template('contact.html') 

@app.route('/admin')
def admin():
	if "logged-in" in login_session and login_session["logged-in"]:
		events=query_events()
		events.sort(key=lambda x:x.start)
		return render_template('admin.html', members=query_members(), imgs=query_images(), events=events) 
	else:
		flash("please login to view that page")
		return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
	if request.form['username'] == "admin" and request.form['password'] == "admin":
		login_session['logged-in'] = True;
		return redirect("/admin")
	else:
		flash("incorrect username or password")
		return render_template('login.html')


@app.route('/addEvent', methods=["POST"])
def addEvent():
	if "logged-in" in login_session and login_session["logged-in"]:
		name = request.form['name']
		desc = request.form['descrip']
		date = request.form['date']
		date = datetime.datetime.strptime(request.form["date"],"%Y-%m-%d")
		print(request.form["start"],request.form["end"])
		if(len(request.form['start'])==8):
			start = datetime.datetime.strptime(request.form["start"],"%H:%M:%S")
			end = datetime.datetime.strptime(request.form["end"],"%H:%M:%S")
		else:
			start = datetime.datetime.strptime(request.form["start"],"%H:%M")
			end = datetime.datetime.strptime(request.form["end"],"%H:%M")
		print(date,"\n",start)
		start = datetime.datetime(date.year,date.month,date.day,start.hour,start.minute)
		end = datetime.datetime(date.year,date.month,date.day,end.hour,end.minute)
		pic = "default.png"
		print(request.files)
		if 'pic' in request.files:
			f = request.files['pic']
			pic = "static/imgs/"+f.filename
			f.save(pic)

		add_event(name,start,end,desc,pic)
		return redirect("/admin")
	else:
		return render_template('login.html')

@app.route('/removeEvent/<int:id>')
def removeEvent(id):
	if "logged-in" in login_session and login_session["logged-in"]:
		delete_event(id)
		return redirect("/admin")
	else:
		return render_template('login.html')

@app.route('/addMember', methods=["POST"])
def addMember():
	if "logged-in" in login_session and login_session["logged-in"]:
		name = request.form['name']
		desc = request.form['descrip']
		pic = "default.png"
		print(request.files)
		if 'pic' in request.files:
			f = request.files['pic']
			pic = "static/imgs/"+f.filename
			f.save(pic)

		add_member(name,desc,pic)
		return redirect("/admin")
	else:
		return render_template('login.html')

@app.route('/removeMember/<int:id>')
def removeMember(id):
	if "logged-in" in login_session and login_session["logged-in"]:
		delete_member(id)
		return redirect("/admin")
	else:
		return render_template('login.html')

@app.route('/addImage', methods=["POST"])
def addImage():
	if "logged-in" in login_session and login_session["logged-in"]:
		pic = "default.png"
		print(request.files)
		if 'pic' in request.files:
			f = request.files['pic']
			pic = "static/imgs/"+f.filename
			f.save(pic)

		add_image(pic)
		return redirect("/admin")
	else:
		return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
