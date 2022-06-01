from config import server
from controllers.controllerfactory import controllers


class Routes:
    def __init__(self) -> None:
         #index
        server.app.add_url_rule('/',endpoint='index',view_func=controllers.system.index, methods=['GET'])

#cidade e bairro
#cidade
        server.app.add_url_rule('/nova_cidade', endpoint='nova_cidade',view_func=controllers.orthers.nova_cidade, methods=['POST'])
#bairro
        server.app.add_url_rule('/novo_bairro', endpoint='novo_bairro', view_func=controllers.orthers.novo_bairro, methods=['POST'])

#financerio

#visualização do imovel
        server.app.add_url_rule('/view_imovel/<int:id>', endpoint='view_imovel',view_func=controllers.imovel.view_imovel,methods=['GET'])

        server.app.add_url_rule('/resumo_imovel/<int:id>',endpoint='resumo_imovel',view_func=controllers.imovel.resumo_imovel, methods=['GET'])

        server.app.add_url_rule('/filtro', endpoint='filtro' ,view_func=controllers.imovel.filtro, methods=['POST'])

#exclui_imovel
        server.app.add_url_rule('/deleta_imovel/<int:id>', endpoint='deleta_imovel',view_func=controllers.imovel.deleta_imovel)

#editar_imovel
        server.app.add_url_rule('/editar_imovel/<int:id>',endpoint='editar_imovel', view_func=controllers.imovel.editar_imovel,methods=['GET'])

        server.app.add_url_rule('/atualizar_imovel',endpoint='atualizar_imovel' ,view_func=controllers.imovel.atualiza_imovel,methods=['POST'])

        server.app.add_url_rule('/editar_terreno/<int:id>', endpoint='editar_terreno', view_func=controllers.terreno.editar_terreno)

        server.app.add_url_rule('/atualiza_terreno',endpoint='atualiza_terreno', view_func=controllers.terreno.atualiza_terreno, methods=['POST'])

#criar_imovel
        server.app.add_url_rule('/novo_imovel', endpoint='novo_imovel'  ,view_func=controllers.imovel.novo_imovel,methods=['GET'])

        server.app.add_url_rule('/criar_imovel', endpoint='cria_imovel' , view_func=controllers.imovel.criar_imovel,methods=['POST'])

        server.app.add_url_rule('/novo_terreno', endpoint='novo_terreno', view_func=controllers.terreno.novo_terreno)

        server.app.add_url_rule('/criar_terreno', endpoint='criar_terreno', view_func=controllers.terreno.criar_terreno, methods=['POST'])


#Criar Proprietario
        server.app.add_url_rule('/Proprietario', endpoint='Proprietario',view_func=controllers.proprietario.rota_proprietario,methods=['GET'])

        server.app.add_url_rule('/find_prop_by_name',endpoint='find_prop_by_name',view_func = controllers.proprietario.find_prop_by_nome,methods=['POST','GET'])

        server.app.add_url_rule('/cad_prop',endpoint='cad_prop',view_func=controllers.proprietario.criar_proprietario, methods=['POST'])

        server.app.add_url_rule('/editar_prop/<int:id>', endpoint='editar_prop' ,view_func=controllers.proprietario.editar_proprietario, methods=['GET'])

        server.app.add_url_rule('/atualizar_proprietario',endpoint='atualizar_proprietario',view_func=controllers.proprietario.atualizar_proprietario, methods=['POST'])

        server.app.add_url_rule('/deletar_prop/<int:id>', endpoint='delete_prop' ,view_func=controllers.proprietario.deletar_prop)


#corretor
        server.app.add_url_rule('/Corretor',endpoint='Corretor',view_func=controllers.corretor.rota_corretor)

        server.app.add_url_rule('/find_cor_by_name',endpoint='find_cor_by_name',view_func = controllers.corretor.find_by_name,methods=['POST','GET'])

        server.app.add_url_rule('/cad_corretor', endpoint='cad_corretor', view_func=controllers.corretor.criar_Corretor, methods=['POST'])

        server.app.add_url_rule('/editar_corretor/<int:id>', endpoint='editar_corretor' ,view_func=controllers.corretor.editar_corretor)

        server.app.add_url_rule('/atualizar_corretor', endpoint='atualizar_corretor',view_func=controllers.corretor.atualizar_corretor,methods=['POST'])

        server.app.add_url_rule('/deletar_corr/<int:id>', endpoint='deletar_corr', view_func=controllers.corretor.deletar_corr)


#login, autenticar, logout#
        server.app.add_url_rule('/login',endpoint='login',view_func=controllers.system.login,methods=['GET'])

        server.app.add_url_rule('/autenticar',endpoint='autenticar',view_func=controllers.system.autenticar,methods=['POST'])

        server.app.add_url_rule('/logout',endpoint='logout',view_func=controllers.system.logout)
