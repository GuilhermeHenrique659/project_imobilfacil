from controllers.controller import *
from models import Tipo,Cidade,Bairro

class OthersController:
    def __init__(self,TiposDao,CidadeDao,BairroDao):
        self._TiposDao = TiposDao
        self._CidadeDao = CidadeDao
        self._BairroDao = BairroDao

    def novo_tipo(self):
        Tipo_nome = request.form['tipo']
        previous = request.form['previous']
        tipo = Tipo(Tipo_nome)
        self._TiposDao.salvar(tipo)
        return redirect(previous)

    def nova_cidade(self):
        cidade_nome = request.form['cidade']
        cidade = Cidade(cidade_nome)
        previous = request.form['previous']
        self._CidadeDao.salvar(cidade)
        return redirect(previous)

    def novo_bairro(self):
        cidade = request.form['cidade_bairro']
        bairro_nome = request.form['bairro']
        bairro = Bairro(bairro_nome, cidade)
        previous = request.form['previous']
        self._BairroDao.salvar(bairro)
        return redirect(previous)


