import MySQLdb
from config import server
from flask import jsonify, request, redirect, render_template, session, flash,url_for
from models import Proprietario
from daofactory import dao

UNIQUE_ERROR_CODE = 1062

class ProprietarioController():

    @server.loggin_required
    def rota_proprietario(self):
        lista_cidades = dao.cidade.lista()
        return render_template('novo_proprietario.html', cidades=lista_cidades)

    def take_message_error(self, error):
        error_message = error.lower().replace("duplicate entry",'').replace("for key",'no campo')
        return error_message

    @server.loggin_required
    def find_prop_by_nome(self):
        prop_name = request.get_json()
        prop_list:list = dao.proprietario.find_by_name("%" + prop_name['name'] + "%")
        prop_list_json = [prop.__dict__ for prop in prop_list]
        return jsonify(prop_list_json),200

    @server.loggin_required
    def criar_proprietario(self):
        tipo_pessoa = int(request.args['tipo_pessoa'])
        prop_data = request.form
        if tipo_pessoa == 0:
            proprietario = Proprietario(prop_data['nome'],prop_data['doc_federal'],prop_data['doc_estadual'],
                                        prop_data['endereco'],prop_data['numero'],prop_data['cep'],
                                        prop_data['celular'],prop_data['email'],prop_data['cidades'],prop_data['bairros'], 
                                        sexo=prop_data['sexo'],telefone=prop_data['telefone'], whatsapp=prop_data['whatsapp'], 
                                        tipo_pessoa=tipo_pessoa)
        else:
            proprietario = Proprietario(prop_data['nome'],prop_data['doc_federal'],prop_data['doc_estadual'],prop_data['endereco'],prop_data['numero'],prop_data['cep'],
                                        prop_data['celular'],prop_data['email'],prop_data['cidades'],prop_data['bairros'], atividade=prop_data['atividade'],
                                        telefone=prop_data['telefone'], whatsapp=prop_data['whatsapp'], tipo_pessoa=tipo_pessoa, razao=prop_data['razao'], 
                                        capital=prop_data['capital'], patrimonio=prop_data['patrimonio'])
        result = dao.proprietario.salvar(proprietario)
        if isinstance(result,MySQLdb.IntegrityError) and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('Proprietario'))
        return redirect(url_for('index'))

    @server.loggin_required
    def editar_proprietario(self,id):
        lista_cidades = dao.cidade.lista()
        proprietario = dao.proprietario.busca_por_id(id)
        return render_template('editar_prop.html', proprietario=proprietario, cidades=lista_cidades)

    @server.loggin_required
    def atualizar_proprietario(self):
        tipo_pessoa = int(request.args['tipo_pessoa'])
        id_prop = int(request.args['id_prop'])
        prop_data = request.form
        if tipo_pessoa == 0:
            proprietario = Proprietario(prop_data['nome'],prop_data['doc_federal'],prop_data['doc_estadual'],
                                        prop_data['endereco'],prop_data['numero'],prop_data['cep'],
                                        prop_data['celular'],prop_data['email'],prop_data['cidades'],prop_data['bairros'], 
                                        sexo=prop_data['sexo'],telefone=prop_data['telefone'], whatsapp=prop_data['whatsapp'], 
                                        tipo_pessoa=tipo_pessoa, id=id_prop)
        else:
            proprietario = Proprietario(prop_data['nome'],prop_data['doc_federal'],prop_data['doc_estadual'],prop_data['endereco'],prop_data['numero'],prop_data['cep'],
                                        prop_data['celular'],prop_data['email'],prop_data['cidades'],prop_data['bairros'], atividade=prop_data['atividade'],
                                        telefone=prop_data['telefone'], whatsapp=prop_data['whatsapp'], tipo_pessoa=tipo_pessoa, razao=prop_data['razao'], 
                                        capital=prop_data['capital'], patrimonio=prop_data['patrimonio'], id=id_prop)
        result = dao.proprietario.salvar(proprietario)
        if isinstance(result,MySQLdb.IntegrityError) and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('editar_prop', id=id_prop))
        return redirect(url_for('index'))

    @server.loggin_required
    def deletar_prop(self,id):
        dao.proprietario.deletar_prop(id)
        return redirect('/')
