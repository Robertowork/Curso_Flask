# coding: utf-8
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask("projeto")
#criando uma chave de criptografia
app.secret_key = "faojldsnofnawuendfljk"

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

#rota para formulario de login
@app.route("/login")
def login():
    return render_template("login.html"), 200

#rota para validar o formulario de login
@app.route("/login_validar", methods=["POST"])
def login_validar():
    if request.form["usuario"] == "roberto" and request.form["senha"] == "12345":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))
    else:
        return "usuario/senha invalidos, digite novamente.", 200
# Rota para a area restrita
@app.route("/restrito")
def acesso_restrito():
    if session["codigo"] == 1:
        return "Bem-vindo à area restrita!!<br>Usuário: {}<br>Código: {}".format(session["usuario"], session["codigo"]), 200
    else:
        return "Acesso inválido", 200

app.run() 