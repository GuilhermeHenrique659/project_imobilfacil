from config import server
from flask import request, redirect, render_template, session, flash,url_for
from models import Proprietario
from daofactory import dao

class ProprietarioController():

    @server.loggin_required
    def rota_proprietario(self):
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        return render_template('novo_proprietario.html', cidades=lista_cidades, bairros=lista_bairro)

    @server.loggin_required
    def criar_proprietario(self):
        nome = request.form['nome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        email = request.form['email']
        cidade = request.form['cidades']
        bairro = request.form['bairros']
        proprietario = Proprietario(nome, cpf, rg, endereco, telefone, email, cidade, bairro)
        proprietario.set_cidade(proprietario.valida(cidade))
        proprietario.set_bairro(proprietario.valida(bairro))
        dao.proprietario.salvar(proprietario)
        return redirect('/')

    @server.loggin_required
    def editar_proprietario(self,id):
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        proprietario = dao.proprietario.busca_por_id(id)
        return render_template('editar_prop.html', proprietario=proprietario, cidades=lista_cidades,
                               bairros=lista_bairro)

    @server.loggin_required
    def atualizar_proprietario(self):
        nome = request.form['nome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        email = request.form['email']
        cidade = request.form['cidades']
        bairro = request.form['bairros']
        id = request.form['id']
        proprietario = Proprietario(nome, cpf, rg, endereco, telefone, email, cidade, bairro, id)
        proprietario.set_cidade(proprietario.valida(cidade))
        proprietario.set_bairro(proprietario.valida(bairro))
        dao.proprietario.salvar(proprietario)
        return redirect('/')

    @server.loggin_required
    def deletar_prop(self,id):
        dao.proprietario.deletar_prop(id)
        return redirect('/')
