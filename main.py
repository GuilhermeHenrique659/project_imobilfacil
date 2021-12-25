from flask import Flask
from dao import imovelDao, cad_proprietario_dao, cad_corretor_dao,tiposDao,ciadadeDao,bairroDao,financeiroDao
from flask_mysqldb import MySQL
from controllers.controller import IndexController
from controllers.CorretorController import CorretorController
from controllers.ProprietarioController import ProprietarioController
from controllers.ImovelController import ImovelController
from controllers.FinanceiroController import FinanceiroController
from controllers.OthersController import OthersController

app = Flask(__name__)
app.secret_key='LP2'
'''
#banco para teste
app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_USER'] = 'b8ab2bd3638752'
app.config['MYSQL_PASSWORD'] = '7627e7de'
app.config['MYSQL_DB'] = 'heroku_7f17bca4c88d1c7'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = MySQL(app)
'''

#banco para produção
app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_USER'] = 'bdbbbc8d2b231a'
app.config['MYSQL_PASSWORD'] = '5deebf3c'
app.config['MYSQL_DB'] = 'heroku_405b84a0ef05c35'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = MySQL(app)




#DAO
Imovel_Dao = imovelDao(db)
Proprietario_dao = cad_proprietario_dao(db)
Corretores_dao = cad_corretor_dao(db)
TiposDao = tiposDao(db)
CidadeDao = ciadadeDao(db)
BairroDao = bairroDao(db)
FinDao = financeiroDao(db)

index_controller = IndexController(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao)

corretor_controller = CorretorController(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao)

proprietario_controller = ProprietarioController(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao)

imovel_controller = ImovelController(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao,TiposDao,FinDao)

financeiro_controller = FinanceiroController(FinDao,Corretores_dao)

other_controller = OthersController(TiposDao,CidadeDao,BairroDao)


#index
app.add_url_rule('/',endpoint='index',view_func=index_controller.index, methods=['GET'])

#tipos,cidade e bairro
#tipo
app.add_url_rule('/novo_tipo', view_func=other_controller.novo_tipo, methods=['POST'])

#cidade
app.add_url_rule('/nova_cidade', view_func=other_controller.nova_cidade, methods=['POST'])
#bairro
app.add_url_rule('/novo_bairro', endpoint='novo_bairro', view_func=other_controller.novo_bairro, methods=['POST'])

#financerio

#atualiza_financeiro
app.add_url_rule('/atualizar_finceiro', endpoint='atualizar_finceiro', view_func=financeiro_controller.atualizar_finceiro, methods=['POST'])

#mostrar lista de vendas
app.add_url_rule('/financeiro', endpoint='financeiro', view_func=financeiro_controller.financeiro, methods=['GET'])

app.add_url_rule('/financeiro/<int:filtro>',view_func=financeiro_controller.finaceiro_filtro)


#visualização do imovel
app.add_url_rule('/view_imovel/<int:id>',view_func=imovel_controller.view_imovel,methods=['GET'])

app.add_url_rule('/resumo_imovel/<int:id>',view_func=imovel_controller.resumo_imovel, methods=['GET'])

#exclui_imovel
app.add_url_rule('/filtro',view_func=imovel_controller.filtro, methods=['POST'])

#exclui_imovel
app.add_url_rule('/deleta_imovel/<int:id>',view_func=imovel_controller.deleta_imovel)

#editar_imovel
app.add_url_rule('/editar_imovel/<int:id>', view_func=imovel_controller.editar_imovel,methods=['GET'])

app.add_url_rule('/atualizar_imovel',view_func=imovel_controller.atualiza_imovel,methods=['POST'])

#criar_imovel
app.add_url_rule('/novo_imovel',view_func=imovel_controller.novo_imovel,methods=['GET'])

app.add_url_rule('/criar_imovel',view_func=imovel_controller.criar_imovel,methods=['POST'])


#Criar Proprietario
app.add_url_rule('/Proprietario', endpoint='Proprietario',view_func=proprietario_controller.rota_proprietario,methods=['GET'])

app.add_url_rule('/cad_prop',endpoint='cad_prop',view_func=proprietario_controller.criar_proprietario, methods=['POST'])

app.add_url_rule('/editar_prop/<int:id>',view_func=proprietario_controller.editar_proprietario, methods=['GET'])

app.add_url_rule('/atualizar_proprietario',endpoint='atualizar_proprietario',view_func=proprietario_controller.atualizar_proprietario, methods=['POST'])

app.add_url_rule('/deletar_prop/<int:id>',view_func=proprietario_controller.deletar_prop)


#corretor
app.add_url_rule('/Corretor',endpoint='Corretor',view_func=corretor_controller.rota_corretor)

app.add_url_rule('/cad_corretor', endpoint='cad_corretor', view_func=corretor_controller.criar_Corretor, methods=['POST'])

app.add_url_rule('/editar_corretor/<int:id>',view_func=corretor_controller.editar_corretor)

app.add_url_rule('/atualizar_corretor', endpoint='atualizar_corretor',view_func=corretor_controller.atualizar_corretor,methods=['POST'])

app.add_url_rule('/deletar_corr/<int:id>', view_func=corretor_controller.deletar_corr)


#login, autenticar, logout#
app.add_url_rule('/login',endpoint='login',view_func=index_controller.login,methods=['GET'])

app.add_url_rule('/autenticar',endpoint='autenticar',view_func=index_controller.autenticar,methods=['POST'])

app.add_url_rule('/logout',endpoint='logout',view_func=index_controller.logout)

if __name__ == '__main__':
    app.run(debug=True)