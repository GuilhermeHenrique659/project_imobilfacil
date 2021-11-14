
#Sql da tabela imoveis
SQL_CRIA_IMOVEL = 'INSERT into imoveis (ID_CORR, ID_PROP, ID_TIPO, FINALIDADE, ID_CIDADE, ID_BAIRRO, ENDERECO_IMOVEL, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS, BANHEIRO, QUARTOS, GARAGEM)' \
                  ' values (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)'

SQL_DELETA_IMOVEL = 'delete from imoveis where ID_IMOB = %s'

SQL_ATUALIZA_IMOVEIS = 'UPDATE imoveis SET ID_CORR=%s,ID_PROP=%s,ID_TIPO=%s,FINALIDADE=%s,ID_CIDADE=%s,ID_BAIRRO=%s,ENDERECO_IMOVEL=%s, AREA=%s, DETALHES=%s,'\
                       'VALOR_IMOVEL=%s,VALOR_VENDA=%s,STATUS=%s, PORCENTAGEM=%s, HONORARIOS=%s,BANHEIRO=%s,QUARTOS=%s, GARAGEM=%s where ID_IMOB=%s'

SQL_BUSCA_LISTA_IMOB = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP  inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                       'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO'

SQL_BUSCA_IMOB_ID = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP ' \
                    'inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE ' \
                    'join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO ' \
                    'inner join corretores on imoveis.ID_CORR = corretores.ID_CORR ' \
                    'where imoveis.ID_IMOB = %s'


#Sql da tabela propeitarios

SQL_DELETA_PROPRIETARIO = 'delete from proprietarios where ID_PROP = %s'


SQL_CRIA_PROPRIETARIO = 'INSERT into proprietarios (NOME, CPF, RG, ENDERECO, TELEFONE, EMAIL,ID_CIDADE, ID_BAIRRO) values (%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_PROPRIETARIO = 'UPDATE proprietarios SET NOME=%s, CPF=%s, RG=%s, ENDERECO=%s, TELEFONE=%s, EMAIL=%s, ID_CIDADE=%s, ID_BAIRRO=%s   where ID_PROP=%s'

SQL_BUSCAR_LISTA_PROP = 'SELECT ID_PROP, NOME, CPF, RG, ENDERECO, TELEFONE, EMAIl, ID_CIDADE, ID_BAIRRO from proprietarios'

SQL_PROP_POR_ID = 'select * from projeto_db.proprietarios ' \
                  'inner join projeto_db.cidade on proprietarios.ID_CIDADE = cidade.ID_CID ' \
                  'inner join projeto_db.bairro on proprietarios.ID_BAIRRO = bairro.ID_BAIRRO where ID_PROP=%s'


#Sql da tabela corretores
SQL_DELETA_CORRETOR = 'delete from corretores where ID_CORR = %s'

SQL_CRIA_CORRETORES = 'INSERT into corretores (USUARIO,EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_CORRETORES = 'UPDATE corretores SET USUARIO=%s,EMAIL=%s,NOME=%s,IMOBIL=%s,CRECI=%s,CELULAR=%s,CPF=%s,ENDERECO=%s,SENHA=%s,ID_CIDADE=%s,ID_BAIRRO=%s  where ID_CORR=%s'

SQL_BUSCA_LISTA_CORRETORES = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO from corretores'

SQL_BUSCA_CORR_ID = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA,ID_CIDADE, ID_BAIRRO from corretores where USUARIO=%s'

SQL_BUSCA_CORR_POR_ID = 'SELECT * from projeto_db.corretores ' \
                        ' join projeto_db.cidade on corretores.ID_CIDADE = cidade.ID_CID ' \
                        ' join projeto_db.bairro on corretores.ID_BAIRRO = bairro.ID_BAIRRO where ID_CORR=%s'


#Sql da tabela corretores

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