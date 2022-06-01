import MySQLdb
from config import server
from flask import redirect, url_for, render_template, request,flash
from daofactory import dao
from models import Imovel

UNIQUE_ERROR_CODE = 1062

class TerrenoController:

    def take_message_error(self, error):
        error_message = error.lower().replace("duplicate entry",'').replace("for key",'no campo')
        return error_message

    @server.loggin_required
    def novo_terreno(self):
        lista_cidade = dao.cidade.lista()
        return render_template('novo_terreno.html',cidades=lista_cidade)

    @server.loggin_required
    def criar_terreno(self):
        formdata = request.form
        placa = formdata.get('placa')
        if not placa:
            placa = 0
        terreno = Imovel('Terreno',formdata['forma'],formdata['ladoesq'],formdata['ladodir'],formdata['ladofrente'],formdata['ladofundo'],formdata['metros'],formdata['topografia'],
                        formdata['areautil'],formdata['areacons'],formdata['edicula'],formdata['cidades'],formdata['bairros'],formdata['endereco'],formdata['numero'],
                        formdata['cep'],formdata['valor'],formdata['porcentagem'],formdata['valorvenda'],formdata['repasse'],placa,formdata['url'],formdata['dataplaca'],
                        formdata['datavis'],formdata['dataultvis'],formdata['codanun'],formdata['infoanun'],formdata['inflocal'],formdata['infoarea'],formdata['proprietario'],formdata['corretor'])
        result = dao.imovel.salvar(terreno)
        if isinstance(result,MySQLdb.IntegrityError) == tuple and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('novo_terreno'))
        return redirect(url_for('index'))

    
    @server.loggin_required
    def editar_terreno(self,id):
        terreno = dao.imovel.busca_imob_id(id)
        lista_cidade = dao.cidade.lista()
        return render_template('editar_terreno.html',cidades=lista_cidade, terreno = terreno )

    @server.loggin_required
    def atualiza_terreno(self):
        id = request.args['id_terr']
        formdata = request.form
        placa = formdata.get('placa')
        if not placa:
            placa = 0
        terreno = Imovel('Terreno',formdata['forma'],formdata['ladoesq'],formdata['ladodir'],formdata['ladofrente'],formdata['ladofundo'],formdata['metros'],formdata['topografia'],
                        formdata['areautil'],formdata['areacons'],formdata['edicula'],formdata['cidades'],formdata['bairros'],formdata['endereco'],formdata['numero'],
                        formdata['cep'],formdata['valor'],formdata['porcentagem'],formdata['valorvenda'],formdata['repasse'],placa,formdata['url'],formdata['dataplaca'],
                        formdata['datavis'],formdata['dataultvis'],formdata['codanun'],formdata['infoanun'],formdata['inflocal'],formdata['infoarea'],formdata['proprietario'],formdata['corretor'],imob_id=id)
        result = dao.imovel.salvar(terreno)
        if isinstance(result,MySQLdb.IntegrityError) and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('editar_terreno', id=id))
        return redirect(url_for('index'))