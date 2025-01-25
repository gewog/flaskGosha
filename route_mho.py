from flask import Blueprint, render_template


main_bp = Blueprint('main', __name__, url_prefix='')

@main_bp.route("/")
def main_page():
    """Главная базовая страница"""
    data = 'hi'
    return render_template("main.html", data=data)

@main_bp.route("/about")
def about_page():
    """Страница About"""
    return render_template("about.html")

@main_bp.route("/home")
def home_page():
    """Страница Home"""
    return render_template("home.html", )