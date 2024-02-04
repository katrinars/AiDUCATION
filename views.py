from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")


'''
suggested routing for planned pages
'''
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/links")
def links():
    return render_template("links.html")

@views.route("/ai")
def ai():
    return render_template("ai.html")

@views.route("/strangers", methods = ['POST','GET'])
def strangers():
    if request.method == 'POST':
        usr = request.form['nm']
        print(usr)
        return render_template("strangers.html", arg0=usr)
    else:
        return render_template("strangers.html", arg0='')

@views.route("/protection")
def protection():
    return render_template("protect_info.html")

@views.route("/quiz")
def quiz():
    return "quiz"