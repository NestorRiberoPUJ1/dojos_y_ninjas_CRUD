from flask import Flask, render_template, request, redirect
from dojo_app import app
from dojo_app.models.dojo import Dojo

@app.route("/")
def root():
    return redirect("/dojo")

@app.route("/dojo")
def dojo():
    dojos =  Dojo.muestraDojos()
    return render_template("new_dojo.html",dojos=dojos)