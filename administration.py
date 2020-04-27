
tehlikelistesi =  ['<?php','<?=','?>','<?','select','SELECT','sleep','SLEEP','XOR','xor','insert','INSERT','into','UNION','now(',"'",'/','/','sleep(','sysdate(','if(','union','"SELECT"','INTO','update','UPDATE','delete','DELETE','%','"','(',')','<?php','<?=','?>','<script>','</script>','<a href=','</a>','<a>']
import random
from flask import Flask,g,render_template,flash,redirect,url_for,session,logging,request
from passlib.hash import sha256_crypt


from functools import wraps
app = Flask("__name__")

app.secret_key ="talsiir"

"""
class RegisterForm(Form):
	name = StringField("İsminiz ve soyisminiz")
	email = StringField("E-mail adresiniz",validators = [validators.Email(message = "Lütfen Geçerli Bir E-mail Adresi Girin.")])
	password = PasswordField("Parola",validators = [

		validators.DataRequired(message = "Lütfen Bir Parola Belirleyin."),
		validators.EqualTo(fieldname = "confirm",message = "Parolalar uyuşmuyor..")


	])
	confirm = PasswordField("Parolanızı Doğrulayın")

	#---------------------------------------
class LoginForm(Form):
	email = StringField("E-mail Adresiniz")
	password = PasswordField("Parolanız")

"""


"""
@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm(request.form)

    if request.method =="POST":
        email = form.email.data
        password_entered = form.password.data

        cursor = con.connection.cursor()
        sorgu="Select * From users where email = %s"
        result = cursor.execute(sorgu,(email,))

        if result == 0:
            return redirect(url_for("register"))
        else:
            data = cursor.fetchone()
            real_password = data["password"]

            if sha256_crypt.verify(password_entered,real_password):
                session["logged_in"] = True
                return redirect(url_for("index"))
            else:
                return render_template("login.html",form = form)


    else:
        return render_template("login.html",form = form)
"""

"""
@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method =="POST":
        name = form.name.data
        email = form.email.data

        password =sha256_crypt.encrypt(form.password.data)

        cursor = con.connection.cursor()
        sorgu01="Select * From users where email = %s"
        result = cursor.execute(sorgu01,(email,))

        if result == 0:
            sorgu02 ="Insert into users(name,email,password) VALUES(%s,%s,%s)"
            cursor.execute(sorgu02,(name,email,password))
            con.connection.commit()
            cursor.close()

            
            return redirect(url_for("login"))
        else:
            flash("Bu e-mail adresi zaten kullanılmaktadır.","danger")
            return render_template("register.html",form = form)
    else:
        return render_template("register.html",form = form)
"""
"""
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))




"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
if __name__ == "__main__":
	app.run(debug = True)