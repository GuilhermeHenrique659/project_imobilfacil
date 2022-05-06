from flask import request, redirect, render_template, session, flash,url_for
from models import Imovel, Financeiro, Descricao_imovel
from daofactory import dao
from config import server

UNIQUE_ERROR_CODE = 1062

class ImovelController():

    def take_message_error(self, error):
        error_message = error.lower().replace("duplicate entry",'').replace("for key",'no campo')
        return error_message


    @server.loggin_required
    def novo_imovel(self):
        lista_prop = dao.proprietario.listar()
        lista_corr = dao.corretor.listar()
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        return render_template('novo_imovel.html', proprietarios=lista_prop, corretores=lista_corr,
                            cidades=lista_cidades, bairros=lista_bairro)

    @server.loggin_required
    def criar_imovel(self):
        imovel_form = request.form
        placa = imovel_form.get('placa')
        if not placa:
            placa = 0
        imovel = Imovel('Imovel',imovel_form['forma'],imovel_form['ladoesq'],imovel_form['ladodir'],imovel_form['ladofrente'],imovel_form['ladofundo'],imovel_form['metros'],imovel_form['topografia'],
                        imovel_form['areautil'],imovel_form['areacons'],imovel_form['edicula'],imovel_form['cidades'],imovel_form['bairros'],imovel_form['endereco'],imovel_form['numero'],
                        imovel_form['cep'],imovel_form['valor'],imovel_form['porcentagem'],imovel_form['valorvenda'],imovel_form['repasse'],placa,imovel_form['url'],imovel_form['dataplaca'],
                        imovel_form['datavis'],imovel_form['dataultvis'],imovel_form['codanun'],imovel_form['infoanun'],imovel_form['inflocal'],imovel_form['infoarea'],imovel_form['proprietario'],imovel_form['corretor'],
                        tipo=imovel_form['tipo'],subtipo=imovel_form['subtipo'])
        
        result = dao.imovel.salvar(imovel)
        if type(result) == tuple and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('novo_imovel'))
        imovel_desc = Descricao_imovel(imovel_form['vagas'],imovel_form['banheiro'],imovel_form['suites'],imovel_form['dormitorios'],imovel_form['area_serve'],imovel_form['copa'],imovel_form['desc_edicula'],
                                        imovel_form['lareira'],imovel_form['portao_elec'],imovel_form['hidromsg'],imovel_form['piso'],imovel_form['sacada'],imovel_form['sala_vist'],imovel_form['sala_estar'],
                                        imovel_form['sotao'],imovel_form['amarinho'],imovel_form['cozinha'],imovel_form['escritorio'],imovel_form['lavabo'],imovel_form['sala_jantar'],imovel_form['varanda'],imovel_form['claraboia'],
                                        imovel_form['dep_empregada'],imovel_form['garage'],imovel_form['living_room'],imovel_form['quintal'],imovel_form['sala_tv'],imovel_form['w_c_empregada'],imovel_form['closet'],
                                        imovel_form['despensa'],imovel_form['churrasqueira'],imovel_form['portaria_24h'],imovel_form['salao_festa'],imovel_form['jd_inverno'],imovel_form['quadra'],imovel_form['piscina'],
                                        imovel_form['sauna'],imovel_form['entrada_ind'],imovel_form['quadra_tenis'],imovel_form['playground'],imovel_form['sala_ginastica'],result)
        dao.imovel.salvar_desc(imovel_desc)
        return redirect(url_for('index'))

    @server.loggin_required
    def editar_imovel(self, id):
        Imovel = dao.imovel.busca_imob_id(id)
        lista_prop = dao.proprietario.listar()
        lista_corr = dao.corretor.listar()
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        return render_template('editar_imovel.html', imovel=Imovel, proprietarios=lista_prop, corretores=lista_corr,
                               cidades=lista_cidades, bairros=lista_bairro)

    @server.loggin_required
    def atualiza_imovel(self):
        imovel_form = request.form
        placa = imovel_form.get('placa')
        id_imob = request.args['id_imob']
        id_desc = request.args['id_desc']
        if not placa:
            placa = 0
        imovel = Imovel('Imovel',imovel_form['forma'],imovel_form['ladoesq'],imovel_form['ladodir'],imovel_form['ladofrente'],imovel_form['ladofundo'],imovel_form['metros'],imovel_form['topografia'],
                        imovel_form['areautil'],imovel_form['areacons'],imovel_form['edicula'],imovel_form['cidades'],imovel_form['bairros'],imovel_form['endereco'],imovel_form['numero'],
                        imovel_form['cep'],imovel_form['valor'],imovel_form['porcentagem'],imovel_form['valorvenda'],imovel_form['repasse'],placa,imovel_form['url'],imovel_form['dataplaca'],
                        imovel_form['datavis'],imovel_form['dataultvis'],imovel_form['codanun'],imovel_form['infoanun'],imovel_form['inflocal'],imovel_form['infoarea'],imovel_form['proprietario'],imovel_form['corretor'],
                        tipo=imovel_form['tipo'],subtipo=imovel_form['subtipo'],imob_id=id_imob)
        
        result = dao.imovel.salvar(imovel)
        if type(result) == tuple and result.args[0] == UNIQUE_ERROR_CODE:
            flash(self.take_message_error(result.args[1]) +' ja está sendo ultilizado')
            return redirect(url_for('editar_imovel', id=id_imob))
        imovel_desc = Descricao_imovel(imovel_form['vagas'],imovel_form['banheiro'],imovel_form['suites'],imovel_form['dormitorios'],imovel_form['area_serve'],imovel_form['copa'],imovel_form['desc_edicula'],
                                        imovel_form['lareira'],imovel_form['portao_elec'],imovel_form['hidromsg'],imovel_form['piso'],imovel_form['sacada'],imovel_form['sala_vist'],imovel_form['sala_estar'],
                                        imovel_form['sotao'],imovel_form['amarinho'],imovel_form['cozinha'],imovel_form['escritorio'],imovel_form['lavabo'],imovel_form['sala_jantar'],imovel_form['varanda'],imovel_form['claraboia'],
                                        imovel_form['dep_empregada'],imovel_form['garage'],imovel_form['living_room'],imovel_form['quintal'],imovel_form['sala_tv'],imovel_form['w_c_empregada'],imovel_form['closet'],
                                        imovel_form['despensa'],imovel_form['churrasqueira'],imovel_form['portaria_24h'],imovel_form['salao_festa'],imovel_form['jd_inverno'],imovel_form['quadra'],imovel_form['piscina'],
                                        imovel_form['sauna'],imovel_form['entrada_ind'],imovel_form['quadra_tenis'],imovel_form['playground'],imovel_form['sala_ginastica'],result, id_desc=id_desc)
        dao.imovel.salvar_desc(imovel_desc)
        return redirect(url_for('index'))

    @server.loggin_required
    def deleta_imovel(self,id):
        dao.imovel.deletar_imob(id)
        return redirect('/')

    @server.loggin_required
    def resumo_imovel(self,id):
        imovel = dao.imovel.busca_imob_id(id)
        return render_template('resumo_imovel.html', imovel=imovel)

    @server.loggin_required
    def view_imovel(self,id):
        imovel = dao.imovel.busca_imob_id(id)
        return render_template('view_imovel.html', imovel=imovel)


    @server.loggin_required
    def filtro(self):
        filtro = request.form['filtro']
        id = request.form[filtro]
        lista_imob = dao.imovel.filtra(id, filtro)
        if len(lista_imob) == 0:
            flash("Nao foi encontrado nenhum imovel com esse filtro!")
            return redirect('/')
        lista_prop = dao.proprietario.listar()
        lista_corr = dao.corretor.listar()
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        return render_template('lista.html', corretores=lista_corr, lista=lista_imob, proprietarios=lista_prop,
                               cidades=lista_cidades, bairros=lista_bairro)


    @server.loggin_required
    def cria_financeiro(self,imovel):
        fin = dao.financeiro.pocurar(imovel._imob_id)
        if fin:
            if imovel._status == "Vendido":
                financeiro = Financeiro((imovel._honorarios * fin.get_porcetagem_corr()), fin._porcentagem_corr,
                                        (imovel._honorarios * fin.get_porcetagem_imob()),
                                        fin._porcentagem_imob, imob=imovel._imob_id, corr=imovel._corretor,
                                        id_fin=fin._id_fin)
                dao.financeiro.salvar(financeiro)
                return
            else:
                dao.financeiro.deletar(imovel._imob_id)
        financeiro = Financeiro((imovel.honorarios / 2), 50, (imovel.honorarios / 2), 50, imob=imovel._imob_id,
                                corr=imovel._corretor)
        if imovel._status == 'Vendido':
            dao.financeiro.salvar(financeiro)
        else:
            return
