#!/usr/bin/env python
#from distutils.log import error
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect, request

app=Flask(__name__)


@app.route("/")
def home():
    return "<h1 style='color:blue'> Pagina principal </h1>"

@app.route("/des")
def description():
    return render_template('description.html')


@app.route('/oper', methods=["POST", "GET"])
def operacions():
    if request.method == "POST":
     if request.form["operate"] == "suma":
        valor = float(request.form["num1"]) + float(request.form["num2"])
        return str(valor)
     if request.form["operate"] == "resta":
        valor = float(request.form["num1"]) - float(request.form["num2"])
        return str(valor)
     if request.form["operate"] == "multiplicar":
        valor = float(request.form["num1"]) * float(request.form["num2"])
        return str(valor)
     if request.form["operate"] == "dividir":
        if float(request.form["num2"]) == 0:
            return "Record not found", 400
        else:
         valor = float(request.form["num1"]) / float(request.form["num2"])
         return str(valor)
    else:
         return render_template('operacio.html')



if __name__== "__main__":
    app.run(debug=True, port=5000)

