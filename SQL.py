#SQL DA TABELA IMOVEIS
SQL_CRIA_IMOVEL = '''
                INSERT INTO IMOVEIS (ID_CORR, ID_PROP, ID_CIDADE,ID_BAIRRO,CATEGORIA,FORMA,LADO_ESQ,LADO_DIR,LADO_FRE,
                                    LADO_FUN,TOTAL,TOPOGRAFIA,AREA_UTIL,CONSTRUIDA,EDICULA,AREA_INFO,TIPO,SUBTIPO,ENDERECO_IMOVEL,
                                    NUMERO,CEP,END_INFO,PLACA,DATA_PLACA,DATA_VISITA,DATA_ULTIMA_VIS,URL,COD_ANUNCIO,ANUNCIO_INFO,
                                    VALOR_IMOVEL,VALOR_VENDA,CORRETAGEM,REPASSE_IMOB)
                VALUES (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s);
'''

SQL_CRIA_IMOVEL_DESC = '''
                    INSERT INTO IMOVEL_DESC (ID_IMOB,VAGAS,BANHEIRO,SUITE,DORMITORIOS,AREA_SERVICO,COPA,
                    EDICULA ,LAREIRA ,PORTAO_ELEC ,HIDROMSG ,PISO ,SACADA ,SALA_VIST ,SALA_ESTAR ,SOTAO ,AMARINHO ,
                    COZINHA ,ESCRITORIO ,LAVABO ,SALA_JANTAR ,VARANDA ,CLARABOIA ,DEP_EMPREGADA ,GARAGE ,LIVING_ROOM ,
                    QUINTAL ,SALA_TV ,W_C_EMPREGADA ,CLOSET ,DESPENSA ,CHURRASQUEIRA ,PORTARIA_24H ,SALAO_FESTA ,
                    JD_INVERNO ,QUADRA ,SAUNA ,PISCINA ,ENTRADA_INDEP ,QUADRA_TENIS ,PLAYGROUND ,SALA_GINASTICA)
                    VALUES (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s ,%s, %s, 
                            %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s);
'''

SQL_ATUALIZA_DESC = '''UPDATE IMOVEL_DESC SET VAGAS =%s,BANHEIRO =%s,SUITE =%s, DORMITORIOS =%s,AREA_SERVICO =%s,COPA =%s,EDICULA =%s,
                        LAREIRA =%s,PORTAO_ELEC =%s,HIDROMSG =%s,PISO =%s,SACADA =%s,SALA_VIST =%s,SALA_ESTAR =%s,SOTAO =%s,AMARINHO =%s,
                        COZINHA =%s,ESCRITORIO =%s,LAVABO =%s,SALA_JANTAR =%s,VARANDA =%s,CLARABOIA =%s,DEP_EMPREGADA =%s,GARAGE =%s,
                        LIVING_ROOM =%s,QUINTAL =%s,SALA_TV =%s,W_C_EMPREGADA =%s,CLOSET =%s,DESPENSA =%s,CHURRASQUEIRA =%s,PORTARIA_24H =%s,SALAO_FESTA =%s,
                        JD_INVERNO =%s,QUADRA =%s,SAUNA =%s,PISCINA =%s,ENTRADA_INDEP =%s,QUADRA_TENIS =%s,PLAYGROUND =%s,SALA_GINASTICA =%s WHERE ID_DESC = %s
'''

SQL_DELETA_IMOVEL = 'DELETE FROM IMOVEIS WHERE ID_IMOB = %s'

SQL_ATUALIZA_IMOVEIS = ''' UPDATE IMOVEIS SET  ID_CORR=%s, ID_PROP=%s, ID_CIDADE=%s,ID_BAIRRO=%s,
                                    CATEGORIA=%s,FORMA=%s,LADO_ESQ=%s,LADO_DIR=%s,LADO_FRE=%s,
                                    LADO_FUN=%s,TOTAL=%s,TOPOGRAFIA=%s,AREA_UTIL=%s,CONSTRUIDA=%s,EDICULA=%s,
                                    AREA_INFO=%s,TIPO=%s,SUBTIPO=%s,ENDERECO_IMOVEL=%s,
                                    NUMERO=%s,CEP=%s,END_INFO=%s,PLACA=%s,DATA_PLACA=%s,DATA_VISITA=%s,DATA_ULTIMA_VIS=%s,
                                    URL=%s,COD_ANUNCIO=%s,ANUNCIO_INFO=%s,
                                     VALOR_IMOVEL=%s,VALOR_VENDA=%s,CORRETAGEM=%s,REPASSE_IMOB=%s WHERE ID_IMOB=%s;
    '''

SQL_BUSCA_LISTA_IMOB = 'SELECT ID_IMOB,CATEGORIA,CIDADE,BAIRRO,ENDERECO_IMOVEL,NOME,CELULAR FROM IMOVEIS LEFT JOIN PROPRIETARIOS ON IMOVEIS.ID_PROP = PROPRIETARIOS.ID_PROP' \
                       ' JOIN CIDADE ON CIDADE.ID_CID = IMOVEIS.ID_CIDADE JOIN BAIRRO ON BAIRRO.ID_BAIRRO = IMOVEIS.ID_BAIRRO'


SQL_BUSCA_IMOB_ID ='''SELECT * FROM IMOVEIS LEFT JOIN PROPRIETARIOS ON IMOVEIS.ID_PROP = PROPRIETARIOS.ID_PROP 
                    JOIN CIDADE ON CIDADE.ID_CID = IMOVEIS.ID_CIDADE 
                    JOIN BAIRRO ON BAIRRO.ID_BAIRRO = IMOVEIS.ID_BAIRRO 
                    LEFT JOIN CORRETORES ON IMOVEIS.ID_CORR = CORRETORES.ID_CORR 
                    LEFT JOIN IMOVEL_DESC ON IMOVEIS.ID_IMOB = IMOVEL_DESC.ID_IMOB
                    WHERE IMOVEIS.ID_IMOB = %s
'''
 
#SQL DA TABELA PROPEITARIOS

SQL_DELETA_PROPRIETARIO = 'DELETE FROM PROPRIETARIOS WHERE ID_PROP = %s'


SQL_CRIA_PROPRIETARIO = 'INSERT INTO PROPRIETARIOS (NOME, CPF_CNPJ, RG_INSC_ETAD, SEXO, ENDERECO, CEP , NUMERO, PESSOA, RAZAO ,' \
                        'TELEFONE, CELULAR, WHATAPPS, EMAIL,CAPITAL, PATRIMONIO, ATIVIDADE, ID_CIDADE, ID_BAIRRO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_PROPRIETARIO = 'UPDATE PROPRIETARIOS SET NOME=%s, CPF_CNPJ=%s, RG_INSC_ETAD=%s, SEXO=%s, ENDERECO=%s, CEP=%s , NUMERO=%s, PESSOA=%s, RAZAO=%s ,' \
                        'TELEFONE=%s, CELULAR=%s, WHATAPPS=%s, EMAIL=%s,CAPITAL=%s, PATRIMONIO=%s, ATIVIDADE=%s, ID_CIDADE=%s, ID_BAIRRO=%s WHERE ID_PROP=%s'

SQL_BUSCAR_LISTA_PROP = 'SELECT ID_PROP, NOME, CPF_CNPJ, RG_INSC_ETAD, ENDERECO, TELEFONE, EMAIL, ID_CIDADE, ID_BAIRRO FROM PROPRIETARIOS'

SQL_FIND_PROP_BY_NAME = 'SELECT ID_PROP, NOME, CPF_CNPJ, RG_INSC_ETAD, ENDERECO, TELEFONE, EMAIL, ID_CIDADE, ID_BAIRRO FROM PROPRIETARIOS WHERE NOME LIKE %s'

SQL_PROP_POR_ID = 'SELECT * FROM PROPRIETARIOS ' \
                  'LEFT JOIN CIDADE ON PROPRIETARIOS.ID_CIDADE = CIDADE.ID_CID ' \
                  'LEFT JOIN BAIRRO ON PROPRIETARIOS.ID_BAIRRO = BAIRRO.ID_BAIRRO WHERE ID_PROP=%s'


#SQL DA TABELA CORRETORES
SQL_DELETA_CORRETOR = 'DELETE FROM CORRETORES WHERE ID_CORR = %s'

SQL_CRIA_CORRETORES = 'INSERT INTO CORRETORES (USUARIO,EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_CORRETORES = 'UPDATE CORRETORES SET USUARIO=%s,EMAIL=%s,NOME=%s,CRECI=%s,CELULAR=%s,CPF=%s,ENDERECO=%s,SENHA=%s,ID_CIDADE=%s,ID_BAIRRO=%s  WHERE ID_CORR=%s'

SQL_BUSCA_LISTA_CORRETORES = "SELECT ID_CORR, USUARIO, EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO FROM CORRETORES WHERE USUARIO!='ADMIN'"

SQL_BUSCA_CORR_ID = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO FROM CORRETORES WHERE USUARIO=%s OR EMAIL=%s'

SQL_FIND_CORR_BY_NAME = "SELECT ID_CORR, USUARIO, EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO FROM CORRETORES WHERE NOME LIKE %s AND USUARIO!='ADMIN'"

SQL_BUSCA_CORR_POR_ID = 'SELECT * FROM CORRETORES ' \
                        'LEFT JOIN CIDADE ON CORRETORES.ID_CIDADE = CIDADE.ID_CID ' \
                        'LEFT JOIN BAIRRO ON CORRETORES.ID_BAIRRO = BAIRRO.ID_BAIRRO WHERE ID_CORR=%s'


#SQL DA TABELA FINANCEIRO
SQL_BUSCA_FIN_ID = 'SELECT * FROM FINANCEIRO WHERE ID_IMOB_FIN = %s'

SQL_DELETA_FIN = 'DELETE FROM FINANCEIRO WHERE ID_IMOB_FIN = %s'

SQL_CRIA_FIN = 'INSERT INTO FINANCEIRO (HONORARIOS_CORR,PORCENTAGEM_CORR, HONORARIOS_IMOB, PORCENTAGEM_IMOB ,ID_CORR_FIN, ID_IMOB_FIN) VALUES(%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_FIN = 'UPDATE FINANCEIRO SET HONORARIOS_CORR=%s,PORCENTAGEM_CORR=%s, HONORARIOS_IMOB=%s, PORCENTAGEM_IMOB=%s, ID_CORR_FIN=%s WHERE ID_FIN=%s'

SQL_LISTA_FIN = 'SELECT FINANCEIRO.ID_FIN, FINANCEIRO.HONORARIOS_CORR, FINANCEIRO.PORCENTAGEM_CORR,FINANCEIRO.HONORARIOS_IMOB, FINANCEIRO.PORCENTAGEM_IMOB, ' \
                'CORRETORES.NOME, IMOVEIS.ENDERECO_IMOVEL , IMOVEIS.VALOR_VENDA, IMOVEIS.HONORARIOS,FINANCEIRO.ID_CORR_FIN FROM FINANCEIRO ' \
                'INNER JOIN CORRETORES ON FINANCEIRO.ID_CORR_FIN = ID_CORR ' \
                'INNER JOIN IMOVEIS ON FINANCEIRO.ID_IMOB_FIN = IMOVEIS.ID_IMOB'

SQL_LISTA_FIN_CORR = 'SELECT FINANCEIRO.ID_FIN, FINANCEIRO.HONORARIOS_CORR, FINANCEIRO.PORCENTAGEM_CORR,FINANCEIRO.HONORARIOS_IMOB, FINANCEIRO.PORCENTAGEM_IMOB, ' \
                'CORRETORES.NOME, IMOVEIS.ENDERECO_IMOVEL , IMOVEIS.VALOR_VENDA, IMOVEIS.HONORARIOS,FINANCEIRO.ID_CORR_FIN FROM FINANCEIRO ' \
                'INNER JOIN CORRETORES ON FINANCEIRO.ID_CORR_FIN = ID_CORR ' \
                'INNER JOIN IMOVEIS ON FINANCEIRO.ID_IMOB_FIN = IMOVEIS.ID_IMOB WHERE FINANCEIRO.ID_CORR_FIN = %s'

#TIPOS
SQL_CRIA_TIPOS = 'INSERT INTO TIPOS (ID_TIPO,TIPO) VALUES(%s,%s)'
SQL_LISTA_TIPOS = 'SELECT * FROM TIPOS'


#CIDADE E BAIRRO
SQL_CRIA_CIDADE = 'INSERT INTO CIDADE (ID_CID,CIDADE) VALUES(%s,%s)'
SQL_LISTA_CIDADE = 'SELECT * FROM CIDADE'
SQL_CRIA_BAIRRO = 'INSERT INTO BAIRRO (ID_BAIRRO,BAIRRO,CIDADE_ID_CID) VALUES(%s,%s, %s)'
SQL_LISTA_BAIRRO = 'SELECT * FROM BAIRRO INNER JOIN CIDADE ON BAIRRO.CIDADE_ID_CID = CIDADE.ID_CID'


#FILTROS
SQL_FILTRA_CIDADE = 'SELECT ID_IMOB,CATEGORIA,CIDADE,BAIRRO,ENDERECO_IMOVEL,NOME,CELULAR FROM IMOVEIS LEFT JOIN PROPRIETARIOS ON IMOVEIS.ID_PROP = PROPRIETARIOS.ID_PROP' \
                       ' JOIN CIDADE ON CIDADE.ID_CID = IMOVEIS.ID_CIDADE JOIN BAIRRO ON BAIRRO.ID_BAIRRO = IMOVEIS.ID_BAIRRO WHERE IMOVEIS.ID_BAIRRO WHERE IMOVEIS.ID_CIDADE= %s'

SQL_FILTRA_PROP = 'SELECT ID_IMOB,CATEGORIA,CIDADE,BAIRRO,ENDERECO_IMOVEL,NOME,CELULAR FROM IMOVEIS LEFT JOIN PROPRIETARIOS ON IMOVEIS.ID_PROP = PROPRIETARIOS.ID_PROP' \
                       ' JOIN CIDADE ON CIDADE.ID_CID = IMOVEIS.ID_CIDADE JOIN BAIRRO ON BAIRRO.ID_BAIRRO = IMOVEIS.ID_BAIRRO WHERE IMOVEIS.ID_PROP = %s'

SQL_FILTRO_BAIRRO = 'SELECT ID_IMOB,CATEGORIA,CIDADE,BAIRRO,ENDERECO_IMOVEL,NOME,CELULAR FROM IMOVEIS LEFT JOIN PROPRIETARIOS ON IMOVEIS.ID_PROP = PROPRIETARIOS.ID_PROP' \
                       ' JOIN CIDADE ON CIDADE.ID_CID = IMOVEIS.ID_CIDADE JOIN BAIRRO ON BAIRRO.ID_BAIRRO = IMOVEIS.ID_BAIRRO WHERE WHERE IMOVEIS.ID_BAIRRO = %s'