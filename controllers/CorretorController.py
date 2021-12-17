from controllers.controller import *
from models import Corretores

class CorretorController(Controller):
    def __init__(self, Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao):
        super().__init__(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao)

    def rota_corretor(self):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=novo_corretor.html')
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        return render_template('novo_corretor.html', cidades=lista_cidades, bairros=lista_bairro)

    def criar_Corretor(self):
        corretor = self._Corretores_dao.buscar_por_id(request.form['usuario_corr'])
        if corretor:
            flash('usuário já existe')
            return redirect(url_for('rota_corretor'))
        else:
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
            corretor.set_user(corretor.valida(usuario))
            corretor.set_cidade(corretor.valida(bairro))
            corretor.set_bairro(corretor.valida(cidade))
            corretor.set_email(corretor.valida(email))
            self._Corretores_dao.salvar(corretor)

        return redirect('/')

    def editar_corretor(self,id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=''')
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        corretor = self._Corretores_dao.busca_por_id_edit(id)
        return render_template('editar_corr.html', corretor=corretor, cidades=lista_cidades, bairros=lista_bairro)

    def atualizar_corretor(self):
        corretor_busq = self._Corretores_dao.buscar_por_id(request.form['usuario_corr'])
        usuario_verifc = request.form['ussuario_verif']
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
        if usuario_verifc == usuario:
            corretor = Corretores(usuario, email, nome, creci, celular, cpf, endereco, senha, cidade, bairro, id)
            corretor.set_user(corretor.valida(usuario))
            corretor.set_cidade(corretor.valida(cidade))
            corretor.set_bairro(corretor.valida(bairro))
            corretor.set_email(corretor.valida(email))
            self._Corretores_dao.salvar(corretor)

        elif corretor_busq:
            flash('usuário já existe')
            return redirect(url_for('editar_corretor', id=id))
        else:
            corretor = Corretores(usuario, email, nome, creci, celular, cpf, endereco, senha, cidade, bairro, id)
            corretor.set_user(corretor.valida(usuario))
            corretor.set_cidade(corretor.valida(cidade))
            corretor.set_bairro(corretor.valida(bairro))
            corretor.set_email(corretor.valida(email))
            self._Corretores_dao.salvar(corretor)

        return redirect('/')

    def deletar_corr(self,id):
        self._Corretores_dao.deletar_corr(id)
        return redirect('/')
