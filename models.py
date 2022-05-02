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
    def __init__(self, categoria=None,forma=None, ladoesq=None,ladodir=None, frente=None,fundo=None, 
                m_total=None, topografia=None, area_util=None, area_contruida=None,edicula=None, cidade=None, 
                bairro=None, endereco=None, numero=None, cep=None, valor_imovel=None,
                taxa=None, valor_venda=None, repasse=None,  placa=None, url=None, data_placa=None,data_visita=None, 
                data_ultvis=None, codigo=None, info_anun=None,info_area=None,info_end=None, proprietario=None, 
                corretor=None, imob_id=None, tipo=None, subtipo=None):
        self._imob_id = imob_id
        self._categoria = categoria
        self._tipo =tipo
        self._subtipo = subtipo
        self._forma = forma
        self._ladoesq = ladoesq
        self._ladodir = ladodir
        self._frente = frente
        self._fundo = fundo
        self._info_area = info_area
        self._m_total = m_total
        self._topografia = topografia
        self._area_util = area_util
        self._area_contruida = area_contruida
        self._edicula = edicula
        self._numero = numero
        self._cep = cep
        self._placa = placa
        self._info_end = info_end
        self._codigo = codigo
        self._url = url
        self._data_placa = data_placa
        self._data_visita = data_visita
        self._data_ultvis = data_ultvis
        self._info_anun = info_anun
        self._taxa = taxa
        self._repasse = repasse
        self._cidade = cidade
        self._bairro = bairro
        self._endereco = endereco
        self._valor_imovel = valor_imovel
        self._valor_venda = valor_venda
        self._proprietario = proprietario
        self._corretor = corretor

class Proprietario:
    def __init__(self, nome=None, cpf_cnpj=None, rg_insc_estadual=None, endereco=None, numero=None, cep=None,
                celular=None, email=None, cidade=None, bairro=None, id = None, atividade = None,
                telefone = None, razao = None, capital = None, patrimonio = None, 
                whatsapp = None, data_cad = None, tipo_pessoa = None, codigo = None, sexo = None):
        self._id = id
        self._nome = nome
        self._cpf_cnpj = cpf_cnpj
        self._rg_insc_estadual = rg_insc_estadual
        self._sexo = sexo
        self._endereco_prop = endereco
        self._end_numero = numero
        self._cep = cep
        self._celular = celular
        self._email = email
        self._atividade = atividade
        self._whatsapp = whatsapp
        self._telefone = telefone
        self._razao = razao
        self._capital = capital
        self._patrimonio = patrimonio
        self._data_cad = data_cad
        self._cidade = cidade
        self._bairro = bairro
        self._codigo = codigo
        self._tipo_pessoa = tipo_pessoa

    def set_bairro(self,bairro):
        self._bairro = bairro

    def set_cidade(self,cidade):
        self._cidade = cidade


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

    def set_email(self,email):
        self._email = email

    def set_bairro(self,bairro):
        self._bairro = bairro

    def set_cidade(self,cidade):
        self._cidade = cidade

    def set_user(self,user):
        self._usuario = user


class Financeiro:
    def __init__(self, honorarios_corr, porcentagem_corr, honorarios_imob , porcentagem_imob,
                 honorarios_total=None,valor_total=None, imob=None,corr=None,corr_id=None, id_fin=None):
        self._honorarios_corr = honorarios_corr
        self._porcentagem_corr = porcentagem_corr
        self._honorarios_imob = honorarios_imob
        self._porcentagem_imob = porcentagem_imob
        self._imob = imob
        self._corr = corr
        self._corr_id = corr_id
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

    def get_porcetagem_corr(self):
        return float(self._porcentagem_corr/100)

    def get_porcetagem_imob(self):
        return float(self._porcentagem_imob/100)


