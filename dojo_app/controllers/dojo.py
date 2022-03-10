from flask import Flask, render_template, request, redirect
from dojo_app import app
from dojo_app.models.dojo import Dojo
from dojo_app.models.ninja import Ninja

@app.route("/")
def root():
    return redirect("/dojos")

@app.route("/dojos")
def dojo():
    dojos =  Dojo.muestraDojos()
    return render_template("new_dojo.html",dojos=dojos)

@app.route("/create",methods=["POST"])
def create():
    if(request.form["type"]=="dojos"):
        Dojo.createDojo(request.form)
        return redirect("/")
    elif(request.form["type"]=="ninjas"):
        Ninja.createNinja(request.form)
        return redirect("/")

@app.route("/dojos/<int:id>")
def ninjasOfDojo(id):
    form = {"id": id}
    dojo=Dojo.cargaDojo(form)
    return render_template("/show_dojo.html",dojo=dojo)