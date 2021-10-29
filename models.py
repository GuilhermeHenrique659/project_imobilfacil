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

class imovel:
    def __init__(self, tipo, finalidade, cidade, bairro, endereco,area, descricao, valor_imovel, status, porcentagem,
                 proprietario_id=None, corretor_id=None, valor_venda=None,honorarios=None, banheiro=None, quartos=None, garagem=None, imob_id=None):
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
        self._proprietario_id = proprietario_id
        self._corretor_id = corretor_id
        self._banheiro = banheiro
        self._quartos = quartos
        self._garagem = garagem

    def set_area(self):
        self._area = self._area.replace('m','')
        return float(self._area)

    def get_area(self):
        return int(self._area)

    def set_percentagem(self):
        self._porcentagem = self._porcentagem.replace('%','')
        return float(self._porcentagem)

    def set_valor_imovel(self):
        self._valor_imovel = self._valor_imovel.replace('.','')
        return float(self._valor_imovel)

    def get_valor_imovel(self):
        return int(self._valor_imovel)

    def set_honorarios(self):
        self._honorarios = (self.set_percentagem() * self.set_valor_imovel())/100
        return float(self._honorarios)

    def set_valor_venda(self):
        self._valor_venda = (self.get_valor_imovel() + ((self.set_percentagem() * self.get_valor_imovel())/100))
        return float(self._valor_venda)

class Proprietario:
    def __init__(self, nome, cpf, rg, endereco, telefone, email, id = None ):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._endereco_prop = endereco
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
        self._endereco = endereco
        self._senha = senha

#classe para receber inner join da tabela imovel e proprietario do banco de dados
class Imob_Prop(imovel,Proprietario,Tipo,Cidade,Bairro):
    def __init__(self, imob_id, corretor_id, proprietario_id, tipo, finalidade, cidade, bairro,
                 endereco,area, descricao, valor_imovel,valor_venda, status, porcentagem, honorarios, banheiro, quartos, garagem,
                 id, nome, cpf, rg, endereco_prop, telefone, email, tipo_id, tipo_nome,id_cidade,cidade_nome,id_bairro,bairro_nome,cidade_bairro_id):
        imovel.__init__(self, tipo, finalidade, cidade, bairro, endereco,area, descricao, valor_imovel, status,porcentagem,
                    proprietario_id, corretor_id, valor_venda, honorarios, banheiro, quartos, garagem, imob_id=imob_id)
        Proprietario.__init__(self,nome, cpf, rg, endereco_prop, telefone, email,id)
        Tipo.__init__(self,tipo_nome,tipo_id)
        Cidade.__init__(self,cidade_nome,id_cidade)
        Bairro.__init__(self,bairro_nome,cidade_bairro_id,id_bairro)