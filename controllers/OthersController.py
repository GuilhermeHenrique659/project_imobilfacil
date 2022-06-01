from flask import  request, redirect, render_template, session, flash,url_for
from models import Cidade,Bairro
from daofactory import dao
from config import server

class OthersController:
    @server.loggin_required
    def nova_cidade(self):
        cidade_nome = request.form['cidade']
        cidade = Cidade(cidade_nome, request.form['uf'])
        previous = request.form['previous']
        try:
            dao.cidade.salvar(cidade)
        except Exception:
            flash("Cidade já cadastrada")
            return redirect(previous)
        return redirect(previous)

    @server.loggin_required
    def novo_bairro(self):
        cidade = request.form['cidade_bairro']
        bairro_nome = request.form['bairro']
        bairro = Bairro(bairro_nome, cidade)
        previous = request.form['previous']
        try:
            dao.bairro.salvar(bairro)
        except Exception:
            flash("Bairro já cadastrado nessa cidade")
            return redirect(previous)
        return redirect(previous)


