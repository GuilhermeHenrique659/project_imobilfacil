import MySQLdb

from models import (Bairro, Cidade, Corretores, Financeiro, Imovel,
                    Proprietario, Tipo)
from SQL import *

MYSQL_CODE_ERROR = 0

#proprietarios
class ProprietarioDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, proprietario):
        cursor = self.__db.connection.cursor()
        try:
            if (proprietario._id):
                cursor.execute(SQL_ATUALIZA_PROPRIETARIO, (proprietario._nome, proprietario._cpf_cnpj,proprietario._rg_insc_estadual, proprietario._endereco_prop, proprietario._telefone,
                                                       proprietario._email,proprietario._cidade,proprietario._bairro, proprietario._id))
            else:
                cursor.execute(SQL_CRIA_PROPRIETARIO, (proprietario._nome,proprietario._rg_insc_estadual, proprietario._cpf_cnpj, proprietario._sexo,proprietario._endereco_prop,proprietario._cep,
                                                     proprietario._end_numero, proprietario._tipo_pessoa, proprietario._codigo, proprietario._razao,proprietario._telefone,
                                                     proprietario._celular, proprietario._whatsapp, proprietario._email, proprietario._capital, proprietario._patrimonio,
                                                     proprietario._atividade, proprietario._cidade,proprietario._bairro))
        except MySQLdb.IntegrityError as error:
            return error.args[MYSQL_CODE_ERROR]
        self.__db.connection.commit()
        del proprietario
        return cursor.lastrowid

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
        bairro = Bairro(prop_dict['BAIRRO'],prop_dict['CIDADE_ID_CID'],prop_dict['bairro.ID_BAIRRO'],prop_dict['CIDADE'])
        proprietario = Proprietario(prop_dict['NOME'], prop_dict['CPF'], prop_dict['RG/INSC_ETAD'], prop_dict['ENDERECO'],
                                    prop_dict['TELEFONE'], prop_dict['EMAIL'], cidade, bairro, prop_dict['ID_PROP'])
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
            return error.args[MYSQL_CODE_ERROR]
        self.__db.connection.commit()
        del corretor
        return cursor.lastrowid

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
        bairro = Bairro(corr_dict['BAIRRO'],corr_dict['CIDADE_ID_CID'],corr_dict['bairro.ID_BAIRRO'],corr_dict['CIDADE'])
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
        ADMIN_USER = 0
        def traduz_para_objeto(corr_dict):
            return Corretores(corr_dict['USUARIO'],corr_dict['EMAIL'],corr_dict['NOME'],corr_dict['CRECI'],corr_dict['CELULAR'],
                      corr_dict['CPF'],corr_dict['ENDERECO'],corr_dict['SENHA'],corr_dict['ID_CIDADE'],corr_dict['ID_BAIRRO'], corr_dict['ID_CORR'])
        lista_corr = list(map(traduz_para_objeto, corr_dictlist))
        lista_corr.pop(ADMIN_USER)
        return lista_corr

#imovel/
class imovelDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, imovel):
        cursor = self.__db.connection.cursor()
        if (imovel._imob_id):
            cursor.execute(SQL_ATUALIZA_IMOVEIS, (imovel._corretor ,imovel._proprietario, imovel._tipo, imovel._finalidade,
                                            imovel._cidade, imovel._bairro,imovel._endereco, imovel.set_area(),
                                            imovel._descricao, imovel.set_valor_imovel(), imovel.set_valor_venda(), imovel._status,
                                            imovel.set_percentagem(), imovel.set_honorarios(), imovel._banheiro, imovel._quartos, imovel._garagem, imovel._imob_id))
        else:
            cursor.execute(SQL_CRIA_IMOVEL,( imovel._corretor ,imovel._proprietario, imovel._tipo, imovel._finalidade,
                                            imovel._cidade, imovel._bairro,imovel._endereco, imovel.set_area(),
                                            imovel._descricao, imovel.set_valor_imovel(), imovel.set_valor_venda(), imovel._status,
                                            imovel.set_percentagem(), imovel.set_honorarios(),imovel._banheiro,imovel._quartos,imovel._garagem))
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        del imovel
        return cursor._id

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LISTA_IMOB)
        imoveis = self.traduz_para_lista_imob(cursor.fetchall())
        return imoveis

    def busca_imob_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_IMOB_ID, (id,))
        imob_dict = cursor.fetchone()
        tipo = Tipo(imob_dict['TIPO'], imob_dict['ID_TIPO'])

        cidade = Cidade(imob_dict['CIDADE'], imob_dict['ID_CID'])

        bairro = Bairro(imob_dict['BAIRRO'], imob_dict['CIDADE_ID_CID'], imob_dict['bairro.ID_BAIRRO'], imob_dict['CIDADE'])

        corretor = Corretores(imob_dict['USUARIO'],imob_dict['EMAIL'],imob_dict['corretores.NOME'],imob_dict['CRECI'],imob_dict['CELULAR'],
                      imob_dict['CPF'],imob_dict['ENDERECO'],imob_dict['SENHA'],imob_dict['ID_CIDADE'],imob_dict['ID_BAIRRO'], imob_dict['ID_CORR'])

        proprietario = Proprietario(imob_dict['NOME'], imob_dict['CPF'], imob_dict['RG'], imob_dict['ENDERECO'], imob_dict['TELEFONE'],
                                    imob_dict['EMAIL'], imob_dict['CIDADE'],imob_dict['BAIRRO'],imob_dict['proprietarios.ID_PROP'])

        imovel = Imovel(tipo, imob_dict['FINALIDADE'], cidade, bairro, imob_dict['ENDERECO_IMOVEL'], imob_dict['AREA'],
                        imob_dict['DETALHES'], imob_dict['VALOR_IMOVEL'], imob_dict['STATUS'],
                        imob_dict['PORCENTAGEM'], proprietario, corretor, imob_dict['VALOR_VENDA'], imob_dict['HONORARIOS'],
                        imob_dict['BANHEIRO'], imob_dict['QUARTOS'], imob_dict['GARAGEM'], imob_dict['ID_IMOB'])

        del tipo, cidade, bairro, proprietario
        return imovel


    def filtra(self, id, filtro):
        filtros_dic = {
            "filtra_cidade" : SQL_FILTRA_CIDADE,
            "filtra_prop" : SQL_FILTRA_PROP,
            "filtra_status" : SQL_FILTRA_STATUS,
            "filtra_quartos": SQL_FILTRO_QUARTO,
            "filtra_banheiro": SQL_FILTRO_BANHEIRO,
            "filtra_garagem": SQL_FILTRO_GARAGEM,
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
            tipo = Tipo(imob_dict['TIPO'], imob_dict['ID_TIPO'])

            cidade = Cidade(imob_dict['CIDADE'], imob_dict['ID_CID'])

            bairro = Bairro(imob_dict['BAIRRO'], imob_dict['CIDADE_ID_CID'], imob_dict['bairro.ID_BAIRRO'], imob_dict['CIDADE'])

            proprietario = Proprietario(imob_dict['NOME'],imob_dict['CPF'],imob_dict['RG'],imob_dict['ENDERECO'],imob_dict['TELEFONE'],imob_dict['EMAIL'], imob_dict['proprietarios.ID_PROP'])

            imovel = Imovel(tipo,imob_dict['FINALIDADE'],cidade,bairro,imob_dict['ENDERECO_IMOVEL'],imob_dict['AREA'],imob_dict['DETALHES'],imob_dict['VALOR_IMOVEL'],
                            imob_dict['STATUS'],imob_dict['PORCENTAGEM'],proprietario,imob_dict['ID_CORR'],imob_dict['VALOR_VENDA'],imob_dict['HONORARIOS'],imob_dict['BANHEIRO'],
                            imob_dict['QUARTOS'],imob_dict['GARAGEM'],imob_dict['ID_IMOB'])
            del tipo,cidade,bairro,proprietario
            return imovel
        return list(map(traduz_para_objct_imob, imob_dictlist))

class financeiroDao:
    def __init__(self, db):
        self.__db = db
    def salvar(self,finaceiro):
        cursor = self.__db.connection.cursor()
        if(finaceiro._id_fin):
            cursor.execute(SQL_ATUALIZA_FIN,(finaceiro.get_honorarios_corr(), finaceiro._porcentagem_corr, finaceiro.get_honorarios_imob(),
                                             finaceiro._porcentagem_imob,finaceiro._corr,finaceiro._id_fin))
        else:
            cursor.execute(SQL_CRIA_FIN,(finaceiro.get_honorarios_corr(), finaceiro._porcentagem_corr, finaceiro.get_honorarios_imob(),
                                         finaceiro._porcentagem_imob,finaceiro._corr,finaceiro._imob))
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        del finaceiro
        return cursor._id

    def pocurar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_FIN_ID, (id,))
        fin_dict = cursor.fetchone()
        if fin_dict:
            fin = Financeiro(fin_dict['HONORARIOS_CORR'],fin_dict['PORCENTAGEM_CORR'],
                         fin_dict['HONORARIOS_IMOB'],fin_dict['PORCENTAGEM_IMOB'], id_fin=fin_dict['ID_FIN'])
            return fin
        else:
            return None

    def deletar(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_FIN, (id,))
        self.__db.connection.commit()

    def lista(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_FIN)
        fin = self.traduz_para_lista_fin(cursor.fetchall())
        return fin

    def filtro(self,filtro):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_FIN_CORR, (filtro,))
        fin = self.traduz_para_lista_fin(cursor.fetchall())
        return fin

    def traduz_para_lista_fin(self,fin_dictlist):
        def traduz_para_objeto_fin(fin_dict):
            return Financeiro(fin_dict['HONORARIOS_CORR'],fin_dict['PORCENTAGEM_CORR'],fin_dict['HONORARIOS_IMOB'],fin_dict['PORCENTAGEM_IMOB'],
                              fin_dict['HONORARIOS'],fin_dict['VALOR_VENDA'],fin_dict['ENDERECO_IMOVEL'],fin_dict['NOME'],corr_id=fin_dict['ID_CORR_FIN'],id_fin=fin_dict['ID_FIN'])
        return list(map(traduz_para_objeto_fin, fin_dictlist))

#tipos
class tiposDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, tipo):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_TIPOS,(tipo._id_tipo,tipo._tipo_nome))
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        del tipo

    def lista(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_TIPOS)
        tipos = self.traduz_para_lista_tipos(cursor.fetchall())
        return tipos

    def traduz_para_lista_tipos(self, tipo_dictlist):
        def traduz_para_objct_tipo(tipo_dict):
            return Tipo(tipo_dict['TIPO'],tipo_dict['ID_TIPO'])
        return list(map(traduz_para_objct_tipo,tipo_dictlist))

class ciadadeDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cidade):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_CIDADE,(cidade._id_cidade,cidade._cidade_nome))
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
                return Cidade(cidade_dict['CIDADE'],cidade_dict['ID_CID'])
        return list(map(traduz_para_objct_cidade, cidade_dictlist))

class bairroDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, bairro):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_BAIRRO,(bairro._id_bairro,bairro._bairro_nome,bairro._id_cid))
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        del bairro

    def lista(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_BAIRRO)
        bairros = self.traduz_para_lista_bairros(cursor.fetchall())
        return bairros

    def traduz_para_lista_bairros(self, bairro_dictlist):
        def traduz_para_objct_bairro(bairro_dict):
            return Bairro(bairro_dict['BAIRRO'],bairro_dict['CIDADE_ID_CID'], bairro_dict['ID_BAIRRO'], bairro_dict['CIDADE'])
        return list(map(traduz_para_objct_bairro, bairro_dictlist))
