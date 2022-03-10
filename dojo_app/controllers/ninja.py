from flask import Flask, render_template, request, redirect
from dojo_app import app
from dojo_app.models.dojo import Dojo
from dojo_app.models.ninja import Ninja


@app.route("/ninjas")
def ninja():
    dojos = Dojo.muestraDojos()
    return render_template("new_ninja.html", dojos=dojos)


