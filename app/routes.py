from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegisterForm, LoginForm, PropertyForm
from app.models import User, Property
from app import db

main = Blueprint("main", __name__)

@main.route("/")
def landing():
    return render_template("landing.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered.", "danger")
            return redirect(url_for("main.register"))

        user = User(
            full_name=form.full_name.data,
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login successful.", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)

@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "owner":
        return render_template("owner_dashboard.html")
    elif current_user.role == "tenant":
        return render_template("tenant_dashboard.html")
    elif current_user.role == "admin":
        return render_template("admin_dashboard.html")
    return redirect(url_for("main.login"))

@main.route("/owner/properties", methods=["GET", "POST"])
@login_required
def owner_properties():
    if current_user.role != "owner":
        flash("Unauthorized access.", "danger")
        return redirect(url_for("main.dashboard"))

    form = PropertyForm()
    properties = Property.query.filter_by(owner_id=current_user.id).all()

    if form.validate_on_submit():
        new_property = Property(
            title=form.title.data,
            location=form.location.data,
            rent_amount=form.rent_amount.data,
            description=form.description.data,
            owner_id=current_user.id
        )
        db.session.add(new_property)
        db.session.commit()
        flash("Property added successfully.", "success")
        return redirect(url_for("main.owner_properties"))

    return render_template("owner_properties.html", form=form, properties=properties)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("main.login"))