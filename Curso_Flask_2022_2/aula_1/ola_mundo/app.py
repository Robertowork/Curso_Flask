# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    #variavel com o nome do usuario (no caso eu mesmo)
    nome= "Roberto Junior"
    return render_template("alo.html", n=nome), 200

app.run()