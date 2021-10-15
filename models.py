
class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

    def get_senha(self):
        return self._senha

class imovel:
    def __init__(self, sigla, tipo, finalidade, bairro, quadra, lote,area, descricao, valor_imovel, status, porcentagem, proprietario_id=None, corretor_id=None, imob_id=None, valor_venda=None,honorarios =None):
        self._id = imob_id
        self._sigla = sigla
        self._tipo= tipo
        self._finalidade = finalidade
        self._bairro = bairro
        self._quadra = quadra
        self._lote = lote
        self._area = area
        self._descricao = descricao
        self._valor_imovel = valor_imovel
        self._valor_venda = valor_venda
        self._status = status
        self._porcentagem = porcentagem
        self._honorarios = honorarios
        self._proprietario_id = proprietario_id
        self._corretor_id = corretor_id

        #banheiro
        #quarto
        #garagem

    def get_honorarios(self):
        self._honorarios = self._porcentagem
        return self._honorarios

    def get_imovel_venda(self):
        self._valor_venda = self._valor_imovel
        return self._valor_venda

class Proprietario:
    def __init__(self, nome, cpf, rg, endereco, telefone, email, id = None ):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._telefone = telefone
        self._email = email

class Corretores:
    def __init__(self, usuario, email, nome, imobil, creci, celular, cpf, endereco, senha, id_corr=None):
        self._id_corr = id_corr
        self._usuario = usuario
        self._email = email
        self._nome = nome
        self._imobil = imobil
        self._creci = creci
        self._celular = celular
        self._cpf = cpf
        self._endereco =endereco
        self._senha = senha

