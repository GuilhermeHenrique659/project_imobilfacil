from controllers.controller import *
from models import Proprietario

class ProprietarioController(Controller):
    def __init__(self,Imovel_Dao, Proprietario_dao, Corretores_dao, CidadeDao, BairroDao):
        super().__init__(Imovel_Dao, Proprietario_dao, Corretores_dao, CidadeDao, BairroDao)

    def rota_proprietario(self):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=novo_proprietario.html')
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        return render_template('novo_proprietario.html', cidades=lista_cidades, bairros=lista_bairro)

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
        self._Proprietario_dao.salvar(proprietario)
        return redirect('/')

    def editar_proprietario(self,id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=''')
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        proprietario = self._Proprietario_dao.busca_por_id(id)
        return render_template('editar_prop.html', proprietario=proprietario, cidades=lista_cidades,
                               bairros=lista_bairro)

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
        self._Proprietario_dao.salvar(proprietario)
        return redirect('/')


    def deletar_prop(self,id):
        self._Proprietario_dao.deletar_prop(id)
        return redirect('/')
