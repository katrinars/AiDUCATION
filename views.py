from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


'''
suggested routing for planned pages
'''
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/links")
def links():
    return "suspicious links/urls"

@views.route("/privacy")
def privacy():
    return "social media/ai"

@views.route("/strangers")
def strangers():
    # return "good practices when talking to strangers"
    return render_template("strangers.html")

@views.route("/protection")
def protection():
    return "protecting important personal information"

@views.route("/quiz")
def quiz():
    return "quiz"