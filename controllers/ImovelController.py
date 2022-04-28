from flask import request, redirect, render_template, session, flash,url_for
from models import Imovel, Financeiro
from daofactory import dao
from config import server

class ImovelController():

    @server.loggin_required
    def novo_imovel(self):
        lista_prop = dao.proprietario.listar()
        lista_corr = dao.corretor.listar()
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        lista_tipo = dao.tipo.lista()
        return render_template('novo_imovel.html', proprietarios=lista_prop, corretores=lista_corr,
                               tipos=lista_tipo, cidades=lista_cidades, bairros=lista_bairro)

    @server.loggin_required
    def criar_imovel(self):
        tipo = request.form['tipos']
        finalidade = request.form['finalidade']
        cidade = request.form['cidades']
        bairro = request.form['bairros']
        endereco = request.form['endereco']
        area = request.form['area']
        descriacao = request.form['detalhes']
        valor = request.form['valor']
        status = request.form['status']
        porcentagem = request.form['porcentagem']
        proprietario = request.form['proprietario']
        corretor = request.form['corretor']
        banheiro = request.form['banheiro']
        quartos = request.form['quartos']
        garagem = request.form['garagem']
        imovel = Imovel(tipo, finalidade, cidade, bairro, endereco, area, descriacao, valor, status, porcentagem,
                        proprietario, corretor,
                        banheiro=banheiro, quartos=quartos, garagem=garagem)
        id = dao.imovel.salvar(imovel)
        imovel.set_id(id)
        self.cria_financeiro(imovel)

        return redirect('/')

    @server.loggin_required
    def editar_imovel(self, id):
        Imovel = dao.imovel.busca_imob_id(id)
        lista_prop = dao.proprietario.listar()
        lista_corr = dao.corretor.listar()
        lista_cidades = dao.cidade.lista()
        lista_bairro = dao.bairro.lista()
        lista_tipo = dao.tipo.lista()
        return render_template('editar_imovel.html', imovel=Imovel, proprietarios=lista_prop, corretores=lista_corr,
                               tipos=lista_tipo, cidades=lista_cidades, bairros=lista_bairro)

    @server.loggin_required
    def atualiza_imovel(self):
        tipo = request.form['tipos']
        finalidade = request.form['finalidade']
        cidade = request.form['cidades']
        bairro = request.form['bairros']
        endereco = request.form['endereco']
        area = request.form['area']
        descriacao = request.form['detalhes']
        valor = request.form['valor']
        status = request.form['status']
        porcentagem = request.form['porcentagem']
        proprietario = request.form['proprietario']
        corretor = request.form['corretor']
        banheiro = request.form['banheiro']
        quartos = request.form['quartos']
        garagem = request.form['garagem']
        id = request.form['id']
        if corretor == 'None':
            corretor = None
        imovel = Imovel(tipo, finalidade, cidade, bairro, endereco, area, descriacao, valor, status, porcentagem,
                        proprietario, corretor,
                        banheiro=banheiro, quartos=quartos, garagem=garagem, imob_id=id)
        dao.imovel.salvar(imovel)
        self.cria_financeiro(imovel)
        return redirect('/')

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
