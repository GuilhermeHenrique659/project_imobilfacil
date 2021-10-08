
class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

    def get_senha(self):
        return self._senha

class imovel:
    def  __init__(self, sigla, tipo, finalidade, bairro, quadra, lote, valor, status, porcentagem, honorarios, proprietario_id, id=None):
        self._id = id
        self._sigla = sigla
        self._tipo= tipo
        self._finalidade = finalidade
        self._bairro = bairro
        self._quadra = quadra
        self._lote = lote
        self._valor = valor
        self._satus = status
        self._porcentagem = porcentagem
        self._honorarios = honorarios
        self._proprietario_id = proprietario_id