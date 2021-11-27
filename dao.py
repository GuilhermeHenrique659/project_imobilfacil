from models import Imovel,Proprietario, Corretores, Tipo, Cidade, Bairro, Financeiro
from SQL import *

#proprietarios
class cad_proprietario_dao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, Proprietario):
        cursor = self.__db.connection.cursor()

        if (Proprietario._id):
            cursor.execute(SQL_ATUALIZA_PROPRIETARIO, (Proprietario._nome, Proprietario._cpf,Proprietario._rg, Proprietario._endereco_prop, Proprietario._telefone,Proprietario._email,Proprietario._cidade,Proprietario._bairro, Proprietario._id))
        else:
            cursor.execute(SQL_CRIA_PROPRIETARIO, (Proprietario._nome,Proprietario._rg, Proprietario._cpf, Proprietario._endereco_prop, Proprietario._telefone, Proprietario._email,Proprietario._cidade,Proprietario._bairro))
            cursor._id = cursor.lastrowid
        self.__db.connection.commit()

        del Proprietario

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCAR_LISTA_PROP)
        proprietarios = traduz_prop(cursor.fetchall())
        return proprietarios

    # busca um unico proprietario pelo id
    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PROP_POR_ID, (id,))
        tupla = cursor.fetchone()
        cidade = Cidade(id_cidade=tupla[9], cidade_nome=tupla[10])

        bairro = Bairro(id_bairro=tupla[11], bairro_nome=tupla[12], id_cid=tupla[13],bairro_cidade_nome=tupla[10])

        proprietario = Proprietario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], cidade, bairro, id=tupla[0])
        del cidade,bairro
        return proprietario
    def deletar_prop(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_PROPRIETARIO, (id,))
        self.__db.connection.commit()


def traduz_prop(proprietarios):
    def cria_prop_lista(tupla):
        return Proprietario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], id=tupla[0])
    return list(map(cria_prop_lista, proprietarios))

#corretor/
class cad_corretor_dao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, corretor):
        cursor = self.__db.connection.cursor()

        if (corretor._id_corr):
            cursor.execute(SQL_ATUALIZA_CORRETORES, (corretor._usuario,corretor._email,corretor._nome,corretor._creci,corretor._celular,corretor._cpf,corretor._endereco,corretor._senha,corretor._cidade,corretor._bairro,corretor._id_corr))
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
        corretores = traduz_corr(cursor.fetchall())
        return corretores

    # busca um unico corretor pelo usuario no login
    def buscar_por_id(self,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CORR_ID, (usuario,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    # busca um unico corretor pelo id
    def busca_por_id_edit(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CORR_POR_ID, (id,))
        tupla = cursor.fetchone()
        cidade = Cidade(id_cidade=tupla[11], cidade_nome=tupla[12])
        bairro = Bairro(id_bairro=tupla[13], bairro_nome=tupla[14], id_cid=tupla[15],bairro_cidade_nome=tupla[12])
        corretor = Corretores(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8],cidade,bairro, id_corr=tupla[0])
        del cidade,bairro
        return corretor

    def deletar_corr(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_CORRETOR, (id,))
        self.__db.connection.commit()

#cria objeto usuario
def traduz_usuario(tupla):
    return Corretores(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],tupla[10], id_corr=tupla[0])

#tranforma dodos do bd em uma lista de objetos
def traduz_corr(corretores):
    def cria_corr(tupla):
        return Corretores(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],tupla[10], id_corr=tupla[0])
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
        tipo = Tipo(id_tipo=tupla[27], tipo_nome=tupla[28])

        cidade = Cidade(id_cidade=tupla[29], cidade_nome=tupla[30])

        bairro = Bairro(id_bairro=tupla[31], bairro_nome=tupla[32], id_cid=tupla[33], bairro_cidade_nome=tupla[30])

        proprietario = Proprietario(tupla[19], tupla[20], tupla[21], tupla[22], tupla[23], tupla[24], id=tupla[18])

        corretor = Corretores(tupla[35],tupla[36],tupla[37],tupla[38],tupla[39],tupla[40],tupla[41],tupla[42],tupla[43], id_corr=tupla[34])

        imovel = Imovel(tipo, tupla[4], cidade, bairro, tupla[7], tupla[8], tupla[9], tupla[10], tupla[12], tupla[13],
                        proprietario, corretor, tupla[11], tupla[14], tupla[15], tupla[16], tupla[17], imob_id=tupla[0])

        del tipo, cidade, bairro, proprietario, corretor
        return imovel


    def filtra(self, id, filtro):
        filtros_dic = {
            "filtra_cidade" : SQL_FILTRA_CIDADE,
            "filtra_prop" : SQL_FILTRA_PROP,
            "filtra_status" : SQL_FILTRA_STATUS,
            "filtra_quartos": SQL_FILTRO_QUARTO,
            "filtra_banheiro": SQL_FILTRO_BANHEIRO,
            "filtra_garagem": SQL_FILTRO_GARAGEM,
            "filtra_bairro": SQL_FILTRO_BAIRRO
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
            tipo = Tipo(id_tipo=tupla[27], tipo_nome=tupla[28])

            cidade = Cidade(id_cidade=tupla[29], cidade_nome=tupla[30])

            bairro = Bairro(id_bairro=tupla[31], bairro_nome=tupla[32], id_cid=tupla[33], bairro_cidade_nome=tupla[30])

            proprietario = Proprietario(tupla[19],tupla[20],tupla[21],tupla[22],tupla[23],tupla[24], id=tupla[18])

            imovel = Imovel(tipo,tupla[4], cidade , bairro, tupla[7],tupla[8],tupla[9],tupla[10],tupla[12],tupla[13],
                            proprietario,tupla[2], tupla[11],tupla[14],tupla[15],tupla[16],tupla[17],imob_id=tupla[0])

            del tipo,cidade,bairro,proprietario
            return imovel
        return list(map(cria_imob_lista, imoveis))

class financeiroDao:
    def __init__(self, db):
        self.__db = db
    def salvar(self,finaceiro):
        cursor = self.__db.connection.cursor()
        if(finaceiro._id_fin):
            cursor.execute(SQL_ATUALIZA_FIN,(finaceiro.get_honorarios_corr(), finaceiro._porcentagem_corr, finaceiro.get_honorarios_imob(),
                                             finaceiro._porcentagem_imob,finaceiro._id_fin))
        else:
            cursor.execute(SQL_CRIA_FIN,(finaceiro.get_honorarios_corr(), finaceiro._porcentagem_corr, finaceiro.get_honorarios_imob(),
                                         finaceiro._porcentagem_imob,finaceiro._corr,finaceiro._imob))
            cursor._id = cursor.lastrowid
        self.__db.connection.commit()

    def pocura_deleta(self, id):
        fin = self.__db.connection.cursor().execute(SQL_BUSCA_FIN_ID, (id,))
        if fin:
            self.__db.connection.cursor().execute(SQL_DELETA_FIN, (id,))
            self.__db.connection.commit()
        else:
            fin = None
        return fin

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
            return Financeiro(tupla[1],tupla[2],tupla[3],tupla[4],tupla[8],tupla[7],tupla[6],tupla[5],tupla[0])
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

    def traduz_tipos(self, tipos):
        def cria_tipo_lista(tupla):
                return Tipo(tupla[1],tupla[0])
        return list(map(cria_tipo_lista, tipos))

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
        cidades = self.traduz_tipos(cursor.fetchall())
        return cidades

    def traduz_tipos(self, cidades):
        def cria_tipo_lista(tupla):
                return Cidade(tupla[1],tupla[0])
        return list(map(cria_tipo_lista, cidades))

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
        bairros = self.traduz_tipos(cursor.fetchall())
        return bairros

    def traduz_tipos(self, bairros):
        def cria_tipo_lista(tupla):
            return Bairro(tupla[1],tupla[2], id_bairro = tupla[0], bairro_cidade_nome = tupla[4])
        return list(map(cria_tipo_lista, bairros))

