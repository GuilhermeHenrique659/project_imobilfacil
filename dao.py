from models import imovel,Proprietario, Corretores, Imob_Prop

#Sql da tabela imoveis
SQL_CRIA_IMOVEL = 'INSERT into imoveis (ID_CORR, ID_PROP, SINGLA, TIPO, FINALIDADE, BAIRRO, QUADRA, LOTE, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS)' \
                  ' values (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s)'

SQL_DELETA_IMOVEL = 'delete from imoveis where ID = %s'

SQL_ATUALIZA_IMOVEIS = 'UPDATE imoveis SET SIGLA=%s,TIPO=%s,FINALIDADE=%s,BAIRRO,QUADRA=%s,LOTE=%s,' \
                       'VALOR_VENDA=%s,STATUS=%s, PORCENTAGEM=%s, HONORARIOS=%s, PROPRIETARIO_ID=%s where ID=%s'

'''SQL_BUSCA_LISTA_IMOB = 'SELECT ID_IMOB, ID_CORR, ID_PROP, SINGLA, TIPO, FINALIDADE, BAIRRO, QUADRA, LOTE, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS from imoveis'
'''

SQL_BUSCA_LISTA_IMOB = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP'


#Sql da tabela propeitarios
#SQL_DELETA_PROPRIETARIO = 'delete from proprietarios where ID_PROP = %s'

SQL_CRIA_PROPRIETARIO = 'INSERT into proprietarios (NOME, CPF, RG, ENDERECO, TELEFONE, EMAIL) values (%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_PROPRIETARIO = 'UPDATE proprietarios SET NOME=%s, CPF=%s, RG=%s, ENDERECO=%s, TELEFONE=%s, EMAIL=%s  where ID_PROP=%s'

SQL_BUSCAR_LISTA_PROP = 'SELECT ID_PROP, NOME, CPF, RG, ENDERECO,TELEFONE,EMAIL from proprietarios'

#Sql da tabela corretores
SQL_CRIA_CORRETORES = 'INSERT into corretores (USUARIO,EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_CORRETORES = 'UPDATE corretores SET USUARIO=%s,EMAIL=%s,NOME=%s,IMOBIL=%s,CRECI=%s,CELULAR=%s,CPF=%s,ENDERECO=%s,SENHA=%s  where ID_CORR=%s'

SQL_BUSCA_LISTA_CORRETORES = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA from corretores'

SQL_BUSCA_CORR_ID = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA from corretores where USUARIO=%s'


#proprietarios
class cad_proprietario_dao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, Proprietario):
        cursor = self.__db.connection.cursor()

        if (Proprietario._id):
            cursor.execute(SQL_ATUALIZA_PROPRIETARIO, (Proprietario._nome, Proprietario._cpf,Proprietario._rg, Proprietario._endereco, Proprietario._id, Proprietario._telefone,Proprietario._email))
        else:
            cursor.execute(SQL_CRIA_PROPRIETARIO, (Proprietario._nome,Proprietario._rg, Proprietario._cpf, Proprietario._endereco, Proprietario._telefone, Proprietario._email))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return Proprietario

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCAR_LISTA_PROP)
        proprietarios = traduz_prop(cursor.fetchall())
        return proprietarios

def traduz_prop(proprietarios):
    def cria_prop_lista(tupla):
        return Proprietario(tupla[1], tupla[2],tupla[3], tupla[4],tupla[5], tupla[6], id=tupla[0])
    return list(map(cria_prop_lista, proprietarios))
#corretor/

class cad_corretor_dao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, corretor):
        cursor = self.__db.connection.cursor()

        if (corretor._id_corr):
            cursor.execute(SQL_ATUALIZA_CORRETORES, (corretor._id_corr,corretor._usuario,corretor._email,corretor._nome,corretor._imobil,corretor._creci,corretor._celular,corretor._cpf,corretor._endereco,corretor._senha))
        else:
            cursor.execute(SQL_CRIA_CORRETORES, (corretor._usuario,corretor._email,corretor._nome,corretor._imobil,corretor._creci,corretor._celular,corretor._cpf,corretor._endereco,corretor._senha))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return corretor
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
#cria objeto usuario
def traduz_usuario(tupla):
    return Corretores(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9], id_corr=tupla[0])

#tranforma dodos do bd em uma lista de objetos
def traduz_corr(corretores):
    def cria_corr(tupla):
        return Corretores(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9], id_corr=tupla[0])
    return list(map(cria_corr, corretores))
#imovel/

class imovelDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, imovel):
        cursor = self.__db.connection.cursor()

        if (imovel._id):
            cursor.execute(SQL_ATUALIZA_IMOVEIS,( imovel._sigla, imovel._tipo, imovel._finalidade,
                                                imovel._bairro, imovel._quadra,imovel._lote,imovel.get_area(),imovel._descricao,
                                                imovel.get_valor_imovel(),imovel.get_valor_venda(),imovel._status,
                                                imovel.get_percentagem(), imovel.get_honorarios(), imovel._proprietario_id ) )
        else:
            cursor.execute(SQL_CRIA_IMOVEL,( imovel._corretor_id ,imovel._proprietario_id,imovel._sigla, imovel._tipo, imovel._finalidade,
                                            imovel._bairro, imovel._quadra,imovel._lote, imovel.get_area(),
                                            imovel._descricao, imovel.get_valor_imovel(), imovel.get_valor_venda(), imovel._status,
                                            imovel.get_percentagem(), imovel.get_honorarios()))
        self.__db.connection.commit()
        return imovel

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LISTA_IMOB)
        imoveis = traduz_imob(cursor.fetchall())
        return imoveis

def traduz_imob(imoveis):
    def cria_imob_lista(tupla):
        return Imob_Prop(tupla[3],tupla[4],tupla[5],tupla[6],tupla[7], tupla[8],tupla[9],tupla[10], tupla[11],tupla[13],tupla[14],
                      tupla[2], tupla[1], tupla[0], tupla[12],tupla[15],tupla[17], tupla[18], tupla[19], tupla[20], tupla[21], tupla[22],tupla[16])
    return list(map(cria_imob_lista, imoveis))