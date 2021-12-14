from models import Imovel,Proprietario, Corretores, Tipo, Cidade, Bairro, Financeiro
from SQL import *

#proprietarios
class cad_proprietario_dao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, Proprietario):
        cursor = self.__db.connection.cursor()

        if (Proprietario._id):
            cursor.execute(SQL_ATUALIZA_PROPRIETARIO, (Proprietario._nome, Proprietario._cpf,Proprietario._rg, Proprietario._endereco_prop, Proprietario._telefone,
                                                       Proprietario._email,Proprietario._cidade,Proprietario._bairro, Proprietario._id))
        else:
            cursor.execute(SQL_CRIA_PROPRIETARIO, (Proprietario._nome,Proprietario._rg, Proprietario._cpf, Proprietario._endereco_prop, Proprietario._telefone,
                                                   Proprietario._email,Proprietario._cidade,Proprietario._bairro))
            cursor._id = cursor.lastrowid
        self.__db.connection.commit()

        del Proprietario

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCAR_LISTA_PROP)
        proprietarios = self.traduz_prop(cursor.fetchall())
        return proprietarios

    # busca um unico proprietario pelo id
    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PROP_POR_ID, (id,))
        tupla = cursor.fetchone()
        cidade = Cidade(tupla['CIDADE'], tupla['ID_CIDADE'])
        bairro = Bairro(tupla['BAIRRO'],tupla['CIDADE_ID_CID'],tupla['bairro.ID_BAIRRO'],tupla['CIDADE'])
        proprietario = Proprietario(tupla['NOME'], tupla['CPF'], tupla['RG'], tupla['ENDERECO'],
                                    tupla['TELEFONE'], tupla['EMAIL'], cidade, bairro, tupla['ID_PROP'])
        del cidade,bairro
        return proprietario
    def deletar_prop(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_PROPRIETARIO, (id,))
        self.__db.connection.commit()


    def traduz_prop(self,proprietarios):
        def cria_prop_lista(tupla):
            return Proprietario(tupla['NOME'], tupla['CPF'], tupla['RG'], tupla['ENDERECO'], tupla['TELEFONE'], None,tupla['ID_CIDADE'],tupla['ID_BAIRRO'],tupla['ID_PROP'])
        return list(map(cria_prop_lista, proprietarios))

#corretor/
class cad_corretor_dao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, corretor):
        cursor = self.__db.connection.cursor()
        if (corretor._id_corr):
            cursor.execute(SQL_ATUALIZA_CORRETORES, (corretor._usuario,corretor._email,corretor._nome,corretor._creci,corretor._celular,corretor._cpf,
                                                     corretor._endereco,corretor._senha,corretor._cidade,corretor._bairro,corretor._id_corr))
        else:
            cursor.execute(SQL_CRIA_CORRETORES, (corretor._usuario,corretor._email,corretor._nome,corretor._creci,
                                                 corretor._celular,corretor._cpf,corretor._endereco,corretor._senha,corretor._cidade,corretor._bairro))
        cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        del corretor

    # faz lista de corretores para mostrar no index
    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LISTA_CORRETORES)
        corretores = self.traduz_corr(cursor.fetchall())
        return corretores

    # busca um unico corretor pelo usuario no login
    def buscar_por_id(self,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CORR_ID, (usuario,))
        dados = cursor.fetchone()
        if dados:
            usuario = self.traduz_usuario(dados) if dados else None
            return usuario
        cursor.execute(SQL_BUSCA_CORR_EMAIL, (usuario,))
        dados = cursor.fetchone()
        if dados:
            print(dados)
            usuario = self.traduz_usuario(dados) if dados else None
            return usuario
        return None

    # busca um unico corretor pelo id
    def busca_por_id_edit(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CORR_POR_ID, (id,))
        tupla = cursor.fetchone()
        cidade = Cidade(tupla['CIDADE'], tupla['ID_CIDADE'])
        bairro = Bairro(tupla['BAIRRO'],tupla['CIDADE_ID_CID'],tupla['bairro.ID_BAIRRO'],tupla['CIDADE'])
        corretor = Corretores(tupla['USUARIO'], tupla['EMAIL'], tupla['NOME'], tupla['CRECI'], tupla['CELULAR'],
                              tupla['CPF'], tupla['ENDERECO'], tupla['SENHA'],cidade,bairro,tupla['ID_CORR'])
        del cidade,bairro
        return corretor

    def deletar_corr(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_CORRETOR, (id,))
        self.__db.connection.commit()

#cria objeto usuario
    def traduz_usuario(self,tupla):
        return Corretores(tupla['USUARIO'],tupla['EMAIL'],tupla['NOME'],tupla['CRECI'],tupla['CELULAR'],
                      tupla['CPF'],tupla['ENDERECO'],tupla['SENHA'],tupla['ID_CIDADE'],tupla['ID_BAIRRO'], tupla['ID_CORR'])

#tranforma dodos do bd em uma lista de objetos
    def traduz_corr(self,corretores):
        def cria_corr(tupla):
            return Corretores(tupla['USUARIO'],tupla['EMAIL'],tupla['NOME'],tupla['CRECI'],tupla['CELULAR'],
                      tupla['CPF'],tupla['ENDERECO'],tupla['SENHA'],tupla['ID_CIDADE'],tupla['ID_BAIRRO'], tupla['ID_CORR'])
        lista_corr = list(map(cria_corr, corretores))
        lista_corr.pop(0)
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
        imoveis = self.traduz_imob(cursor.fetchall())
        return imoveis

    def busca_imob_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_IMOB_ID, (id,))
        tupla = cursor.fetchone()
        tipo = Tipo(tupla['TIPO'], tupla['ID_TIPO'])

        cidade = Cidade(tupla['CIDADE'], tupla['ID_CID'])

        bairro = Bairro(tupla['BAIRRO'], tupla['CIDADE_ID_CID'], tupla['bairro.ID_BAIRRO'], tupla['CIDADE'])

        corretor = Corretores(tupla['USUARIO'],tupla['EMAIL'],tupla['corretores.NOME'],tupla['CRECI'],tupla['CELULAR'],
                      tupla['CPF'],tupla['ENDERECO'],tupla['SENHA'],tupla['ID_CIDADE'],tupla['ID_BAIRRO'], tupla['ID_CORR'])

        proprietario = Proprietario(tupla['NOME'], tupla['CPF'], tupla['RG'], tupla['ENDERECO'], tupla['TELEFONE'],
                                    tupla['EMAIL'], tupla['CIDADE'],tupla['BAIRRO'],tupla['proprietarios.ID_PROP'])

        imovel = Imovel(tipo, tupla['FINALIDADE'], cidade, bairro, tupla['ENDERECO_IMOVEL'], tupla['AREA'],
                        tupla['DETALHES'], tupla['VALOR_IMOVEL'], tupla['STATUS'],
                        tupla['PORCENTAGEM'], proprietario, corretor, tupla['VALOR_VENDA'], tupla['HONORARIOS'],
                        tupla['BANHEIRO'], tupla['QUARTOS'], tupla['GARAGEM'], tupla['ID_IMOB'])

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
        imoveis = self.traduz_imob(cursor.fetchall())
        return imoveis

    def deletar_imob(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_IMOVEL, (id,))
        self.__db.connection.commit()

    def traduz_imob(self,imoveis):
        def cria_imob_lista(tupla):
            tipo = Tipo(tupla['TIPO'], tupla['ID_TIPO'])

            cidade = Cidade(tupla['CIDADE'], tupla['ID_CID'])

            bairro = Bairro(tupla['BAIRRO'], tupla['CIDADE_ID_CID'], tupla['bairro.ID_BAIRRO'], tupla['CIDADE'])

            proprietario = Proprietario(tupla['NOME'],tupla['CPF'],tupla['RG'],tupla['ENDERECO'],tupla['TELEFONE'],tupla['EMAIL'], tupla['proprietarios.ID_PROP'])

            imovel = Imovel(tipo,tupla['FINALIDADE'],cidade,bairro,tupla['ENDERECO_IMOVEL'],tupla['AREA'],tupla['DETALHES'],tupla['VALOR_IMOVEL'],
                            tupla['STATUS'],tupla['PORCENTAGEM'],proprietario,tupla['ID_CORR'],tupla['VALOR_VENDA'],tupla['HONORARIOS'],tupla['BANHEIRO'],
                            tupla['QUARTOS'],tupla['GARAGEM'],tupla['ID_IMOB'])
            del tipo,cidade,bairro,proprietario
            return imovel
        return list(map(cria_imob_lista, imoveis))

class financeiroDao:
    def __init__(self, db):
        self.__db = db
    def salvar(self,finaceiro):
        cursor = self.__db.connection.cursor()
        if(finaceiro._id_fin):
            print(finaceiro._corr)
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
        tupla = cursor.fetchone()
        if tupla:
            fin = Financeiro(tupla['HONORARIOS_CORR'],tupla['PORCENTAGEM_CORR'],
                         tupla['HONORARIOS_IMOB'],tupla['PORCENTAGEM_IMOB'], id_fin=tupla['ID_FIN'])
            return fin
        else:
            return None

    def deletar(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_FIN, (id,))
        self.__db.connection.commit()

    def lista(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_FIN)
        fin = self.traduz_fin(cursor.fetchall())
        return fin

    def filtro(self,filtro):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LISTA_FIN_CORR, (filtro,))
        fin = self.traduz_fin(cursor.fetchall())
        return fin

    def traduz_fin(self,fin):
        def cria_lista_fin(tupla):
            return Financeiro(tupla['HONORARIOS_CORR'],tupla['PORCENTAGEM_CORR'],tupla['HONORARIOS_IMOB'],tupla['PORCENTAGEM_IMOB'],
                              tupla['HONORARIOS'],tupla['VALOR_VENDA'],tupla['ENDERECO_IMOVEL'],tupla['NOME'],corr_id=tupla['ID_CORR_FIN'],id_fin=tupla['ID_FIN'])
        return list(map(cria_lista_fin, fin))

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
        tipos = self.traduz_tipos(cursor.fetchall())
        return tipos

    def traduz_tipos(self, tipo):
        def cria_tipos_lista(dados):
            return Tipo(dados['TIPO'],dados['ID_TIPO'])
        return list(map(cria_tipos_lista,tipo))

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
        cidades = self.traduz_cidades(cursor.fetchall())
        return cidades

    def traduz_cidades(self, cidades):
        def cria_cidade_lista(tupla):
                return Cidade(tupla['CIDADE'],tupla['ID_CID'])
        return list(map(cria_cidade_lista, cidades))

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
        bairros = self.traduz_bairros(cursor.fetchall())
        return bairros

    def traduz_bairros(self, bairros):
        def cria_bairro_lista(tupla):
            return Bairro(tupla['BAIRRO'],tupla['CIDADE_ID_CID'], tupla['ID_BAIRRO'], tupla['CIDADE'])
        return list(map(cria_bairro_lista, bairros))