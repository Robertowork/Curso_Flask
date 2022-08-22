# coding: utf-8
from flask import Flask, render_template
tabela = Flask("projeto")
@tabela.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome="Seu Nome"
    produtos = [
    {"nome": "Ração", "preco": 199.99},
    {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200

tabela.run()