
#Sql da tabela imoveis
SQL_CRIA_IMOVEL = '''
                INSERT into imoveis (ID_CORR, ID_PROP, ID_CIDADE,ID_BAIRRO,CATEGORIA,FORMA,LADO_ESQ,LADO_DIR,LADO_FRE,
                                    LADO_FUN,TOTAL,TOPOGRAFIA,AREA_UTIL,CONSTRUIDA,EDICULA,AREA_INFO,TIPO,SUBTIPO,ENDERECO_IMOVEL,
                                    NUMERO,CEP,END_INFO,PLACA,DATA_PLACA,DATA_VISITA,DATA_ULTIMA_VIS,URL,COD_ANUNCIO,ANUNCIO_INFO,
                                    VALOR_IMOVEL,VALOR_VENDA,CORRETAGEM,REPASSE_IMOB)
                values (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s,
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
                        JD_INVERNO =%s,QUADRA =%s,SAUNA =%s,PISCINA =%s,ENTRADA_INDEP =%s,QUADRA_TENIS =%s,PLAYGROUND =%s,SALA_GINASTICA =%s WHERE ID_IMOB = %s
'''

SQL_DELETA_IMOVEL = 'delete from imoveis where ID_IMOB = %s'

SQL_ATUALIZA_IMOVEIS = ''' UPDATE imoveis SET  ID_CORR=%s, ID_PROP=%s, ID_CIDADE=%s,ID_BAIRRO=%s,
                                    CATEGORIA=%s,FORMA=%s,LADO_ESQ=%s,LADO_DIR=%s,LADO_FRE=%s,
                                    LADO_FUN=%s,TOTAL=%s,TOPOGRAFIA=%s,AREA_UTIL=%s,CONSTRUIDA=%s,EDICULA=%s,
                                    AREA_INFO=%s,TIPO=%s,SUBTIPO=%s,ENDERECO_IMOVEL=%s,
                                    NUMERO=%s,CEP=%s,END_INFO=%s,PLACA=%s,DATA_PLACA=%s,DATA_VISITA=%s,DATA_ULTIMA_VIS=%s,
                                    URL=%s,COD_ANUNCIO=%s,ANUNCIO_INFO=%s,
                                     VALOR_IMOVEL=%s,VALOR_VENDA=%s,CORRETAGEM=%s,REPASSE_IMOB=%s where ID_IMOB=%s;
    '''

SQL_BUSCA_LISTA_IMOB = 'select ID_IMOB,CATEGORIA,CIDADE,BAIRRO,ENDERECO_IMOVEL,NOME,CELULAR from imoveis left join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP' \
                       ' join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO'


SQL_BUSCA_IMOB_ID ='''select * from imoveis left join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP 
                    join cidade on cidade.ID_CID = imoveis.ID_CIDADE 
                    join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO 
                    left join corretores on imoveis.ID_CORR = corretores.ID_CORR 
                    left join IMOVEL_DESC on imoveis.ID_IMOB = IMOVEL_DESC.ID_IMOB
                    where imoveis.ID_IMOB = %s
'''
 
#Sql da tabela propeitarios

SQL_DELETA_PROPRIETARIO = 'delete from proprietarios where ID_PROP = %s'


SQL_CRIA_PROPRIETARIO = 'INSERT into proprietarios (NOME, CPF_CNPJ, RG_INSC_ETAD, SEXO, ENDERECO, CEP , NUMERO, PESSOA, CODIGO, RAZAO ,' \
                        'TELEFONE, CELULAR, WHATAPPS, EMAIL,CAPITAL, PATRIMONIO, ATIVIDADE, ID_CIDADE, ID_BAIRRO) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_PROPRIETARIO = 'UPDATE proprietarios SET NOME=%s, CPF_CNPJ=%s, RG_INSC_ETAD=%s, SEXO=%s, ENDERECO=%s, CEP=%s , NUMERO=%s, PESSOA=%s, CODIGO=%s, RAZAO=%s ,' \
                        'TELEFONE=%s, CELULAR=%s, WHATAPPS=%s, EMAIL=%s,CAPITAL=%s, PATRIMONIO=%s, ATIVIDADE=%s, ID_CIDADE=%s, ID_BAIRRO=%s where ID_PROP=%s'

SQL_BUSCAR_LISTA_PROP = 'SELECT ID_PROP, NOME, CPF_CNPJ, RG_INSC_ETAD, ENDERECO, TELEFONE, EMAIL, ID_CIDADE, ID_BAIRRO from proprietarios'

SQL_PROP_POR_ID = 'SELECT * from proprietarios ' \
                  'left join cidade on proprietarios.ID_CIDADE = cidade.ID_CID ' \
                  'left join bairro on proprietarios.ID_BAIRRO = bairro.ID_BAIRRO where ID_PROP=%s'


#Sql da tabela corretores
SQL_DELETA_CORRETOR = 'delete from corretores where ID_CORR = %s'

SQL_CRIA_CORRETORES = 'INSERT into corretores (USUARIO,EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_CORRETORES = 'UPDATE corretores SET USUARIO=%s,EMAIL=%s,NOME=%s,CRECI=%s,CELULAR=%s,CPF=%s,ENDERECO=%s,SENHA=%s,ID_CIDADE=%s,ID_BAIRRO=%s  where ID_CORR=%s'

SQL_BUSCA_LISTA_CORRETORES = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO from corretores'

SQL_BUSCA_CORR_ID = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO from corretores where USUARIO=%s or EMAIL=%s'


SQL_BUSCA_CORR_POR_ID = 'SELECT * from corretores ' \
                        'left join cidade on corretores.ID_CIDADE = cidade.ID_CID ' \
                        'left join bairro on corretores.ID_BAIRRO = bairro.ID_BAIRRO where ID_CORR=%s'


#Sql da tabela financeiro
SQL_BUSCA_FIN_ID = 'SELECT * from financeiro where ID_IMOB_FIN = %s'

SQL_DELETA_FIN = 'delete from financeiro where ID_IMOB_FIN = %s'

SQL_CRIA_FIN = 'INSERT into financeiro (HONORARIOS_CORR,PORCENTAGEM_CORR, HONORARIOS_IMOB, PORCENTAGEM_IMOB ,ID_CORR_FIN, ID_IMOB_FIN) values(%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_FIN = 'UPDATE financeiro SET HONORARIOS_CORR=%s,PORCENTAGEM_CORR=%s, HONORARIOS_IMOB=%s, PORCENTAGEM_IMOB=%s, ID_CORR_FIN=%s where ID_FIN=%s'

SQL_LISTA_FIN = 'SELECT financeiro.ID_FIN, financeiro.HONORARIOS_CORR, financeiro.PORCENTAGEM_CORR,financeiro.HONORARIOS_IMOB, financeiro.PORCENTAGEM_IMOB, ' \
                'corretores.NOME, imoveis.ENDERECO_IMOVEL , imoveis.VALOR_VENDA, imoveis.HONORARIOS,financeiro.ID_CORR_FIN FROM financeiro ' \
                'inner join corretores on financeiro.ID_CORR_FIN = ID_CORR ' \
                'inner join imoveis on financeiro.ID_IMOB_FIN = imoveis.ID_IMOB'

SQL_LISTA_FIN_CORR = 'SELECT financeiro.ID_FIN, financeiro.HONORARIOS_CORR, financeiro.PORCENTAGEM_CORR,financeiro.HONORARIOS_IMOB, financeiro.PORCENTAGEM_IMOB, ' \
                'corretores.NOME, imoveis.ENDERECO_IMOVEL , imoveis.VALOR_VENDA, imoveis.HONORARIOS,financeiro.ID_CORR_FIN FROM financeiro ' \
                'inner join corretores on financeiro.ID_CORR_FIN = ID_CORR ' \
                'inner join imoveis on financeiro.ID_IMOB_FIN = imoveis.ID_IMOB where financeiro.ID_CORR_FIN = %s'

#TIPOS
SQL_CRIA_TIPOS = 'INSERT into tipos (ID_TIPO,TIPO) values(%s,%s)'
SQL_LISTA_TIPOS = 'SELECT * FROM tipos'


#CIDADE E BAIRRO
SQL_CRIA_CIDADE = 'INSERT into cidade (ID_CID,CIDADE) values(%s,%s)'
SQL_LISTA_CIDADE = 'SELECT * FROM cidade'
SQL_CRIA_BAIRRO = 'INSERT into bairro (ID_BAIRRO,BAIRRO,CIDADE_ID_CID) values(%s,%s, %s)'
SQL_LISTA_BAIRRO = 'SELECT * FROM bairro inner join cidade on bairro.CIDADE_ID_CID = cidade.ID_CID'


#filtros
SQL_FILTRA_CIDADE = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.ID_CIDADE= %s'

SQL_FILTRA_PROP = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.ID_PROP = %s'

SQL_FILTRA_STATUS = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.STATUS = %s'


SQL_FILTRO_QUARTO ='select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.QUARTOS = %s'

SQL_FILTRO_BANHEIRO = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.BANHEIRO = %s'

SQL_FILTRO_GARAGEM = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.GARAGEM = %s'

SQL_FILTRO_BAIRRO = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.ID_BAIRRO = %s'