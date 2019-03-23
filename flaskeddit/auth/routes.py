from flask import render_template, redirect
from flaskeddit.auth import auth_bp
from flaskeddit.auth.forms import RegisterForm, LoginForm


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect("/login")
    else:
        print(form.username.errors)
        print(form.password.errors)
        print(form.confirm_password.errors)
    return render_template("register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    else:
        print(form.username.errors)
        print(form.password.errors)
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    return redirect("/login")