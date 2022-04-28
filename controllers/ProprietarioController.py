from os import popen
import re
from config import server
from flask import request, redirect, render_template, session, flash,url_for
from models import Proprietario
from daofactory import dao

UNIQUE_ERROR_CODE = 1062

class ProprietarioController():

    @server.loggin_required
    def rota_proprietario(self):
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        return render_template('novo_proprietario.html', cidades=lista_cidades, bairros=lista_bairro)

    @server.loggin_required
    def criar_proprietario(self):
        tipo_pessoa = int(request.args['tipo_pessoa'])
        prop_data = request.form
        print(tipo_pessoa)
        if tipo_pessoa == 0:
            proprietario = Proprietario(prop_data['nome'],prop_data['doc_federal'],prop_data['doc_estadual'],
                                        prop_data['endereco'],prop_data['numero'],prop_data['cep'],
                                        prop_data['celular'],prop_data['email'],prop_data['cidades'],prop_data['bairros'], 
                                        sexo=prop_data['sexo'],telefone=prop_data['telefone'], whatsapp=prop_data['whatsapp'], 
                                        tipo_pessoa=tipo_pessoa, codigo=prop_data['codigo'])
        else:
            proprietario = Proprietario(prop_data['nome'],prop_data['doc_federal'],prop_data['doc_estadual'],prop_data['endereco'],prop_data['numero'],prop_data['cep'],
                                        prop_data['celular'],prop_data['email'],prop_data['cidades'],prop_data['bairros'], atividade=prop_data['atividade'],
                                        telefone=prop_data['telefone'], whatsapp=prop_data['whatsapp'], tipo_pessoa=tipo_pessoa, razao=prop_data['razao'], 
                                        codigo=prop_data['codigo'], capital=prop_data['capital'], patrimonio=prop_data['patrimonio'])
        result = dao.proprietario.salvar(proprietario)
        if result == UNIQUE_ERROR_CODE:
            flash('codigo ja ultilizado')
            return redirect(url_for('Proprietario'))
        return redirect(url_for('index'))

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
        dao.proprietario.salvar(proprietario)
        return redirect('/')

    @server.loggin_required
    def deletar_prop(self,id):
        dao.proprietario.deletar_prop(id)
        return redirect('/')
