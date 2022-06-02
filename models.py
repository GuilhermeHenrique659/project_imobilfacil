class Cidade:
    def __init__(self, cidade_nome, uf, id_cidade = None):
        self._id_cidade = id_cidade
        self._cidade_nome = cidade_nome
        self._uf = uf

class Bairro:
    def __init__(self, bairro_nome, id_cid, id_bairro = None, bairro_cidade_nome=None):
        self._id_bairro = id_bairro
        self._bairro_nome = bairro_nome
        self._id_cid = id_cid
        self._bairro_cid_nome = bairro_cidade_nome

class Descricao_imovel:
    def __init__(self, vagas, banheiro, suite, dormitorio, area_serve=None, copa=None, lareira=None,edicula=None,
                portao_elec=None,hidromsg=None, piso=None, sacada=None, sala_vist=None, sala_estar=None, sotao=None,
                amarinho=None,cozinha=None,escritorio=None, lavabo=None,sala_jantar=None,varanda=None, clarabioa=None,
                dep_empregada=None, garage=None, living_room=None,quintal=None,sala_tv=None,w_c_empregada=None,closet=None,
                depensa=None, churrasqueira=None, portaria_24h=None, salao_festa=None,jd_inverno=None,quadra=None, sauna=None,
                piscina=None, entrada_ind=None, quadra_tenis=None, playground=None, salao_ginastica=None, id_imob = None, id_desc = None) -> None:
        self._id_desc = id_desc
        self._id_imob = id_imob
        self._vagas = vagas
        self._banheiro = banheiro
        self._suite = suite
        self._dormitorio = dormitorio
        self._area_serve = area_serve
        self._copa =copa
        self._lareira = lareira
        self._edicula = edicula
        self._portao_elec= portao_elec
        self._hidromsg = hidromsg
        self._piso = piso
        self._sacada = sacada
        self._sala_vist = sala_vist
        self._sala_estar = sala_estar
        self._sotao = sotao
        self._amarinho = amarinho
        self._cozinha = cozinha
        self._escritorio = escritorio
        self._lavabo =lavabo
        self._sala_jantar = sala_jantar
        self._varanda = varanda
        self._claraboia = clarabioa
        self._dep_empregada = dep_empregada
        self._garage = garage
        self._living_room = living_room
        self._quintal = quintal
        self._sala_tv = sala_tv
        self._w_c_empregada = w_c_empregada
        self._closet = closet
        self._despensa = depensa
        self._churrasqueira = churrasqueira
        self._portaria_24h = portaria_24h
        self._salao_festa = salao_festa
        self._jd_inverno = jd_inverno
        self._quadra = quadra
        self._sauna = sauna
        self._pescina = piscina
        self._entrada_ind = entrada_ind
        self._quadra_tenis = quadra_tenis
        self._playground = playground
        self._sala_ginastica = salao_ginastica
    
class Imovel:
    def __init__(self, categoria=None,forma=None, ladoesq=None,ladodir=None, frente=None,fundo=None, 
                m_total=None, topografia=None, area_util=None, area_contruida=None,edicula=None, cidade=None, 
                bairro=None, endereco=None, numero=None, cep=None, valor_imovel=None,
                taxa=None, valor_venda=None, repasse=None,  placa=None, url=None, data_placa=None,data_visita=None, 
                data_ultvis=None, codigo=None, info_anun=None,info_area=None,info_end=None, proprietario=None, 
                corretor=None, imob_id=None, tipo=None, subtipo=None, desc=None):
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
        self._desc = desc

    def get_taxa(self):
        return float(self._taxa.replace('%',''))

    def get_valor_imovel(self):
        return float(self._valor_imovel.replace('.',''))

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