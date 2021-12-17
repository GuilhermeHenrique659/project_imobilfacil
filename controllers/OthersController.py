from controllers.controller import *
from models import Tipo,Cidade,Bairro

class OthersController:
    def __init__(self,TiposDao,CidadeDao,BairroDao):
        self._TiposDao = TiposDao
        self._CidadeDao = CidadeDao
        self._BairroDao = BairroDao

    def novo_tipo(self):
        Tipo_nome = request.form['tipo']
        tipo = Tipo(Tipo_nome)
        self._TiposDao.salvar(tipo)
        return redirect('/novo_imovel')

    def nova_cidade(self):
        cidade_nome = request.form['cidade']
        cidade = Cidade(cidade_nome)
        self._CidadeDao.salvar(cidade)
        return redirect('/novo_imovel')

    def novo_bairro(self):
        cidade = request.form['cidade_bairro']
        bairro_nome = request.form['bairro']
        bairro = Bairro(bairro_nome, cidade)
        self._BairroDao.salvar(bairro)
        return redirect('/novo_imovel')
