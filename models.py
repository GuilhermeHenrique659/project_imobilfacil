class Cidade:
    def __init__(self, cidade_nome, id_cidade = None):
        self._id_cidade = id_cidade
        self._cidade_nome = cidade_nome

class Bairro:
    def __init__(self, bairro_nome, id_cid, id_bairro = None, bairro_cidade_nome=None):
        self._id_bairro = id_bairro
        self._bairro_nome = bairro_nome
        self._id_cid = id_cid
        self._bairro_cid_nome = bairro_cidade_nome

class Tipo:
    def __init__(self,tipo_nome,id_tipo = None):
        self._id_tipo = id_tipo
        self._tipo_nome = tipo_nome

class Imovel:
    def __init__(self, tipo, finalidade, cidade, bairro, endereco,area, descricao, valor_imovel, status, porcentagem,
                 proprietario=None, corretor=None, valor_venda=None,honorarios=None, banheiro=None, quartos=None, garagem=None, imob_id=None):
        self._imob_id = imob_id
        self._tipo = tipo
        self._finalidade = finalidade
        self._cidade = cidade
        self._bairro = bairro
        self._endereco = endereco
        self._area = area
        self._descricao = descricao
        self._valor_imovel = valor_imovel
        self._valor_venda = valor_venda
        self._status = status
        self._porcentagem = porcentagem
        self._honorarios = honorarios
        self._proprietario = proprietario
        self._corretor = corretor
        self._banheiro = banheiro
        self._quartos = quartos
        self._garagem = garagem

    def set_area(self):
        self._area = self._area.replace('m','')
        return float(self._area)
    def set_id(self,id):
        self._imob_id = id

    @property
    def area(self):
        return int(self._area)

    def set_percentagem(self):
        self._porcentagem = self._porcentagem.replace('%','')
        return float(self._porcentagem)

    def set_valor_imovel(self):
        self._valor_imovel = self._valor_imovel.replace('.','')
        return float(self._valor_imovel)

    @property
    def valor_imovel(self):
        return int(self._valor_imovel)

    def set_honorarios(self):
        self._honorarios = (self.set_percentagem() * self.set_valor_imovel())/100
        return float(self._honorarios)
    @property
    def honorarios(self):
        return float(self._honorarios)

    def set_valor_venda(self):
        self._valor_venda = (self.valor_imovel + ((self.set_percentagem() * self.valor_imovel)/100))
        return float(self._valor_venda)

class Proprietario:
    def __init__(self, nome, cpf, rg, endereco, telefone, email, cidade=None, bairro=None, id = None ):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._endereco_prop = endereco
        self._telefone = telefone
        self._email = email
        self._cidade = cidade
        self._bairro = bairro

    def set_bairro(self,bairro):
        self._bairro = bairro

    def set_cidade(self,cidade):
        self._cidade = cidade

    def valida(self, data):
        if data == "" or data == "None":
            data = None
        return data

class Corretores:
    def __init__(self, usuario, email, nome, creci, celular, cpf, endereco, senha, cidade=None, bairro=None, id_corr=None):
        self._id_corr = id_corr
        self._usuario = usuario
        self._email = email
        self._nome = nome
        self._creci = creci
        self._celular = celular
        self._cpf = cpf
        self._endereco = endereco
        self._senha = senha
        self._cidade = cidade
        self._bairro = bairro
        self._senha = senha

    def set_bairro(self,bairro):
        self._bairro = bairro

    def set_cidade(self,cidade):
        self._cidade = cidade

    def set_user(self,user):
        self._usuario = user

    def valida(self,data):
        if data == "" or data == "None":
            data = None
        return data

class Financeiro:
    def __init__(self, honorarios_corr, porcentagem_corr, honorarios_imob , porcentagem_imob,
                 honorarios_total=None,valor_total=None, imob=None,corr=None, id_fin=None):
        self._honorarios_corr = honorarios_corr
        self._porcentagem_corr = porcentagem_corr
        self._honorarios_imob = honorarios_imob
        self._porcentagem_imob = porcentagem_imob
        self._imob = imob
        self._corr = corr
        self._id_fin = id_fin
        self._valor_total = valor_total
        self._honorarios_total = honorarios_total

    @property
    def honorarios_total(self):
        return float(self._honorarios_total)

    @property
    def valor_total(self):
        return float(self._valor_total)

    def get_honorarios_corr(self):
        return float(self._honorarios_corr)

    def get_honorarios_imob(self):
        return float(self._honorarios_imob)


