from flask import Flask, render_template, request, redirect, url_for, session
from flask import *
from sqlite3 import *
from flask_mail import *
from random import randrange
import pickle

app=Flask(__name__)
app.secret_key="gilmore_girls"

app.config['MAIL_SERVER']="smtp.gmail.com"
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']="mlflaskcodedeveloper@gmail.com"
app.config['MAIL_PASSWORD']="mlflask21"
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False
mail=Mail(app)

@app.route("/", methods=["GET", "POST"])
def home():
	return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method=="POST":
		un = request.form["un"]
		pw = request.form["pw"]
		con = None
		try:
			con=connect("mlusers.db")
			cursor=con.cursor()
			sql = "select * from users where username = '%s' and password= '%s'"
			cursor.execute(sql % (un, pw)) 
			data= cursor.fetchall()
			print(data)
			if len(data)==0:
				return render_template("login.html", msg="Invalid Credentials!!")
			else:
				session["username"]=un
				return redirect(url_for("index"))
		except Exception as e:
			msg="Issue!"
			return render_template("login.html", msg=str(e))
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method=="POST":
		un = request.form["un"]
		em = request.form["em"]
		pw1 = request.form["pw1"]
		pw2 = request.form["pw2"]
		if pw1 == pw2:
			con = None
			try:
				con=connect("mlusers.db")
				cursor=con.cursor()
				sql = "insert into users values('%s','%s','%s')"
				cursor.execute(sql % (un, em, pw1)) 
				con.commit()
				return redirect(url_for("login"))
			except Exception as e:
				con.rollback()
				return render_template("signup.html", msg=str(e))
			finally:
				if con is not None:
					con.close()
		else:
			return render_template("signup.html", msg="Passwords do not match, try again!!")
	else:
		return render_template("signup.html")
	
@app.route("/logout", methods=["GET", "POST"])
def logout():
	session.pop("username", None)
	return redirect(url_for('home'))
	
@app.route("/index", methods=["GET", "POST"])
def index():
	if request.method=="POST":
		o = request.form["o"]
		n = request.form["n"]
		c = request.form["c"]
		a = request.form["a"]
		e = request.form["e"]
		d=[[o, n, c, a, e]]
		with open("db.model", "rb") as f:
			model = pickle.load(f)
		res=model.predict(d)
		print(res)
		res=str(res[0])
		print(res)
		r = res[0].upper()
		res = r+ res[1:]
		print(res)
		un = session["username"]
		print(un)
		con = None
		try:
			con=connect("mlusers.db")
			cursor=con.cursor()
			sql = "select email from users where username = '%s'"
			cursor.execute(sql % (un)) 
			data = cursor.fetchone()
			print(data)
			if len(data)==0:
				return render_template("index.html", msg="Issue!!")
			else:
				em = data[0]
				print(em)
				mailmsg = Message("Your Personality Report Is Here!!", sender="mlflaskcodedeveloper@gmail.com", recipients=[em])
				print(mailmsg)
				mailmsg.body="Greetings!!\n\nWelcome "+un+", \n\nWe are pleased to tell you belong to the "+res+" Personality Type. \n\nPlease find the attachment provided below to know the details. \n\nKeep Growing!! \n\nIf you do have any futher queries, kindly contact us via email at mlflaskcodedeveloper@gmail.com \n\nThank You for using our web application. \n\nRegards, \nThe ML-Flask Team."
				print(mailmsg.body)
				if res == "Serious":
					with app.open_resource("serious.png") as fp:
    						mailmsg.attach("serious.png", "image/png", fp.read())
				elif res == "Extraverted":
					with app.open_resource("extraverted.png") as fp:
    						mailmsg.attach("extraverted.png", "image/png", fp.read())
				elif res == "Responsible":
					with app.open_resource("responsible.png") as fp:
    						mailmsg.attach("responsible.png", "image/png", fp.read())
				elif res == "Lively":
					with app.open_resource("lively.png") as fp:
    						mailmsg.attach("lively.png", "image/png", fp.read())
				elif res == "Dependable":
					with app.open_resource("dependable.png") as fp:
    						mailmsg.attach("dependable.png", "image/png", fp.read())
				mail.send(mailmsg)
				return render_template("index.html", msg="You belong to the "+res+" Personality type. We have emailed you your personality report on your registered Email ID!")
		except Exception as e:
			msg="Issue!"
			return render_template("index.html", msg=str(e))
		finally:
			if con is not None:
				con.close()
		
	else:
		return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
