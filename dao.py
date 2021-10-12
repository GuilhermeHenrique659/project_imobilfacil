from models import imovel

SQL_CRIA_IMOVEL = 'INSERT into imoveis (ID_CORR, ID_PROP, SINGLA, TIPO, FINALIDADE, BAIRRO, QUADRA, LOTE, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS)' \
                  ' values (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s)'

SQL_DELETA_IMOVEL = 'delete from imoveis where ID = %s'

SQL_ATUALIZA_IMOVEIS = 'UPDATE imoveis SET SIGLA=%s,TIPO=%s,FINALIDADE=%s,BAIRRO,QUADRA=%s,LOTE=%s,' \
                       'VALOR_VENDA=%s,STATUS=%s, PORCENTAGEM=%s, HONORARIOS=%s, PROPRIETARIO_ID=%s where ID=%s'

SQL_BUSCA_LISTA_IMOB = 'SELECT ID_IMOB, ID_CORR, ID_PROP, SINGLA, TIPO, FINALIDADE, BAIRRO, QUADRA, LOTE, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS from imoveis'

class imovelDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, imovel):
        cursor = self.__db.connection.cursor()

        if (imovel._id):
            cursor.execute(SQL_ATUALIZA_IMOVEIS,( imovel._sigla, imovel._tipo, imovel._finalidade,
                                                imovel._bairro, imovel._quadra,imovel._lote,imovel.get_imovel_venda(),imovel._status,
                                                imovel._porcentagem, imovel.get_honorarios(), imovel._proprietario_id ) )
        else:
            cursor.execute(SQL_CRIA_IMOVEL,( imovel._corretor_id ,imovel._proprietario_id,imovel._sigla, imovel._tipo, imovel._finalidade,
                                            imovel._bairro, imovel._quadra,imovel._lote, imovel._area,
                                            imovel._descricao, imovel._valor_imovel, imovel.get_imovel_venda(), imovel._status,
                                            imovel._porcentagem, imovel.get_honorarios()) )
        self.__db.connection.commit()
        return imovel

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LISTA_IMOB)
        imoveis = traduz_imob(cursor.fetchall())
        return imoveis

def traduz_imob(imoveis):
    def cria_imob_lista(tupla):
        return imovel(tupla[3],tupla[4],tupla[5],tupla[6],tupla[7], tupla[8],tupla[9],tupla[10], tupla[11],tupla[13],tupla[14],
                      tupla[2], tupla[1], tupla[0], tupla[12],tupla[15])
    return list(map(cria_imob_lista, imoveis))