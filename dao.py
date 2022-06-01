import MySQLdb
from flask_mysqldb import MySQL
from models import (Bairro, Cidade, Corretores, Imovel,
                    Proprietario, Descricao_imovel)
from SQL import *



#proprietarios
class ProprietarioDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, proprietario):
        cursor = self.__db.connection.cursor()
        try:
            if (proprietario._id):
                cursor.execute(SQL_ATUALIZA_PROPRIETARIO, (proprietario._nome,proprietario._rg_insc_estadual, proprietario._cpf_cnpj, proprietario._sexo,proprietario._endereco_prop,proprietario._cep,
                                                     proprietario._end_numero, proprietario._tipo_pessoa, proprietario._razao,proprietario._telefone,
                                                     proprietario._celular, proprietario._whatsapp, proprietario._email, proprietario._capital, proprietario._patrimonio,
                                                     proprietario._atividade, proprietario._cidade,proprietario._bairro,proprietario._id,))
            else:
                cursor.execute(SQL_CRIA_PROPRIETARIO, (proprietario._nome,proprietario._rg_insc_estadual, proprietario._cpf_cnpj, proprietario._sexo,proprietario._endereco_prop,proprietario._cep,
                                                     proprietario._end_numero, proprietario._tipo_pessoa, proprietario._razao,proprietario._telefone,
                                                     proprietario._celular, proprietario._whatsapp, proprietario._email, proprietario._capital, proprietario._patrimonio,
                                                     proprietario._atividade, proprietario._cidade,proprietario._bairro))
        except MySQLdb.IntegrityError as error:
            return error
        self.__db.connection.commit()
        del proprietario
        return None

    def find_by_name(self,prop_name):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FIND_PROP_BY_NAME,(prop_name,))
        return self.traduz_para_lista(cursor.fetchall())

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCAR_LISTA_PROP)
        proprietarios = self.traduz_para_lista(cursor.fetchall())
        return proprietarios

    # busca um unico proprietario pelo id
    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PROP_POR_ID, (id,))
        prop_dict = cursor.fetchone()
        cidade = Cidade(prop_dict['CIDADE'], prop_dict['ID_CIDADE'])
        bairro = Bairro(prop_dict['BAIRRO'],prop_dict['CIDADE_ID_CID'],prop_dict['BAIRRO.ID_BAIRRO'],prop_dict['CIDADE'])
        proprietario = Proprietario(prop_dict['NOME'], prop_dict['CPF_CNPJ'], prop_dict['RG_INSC_ETAD'], prop_dict['ENDERECO'],
                                    prop_dict['NUMERO'],prop_dict['CEP'],prop_dict['CELULAR'],prop_dict['EMAIL'],cidade=cidade,bairro=bairro,
                                    id=prop_dict['ID_PROP'],atividade=prop_dict['ATIVIDADE'],telefone=prop_dict['TELEFONE'],
                                    razao=prop_dict['RAZAO'], capital=prop_dict['CAPITAL'],patrimonio=prop_dict['PATRIMONIO'],
                                    whatsapp=prop_dict['WHATAPPS'],data_cad=prop_dict['DATA_CAD'],tipo_pessoa=prop_dict['PESSOA'],
                                    sexo=prop_dict['SEXO'])
        del cidade,bairro
        return proprietario

    def deletar_prop(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_PROPRIETARIO, (id,))
        self.__db.connection.commit()


    def traduz_para_lista(self,prop_dictlist):
        def traduz_para_objeto(prop_dict):
            return Proprietario(prop_dict['NOME'], prop_dict['CPF_CNPJ'], prop_dict['RG_INSC_ETAD'], prop_dict['ENDERECO'], None, None, None,prop_dict['EMAIL'], telefone= prop_dict['TELEFONE'],cidade = prop_dict['ID_CIDADE'], bairro = prop_dict['ID_BAIRRO'],id = prop_dict['ID_PROP'])
        return list(map(traduz_para_objeto, prop_dictlist))

#corretor/
class CorretorDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, corretor):
        cursor = self.__db.connection.cursor()
        try:
            if (corretor._id_corr):
                cursor.execute(SQL_ATUALIZA_CORRETORES, (corretor._usuario,corretor._email,corretor._nome,corretor._creci,corretor._celular,corretor._cpf,
                                                     corretor._endereco,corretor._senha,corretor._cidade,corretor._bairro,corretor._id_corr))
            else:
                cursor.execute(SQL_CRIA_CORRETORES, (corretor._usuario,corretor._email,corretor._nome,corretor._creci,
                                                 corretor._celular,corretor._cpf,corretor._endereco,corretor._senha,corretor._cidade,corretor._bairro))
        except MySQLdb.IntegrityError as error:
            return error
        print(cursor.lastrowid)
        self.__db.connection.commit()
        return cursor.lastrowid

    def find_by_name(self, name):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FIND_CORR_BY_NAME,(name,))
        return self.traduz_para_lista_corr(cursor.fetchall())
    

    # faz lista de corretores para mostrar no index
    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LISTA_CORRETORES)
        corretores = self.traduz_para_lista_corr(cursor.fetchall())
        return corretores

    # busca um unico corretor pelo usuario no login
    def buscar_por_id(self,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CORR_ID, (usuario,usuario,))
        corr_dict = cursor.fetchone()
        usuario = self.traduz_para_obejto(corr_dict) if corr_dict else None
        return usuario

    # busca um unico corretor pelo id
    def busca_por_id_edit(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CORR_POR_ID, (id,))
        corr_dict = cursor.fetchone()
        cidade = Cidade(corr_dict['CIDADE'], corr_dict['ID_CIDADE'])
        bairro = Bairro(corr_dict['BAIRRO'],corr_dict['CIDADE_ID_CID'],corr_dict['BAIRRO.ID_BAIRRO'],corr_dict['CIDADE'])
        corretor = Corretores(corr_dict['USUARIO'], corr_dict['EMAIL'], corr_dict['NOME'], corr_dict['CRECI'], corr_dict['CELULAR'],
                              corr_dict['CPF'], corr_dict['ENDERECO'], corr_dict['SENHA'],cidade,bairro,corr_dict['ID_CORR'])
        del cidade,bairro
        return corretor

    def deletar_corr(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_CORRETOR, (id,))
        self.__db.connection.commit()

#cria objeto usuario
    def traduz_para_obejto(self,tupla):
        return Corretores(tupla['USUARIO'],tupla['EMAIL'],tupla['NOME'],tupla['CRECI'],tupla['CELULAR'],
                      tupla['CPF'],tupla['ENDERECO'],tupla['SENHA'],tupla['ID_CIDADE'],tupla['ID_BAIRRO'], tupla['ID_CORR'])

#tranforma dodos do bd em uma lista de objetos
    def traduz_para_lista_corr(self,corr_dictlist):
        def traduz_para_objeto(corr_dict):
            return Corretores(corr_dict['USUARIO'],corr_dict['EMAIL'],corr_dict['NOME'],corr_dict['CRECI'],corr_dict['CELULAR'],
                      corr_dict['CPF'],corr_dict['ENDERECO'],corr_dict['SENHA'],corr_dict['ID_CIDADE'],corr_dict['ID_BAIRRO'], corr_dict['ID_CORR'])
        lista_corr = list(map(traduz_para_objeto, corr_dictlist))
        return lista_corr

#imovel/
class imovelDao:
    def __init__(self, db:MySQL):
        self.__db = db

    def salvar_desc(self, desc:Descricao_imovel):
        cursor = self.__db.connection.cursor()
        if desc._id_desc:
            cursor.execute(SQL_ATUALIZA_DESC, (desc._vagas,desc._banheiro,desc._suite,desc._dormitorio,desc._area_serve,desc._copa,desc._edicula,desc._lareira,desc._portao_elec,
                                                desc._hidromsg,desc._piso,desc._sacada,desc._sala_vist,desc._sala_estar,desc._sotao,desc._amarinho,desc._cozinha,desc._escritorio,desc._lavabo,desc._sala_jantar,
                                                desc._varanda,desc._claraboia,desc._dep_empregada,desc._garage,desc._living_room,desc._quintal,desc._sala_tv,desc._w_c_empregada,
                                                desc._closet,desc._despensa,desc._churrasqueira,desc._portaria_24h,desc._salao_festa,desc._jd_inverno,
                                                desc._quadra,desc._sauna,desc._pescina,desc._entrada_ind,desc._quadra_tenis,desc._playground,desc._sala_ginastica,desc._id_desc,))
        else:
            cursor.execute(SQL_CRIA_IMOVEL_DESC, (desc._id_imob,desc._vagas,desc._banheiro,desc._suite,desc._dormitorio,desc._area_serve,desc._copa,desc._edicula,desc._lareira,desc._portao_elec,
                                                desc._hidromsg,desc._piso,desc._sacada,desc._sala_vist,desc._sala_estar,desc._sotao,desc._amarinho,desc._cozinha,desc._escritorio,desc._lavabo,desc._sala_jantar,
                                                desc._varanda,desc._claraboia,desc._dep_empregada,desc._garage,desc._living_room,desc._quintal,desc._sala_tv,desc._w_c_empregada,
                                                desc._closet,desc._despensa,desc._churrasqueira,desc._portaria_24h,desc._salao_festa,desc._jd_inverno,
                                                desc._quadra,desc._sauna,desc._pescina,desc._entrada_ind,desc._quadra_tenis,desc._playground,desc._sala_ginastica,))
        self.__db.connection.commit()
        del desc
        return cursor.lastrowid

    def salvar(self, imovel:Imovel):
        cursor = self.__db.connection.cursor()
        try:
            if (imovel._imob_id):
                cursor.execute(SQL_ATUALIZA_IMOVEIS, (imovel._corretor,imovel._proprietario,imovel._cidade, imovel._bairro, imovel._categoria,
                                            imovel._forma,imovel._ladodir,imovel._ladoesq,imovel._frente, imovel._fundo,imovel._m_total, imovel._topografia,
                                            imovel._area_util,imovel._area_contruida,imovel._edicula,imovel._info_area,imovel._tipo,imovel._subtipo,
                                            imovel._endereco, imovel._numero,imovel._cep, imovel._info_end, imovel._placa,imovel._data_placa, imovel._data_visita,
                                            imovel._data_ultvis,imovel._url,imovel._codigo,imovel._info_anun,imovel.get_valor_imovel(),imovel._valor_venda, 
                                            imovel.get_taxa(), imovel._repasse,imovel._imob_id))
            else:
                cursor.execute(SQL_CRIA_IMOVEL,(imovel._corretor,imovel._proprietario,imovel._cidade, imovel._bairro, imovel._categoria,
                                            imovel._forma,imovel._ladodir,imovel._ladoesq,imovel._frente, imovel._fundo,imovel._m_total, imovel._topografia,
                                            imovel._area_util,imovel._area_contruida,imovel._edicula,imovel._info_area,imovel._tipo,imovel._subtipo,
                                            imovel._endereco, imovel._numero,imovel._cep, imovel._info_end, imovel._placa,imovel._data_placa, imovel._data_visita,
                                            imovel._data_ultvis,imovel._url,imovel._codigo,imovel._info_anun,imovel.get_valor_imovel(),imovel._valor_venda, 
                                            imovel.get_taxa(), imovel._repasse))
        except MySQLdb.IntegrityError as error:
            return error
        self.__db.connection.commit()
        del imovel
        return cursor.lastrowid

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LISTA_IMOB)
        imoveis = self.traduz_para_lista_imob(cursor.fetchall())
        return imoveis

    def busca_imob_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_IMOB_ID, (id,))
        imob_dict = cursor.fetchone()
        cidade = Cidade(imob_dict['CIDADE'], imob_dict['ID_CID'])

        bairro = Bairro(imob_dict['BAIRRO'], imob_dict['CIDADE_ID_CID'], imob_dict['BAIRRO.ID_BAIRRO'], imob_dict['CIDADE'])

        corretor = Corretores(imob_dict['USUARIO'],imob_dict['EMAIL'],imob_dict['CORRETORES.NOME'],imob_dict['CRECI'],imob_dict['CELULAR'],
                      imob_dict['CPF'],imob_dict['ENDERECO'],imob_dict['SENHA'],imob_dict['ID_CIDADE'],imob_dict['ID_BAIRRO'], imob_dict['ID_CORR'])

        proprietario = Proprietario(imob_dict['NOME'], imob_dict['CPF_CNPJ'], imob_dict['RG_INSC_ETAD'], imob_dict['ENDERECO'], imob_dict['TELEFONE'],
                                    imob_dict['EMAIL'], imob_dict['CIDADE'],imob_dict['BAIRRO'],id=imob_dict['ID_PROP'])
        
        
        descricao = Descricao_imovel( imob_dict['VAGAS'] ,imob_dict['BANHEIRO'] ,imob_dict['SUITE'] ,imob_dict['DORMITORIOS'] ,imob_dict['AREA_SERVICO'] ,imob_dict['COPA'] ,
                        imob_dict['LAREIRA'] ,imob_dict['EDICULA'] ,imob_dict['PORTAO_ELEC'] ,imob_dict['HIDROMSG'] ,
                        imob_dict['PISO'] ,imob_dict['SACADA'] ,imob_dict['SALA_VIST'] ,imob_dict['SALA_ESTAR'] ,imob_dict['SOTAO'] ,imob_dict['AMARINHO'] ,
                        imob_dict['COZINHA'] ,imob_dict['ESCRITORIO'] ,imob_dict['LAVABO'] ,imob_dict['SALA_JANTAR'] ,imob_dict['VARANDA'] ,
                        imob_dict['CLARABOIA'] ,imob_dict['DEP_EMPREGADA'] ,imob_dict['GARAGE'] ,imob_dict['LIVING_ROOM'] ,imob_dict['QUINTAL'] ,
                        imob_dict['SALA_TV'] ,imob_dict['W_C_EMPREGADA'] ,imob_dict['CLOSET'] ,imob_dict['DESPENSA'] ,imob_dict['CHURRASQUEIRA'] ,
                        imob_dict['PORTARIA_24H'] ,imob_dict['SALAO_FESTA'] ,imob_dict['JD_INVERNO'] ,imob_dict['QUADRA'] ,imob_dict['SAUNA'],
                        imob_dict['PISCINA'] ,imob_dict['ENTRADA_INDEP'] ,imob_dict['QUADRA_TENIS'] ,imob_dict['PLAYGROUND'] ,imob_dict['SALA_GINASTICA'],id_desc=imob_dict['ID_DESC'])

        imovel = Imovel(imob_dict['CATEGORIA'],imob_dict['FORMA'],imob_dict['LADO_ESQ'],imob_dict['LADO_DIR'],imob_dict['LADO_FRE'],imob_dict['LADO_FUN'],
                        imob_dict['TOTAL'],imob_dict['TOPOGRAFIA'],imob_dict['AREA_UTIL'],imob_dict['CONSTRUIDA'],imob_dict['EDICULA'],cidade,bairro,
                        imob_dict['ENDERECO_IMOVEL'],imob_dict['NUMERO'],imob_dict['CEP'],imob_dict['VALOR_IMOVEL'],imob_dict['CORRETAGEM'],imob_dict['VALOR_VENDA'],
                        imob_dict['REPASSE_IMOB'],imob_dict['PLACA'],imob_dict['URL'],imob_dict['DATA_PLACA'],imob_dict['DATA_VISITA'],imob_dict['DATA_ULTIMA_VIS'],imob_dict['COD_ANUNCIO'],
                        imob_dict['ANUNCIO_INFO'],imob_dict['END_INFO'],imob_dict['AREA_INFO'],proprietario,corretor,imob_dict['ID_IMOB'], imob_dict['TIPO'], imob_dict['SUBTIPO'],desc=descricao)
        del cidade, bairro, proprietario, corretor
        return imovel


    def filtra(self, id, filtro):
        filtros_dic = {
            "filtra_cidade" : SQL_FILTRA_CIDADE,
            "filtra_prop" : SQL_FILTRA_PROP,
            "bairros": SQL_FILTRO_BAIRRO
        }
        cursor = self.__db.connection.cursor()
        cursor.execute(filtros_dic[filtro], (id,))
        imoveis = self.traduz_para_lista_imob(cursor.fetchall())
        return imoveis

    def deletar_imob(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_IMOVEL, (id,))
        self.__db.connection.commit()

    def traduz_para_lista_imob(self,imob_dictlist):
        def traduz_para_objct_imob(imob_dict):
            proprietario = Proprietario(imob_dict['NOME'],celular=imob_dict['CELULAR'])
            return Imovel(endereco=imob_dict['ENDERECO_IMOVEL'],cidade=imob_dict['CIDADE'], 
                            bairro=imob_dict['BAIRRO'],categoria=imob_dict['CATEGORIA'],
                             proprietario=proprietario, imob_id=imob_dict['ID_IMOB'])
        return list(map(traduz_para_objct_imob, imob_dictlist))


class ciadadeDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cidade:Cidade):
        cursor = self.__db.connection.cursor()
        try:
            cursor.execute(SQL_CRIA_CIDADE,(cidade._id_cidade,cidade._cidade_nome, cidade._uf))
        except MySQLdb.IntegrityError as error:
            raise Exception(error.args[1])
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        del cidade

    def lista(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_CIDADE)
        cidades = self.traduz_para_lista_cidade(cursor.fetchall())
        return cidades

    def traduz_para_lista_cidade(self, cidade_dictlist):
        def traduz_para_objct_cidade(cidade_dict):
                return Cidade(cidade_dict['CIDADE'],cidade_dict['UF'],cidade_dict['ID_CID'])
        return list(map(traduz_para_objct_cidade, cidade_dictlist))

class bairroDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, bairro:Bairro):
        cursor = self.__db.connection.cursor()
        try:
            cursor.execute(SQL_CRIA_BAIRRO,(bairro._id_bairro,bairro._bairro_nome,bairro._id_cid))
        except MySQLdb.IntegrityError as error:
            print(error)
            raise Exception(error.args[1])
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        del bairro

    def lista(self, bairro_nome, id_cid):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_BAIRRO,(bairro_nome,id_cid,))
        bairros = self.traduz_para_lista_bairros(cursor.fetchall())
        return bairros

    def traduz_para_lista_bairros(self, bairro_dictlist):
        def traduz_para_objct_bairro(bairro_dict):
            return Bairro(bairro_dict['BAIRRO'],bairro_dict['CIDADE_ID_CID'], bairro_dict['ID_BAIRRO'])
        return list(map(traduz_para_objct_bairro, bairro_dictlist))
