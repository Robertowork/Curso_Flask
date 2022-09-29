# coding: utf-8
from flask import Flask, render_template, request
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
@app.route("/teste/<teste_de_rota>")
def funcao_teste(teste_de_rota = ""):
    return "Nova rota teste<br>variável: {}".format(teste_de_rota), 200

#Rota do formulario
@app.route("/form")
def form():
    return render_template("form.html"), 200

#rota de tratamento do formulario

@app.route("/form_recebe", methods=["GET","POST"])
def form_recebe():
    if request.method == "POST":
        nome = request.form["Roberto"]
        return "Nome: {}" .format(nome), 200
    else:
        return "Não pode chamar direto no GET", 200

app.run() 