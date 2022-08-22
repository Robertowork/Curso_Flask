# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome="Seu Nome"
    produtos = [
    {"nome": "Ração", "preco": 199.99},
    {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200
# Nova Rota Teste
@app.route("/teste")
@app.route("/teste/<carro_do_leite>")
def funcao_teste(carro_do_leite = ""):
    return "Nova rota teste<br>variável: {}".format(carro_do_leite), 200
app.run() 