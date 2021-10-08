from models import imovel

SQL_CRIA_IMOVEL = 'INSERT into imoveis (SINGLA, TIPO, FINALIDADE, BAIRRO, QUADRA, LOTE, VALOR, ' \
                  'STATUS, PORCENTAGEM, HONORARIOS, PROPRIETARIO_ID) values (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s)'
SQL_DELETA_IMOVEL = 'delete from imoveis where ID = %s'

SQL_ATUALIZA_IMOVEIS = 'UPDATE imoveis SET SIGLA=%s,TIPO=%s,FINALIDADE=%s,BAIRRO,QUADRA=%s,LOTE=%s,' \
                       'VALOR=%s,STATUS=%s, PORCENTAGEM=%s, HONORARIOS=%s, PROPRIETARIO_ID=%s where ID=%s'

class imovelDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, imovel):
        cursor = self.__db.connection.cursor()

        if (imovel._id):
            cursor.execute(SQL_ATUALIZA_IMOVEIS,(imovel._sigla, imovel._tipo, imovel._finalidade,
                                                 imovel._bairro, imovel._quadra,imovel._lote, imovel._valor, imovel._satus,
                                                 imovel._porcentagem, imovel._honorarios, imovel._proprietario_id ) )
        else:
            cursor.execute(SQL_CRIA_IMOVEL,(imovel._sigla, imovel._tipo, imovel._finalidade,
                                            imovel._bairro,imovel._quadra ,imovel._lote, imovel._valor, imovel._satus,
                                            imovel._porcentagem, imovel._honorarios, imovel._proprietario_id ) )
        self.__db.connection.commit()
        return imovel