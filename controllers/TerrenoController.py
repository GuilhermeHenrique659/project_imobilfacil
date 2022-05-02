from config import server
from flask import redirect, url_for, render_template, request
from daofactory import dao
from models import Imovel

class TerrenoController:
    
    @server.loggin_required
    def novo_terreno(self):
        lista_bairro = dao.bairro.lista()
        lista_cidade = dao.cidade.lista()
        lista_corretor = dao.corretor.listar()
        lista_proprietario = dao.proprietario.listar()
        return render_template('novo_terreno.html',proprietarios=lista_proprietario,
                            corretores=lista_corretor,cidades=lista_cidade, bairros=lista_bairro)

    @server.loggin_required
    def criar_terreno(self):
        formdata = request.form
        terreno = Imovel('Terreno',formdata['forma'],formdata['ladoesq'],formdata['ladodir'],formdata['ladofrente'],formdata['ladofundo'],formdata['metros'],formdata['topografia'],
                        formdata['areautil'],formdata['areacons'],formdata['edicula'],formdata['cidades'],formdata['bairros'],formdata['endereco'],formdata['numero'],
                        formdata['cep'],formdata['valor'],formdata['porcentagem'],formdata['valorvenda'],formdata['repasse'],formdata['placa'],formdata['url'],formdata['dataplaca'],
                        formdata['datavis'],formdata['dataultvis'],formdata['codanun'],formdata['infoanun'],formdata['inflocal'],formdata['infoarea'],formdata['proprietario'],formdata['corretor'])
        dao.imovel.salvar(terreno)
        return redirect(url_for('index'))