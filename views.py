from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")
from chatbox import getReturnMsg

resp = []
msgLst = []
msgcount = 0

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
    global resp, msgcount, msgLst
    if request.method == 'POST':
        msg = request.form['qns']
        if len(resp)==0 or msg!=msgLst[-1]:
            msgLst.append(msg)
            resp.append(getReturnMsg(msg))
            msgcount = msgcount+1
        return render_template("strangers.html", arg0=resp, arg1 = msgcount, arg2 = msgLst)
    else:
        return render_template("strangers.html", arg0=resp, arg1 = msgcount, arg2 = msgLst)

@views.route("/protection")
def protection():
    return render_template("protect_info.html")

@views.route("/quiz")
def quiz():
    return "quiz"

# @views.route("/reset",methods=['POST'])
# def reset():
#     global resp, msgcount
#     resp = []
#     msgcount = 0
#     return jsonify(success=True)