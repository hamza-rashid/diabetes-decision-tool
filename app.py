from flask import Flask, render_template, request, redirect, url_for
from decision import decision_tree
from links import getlink

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data', methods=["POST", "GET"])
def data():
    if request.method== 'POST':
        form_data = request.form
        if request.form["appCategory"] != "Choose one of these categories" and request.form["platform"] != "Choose one of these options" :
            #return form_data
            appchoice = decision(request.form["appCategory"], 
            request.form["number2"],
            request.form["number3"],
            request.form["number4"],
            request.form["number5"],
            request.form["number6"],
            request.form["number7"])
        
            return redirect(getlink(appchoice, request.form["platform"]), code=302)
        else:
            return redirect('/')





        #return redirect("http://www.google.com", code=302)

