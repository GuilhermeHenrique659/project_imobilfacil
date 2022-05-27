import MySQLdb
from flask import request, redirect, render_template, session, flash,url_for, jsonify
from models import Corretores
from daofactory import dao
import bcrypt
from config import server

UNIQUE_ERROR_CODE = 1062

class CorretorController():

    @server.loggin_required
    def rota_corretor(self):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=novo_corretor.html')
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        return render_template('novo_corretor.html', cidades=lista_cidades, bairros=lista_bairro)

    def take_message_error(self, error):
        error_message = error.lower().replace("duplicate entry",'').replace("for key",'no campo')
        return error_message
    
    @server.loggin_required
    def find_by_name(self):
        corr_name = request.get_json()
        corr_list:list = dao.corretor.find_by_name("%" + corr_name['name'] + "%")
        corr_list_json = [corr.__dict__ for corr in corr_list]
        return jsonify(corr_list_json),200


    @server.loggin_required
    def criar_Corretor(self):
        corretor = dao.corretor.buscar_por_id(request.form['usuario_corr'])
        usuario = request.form['usuario_corr']
        email = request.form['email_corr']
        nome = request.form['nome_corr']
        creci = request.form['creci_corr']
        celular = request.form['celular_corr']
        cpf = request.form['cpf_corr']
        endereco = request.form['endereco_corr']
        senha = request.form['senha_corr']
        cidade = request.form['cidades']
        bairro = request.form['bairros']
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        corretor = Corretores(usuario, email, nome, creci, celular, cpf, endereco, senha, cidade, bairro)
        result = dao.corretor.salvar(corretor)
        if isinstance(result,MySQLdb.IntegrityError) and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('Corretor'))
        return redirect('/')

    @server.loggin_required
    def editar_corretor(self,id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=''')
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        corretor = dao.corretor.busca_por_id_edit(id)
        return render_template('editar_corr.html', corretor=corretor, cidades=lista_cidades, bairros=lista_bairro)


    @server.loggin_required
    def atualizar_corretor(self):
        usuario = request.form['usuario_corr']
        email = request.form['email_corr']
        nome = request.form['nome_corr']
        creci = request.form['creci_corr']
        celular = request.form['celular_corr']
        cpf = request.form['cpf_corr']
        endereco = request.form['endereco_corr']
        senha = request.form['senha_corr']
        cidade = request.form['cidades']
        bairro = request.form['bairros']
        id = request.form['id_corr']
        if (senha != ""):
            senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        corretor = Corretores(usuario, email, nome, creci, celular, cpf, 
                                    endereco, senha, cidade, bairro, id)
        result = dao.corretor.salvar(corretor)
        if isinstance(result,MySQLdb.IntegrityError) and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('editar_corretor', id=id))
        return redirect('/')


    @server.loggin_required
    def deletar_corr(self,id):
        dao.corretor.deletar_corr(id)
        return redirect('/')
