from flask import request, redirect, render_template, session, flash,url_for
from models import Financeiro
from daofactory import dao
from config import server

class FinanceiroController:

    @server.loggin_required
    def financeiro(self):
        lista_corr = dao.corretor.listar()
        total_vendas = 0
        total_honorarios = 0
        total_honorarios_corr = 0
        total_honorarios_imob = 0
        lista_fin = dao.financeiro.lista()
        for fin in lista_fin:
            total_vendas = total_vendas + fin.valor_total
            total_honorarios = total_honorarios + fin.honorarios_total
            total_honorarios_corr = total_honorarios_corr + fin.get_honorarios_corr()
            total_honorarios_imob = total_honorarios_imob + fin.get_honorarios_imob()
        return render_template('financeiro.html', financeiros=lista_fin, total_vendas=total_vendas,
                               total_honorarios=total_honorarios,
                               total_honorarios_corr=total_honorarios_corr, total_honorarios_imob=total_honorarios_imob,
                               corretores=lista_corr)

                               
    @server.loggin_required
    def atualizar_finceiro(self):
        corretor = request.form['corretor']
        porcentagem_corr = request.form['porcentagem_corr']
        honorarios_corr = request.form['valor_corr']
        porcentagem_imob = request.form['porcentagem_imob']
        honorarios_imob = request.form['valor_imob']
        id = request.form['id']
        financeiro = Financeiro(honorarios_corr, porcentagem_corr, honorarios_imob, porcentagem_imob, corr=corretor,
                                id_fin=id)
        dao.financeiro.salvar(financeiro)
        return redirect('/financeiro')

    @server.loggin_required
    def finaceiro_filtro(self,filtro):
        lista_corr = dao.corretor.listar()
        total_vendas = 0
        total_honorarios = 0
        total_honorarios_corr = 0
        total_honorarios_imob = 0
        lista_fin = dao.financeiro.filtro(filtro)
        for fin in lista_fin:
            total_vendas = total_vendas + fin.valor_total
            total_honorarios = total_honorarios + fin.honorarios_total
            total_honorarios_corr = total_honorarios_corr + fin.get_honorarios_corr()
            total_honorarios_imob = total_honorarios_imob + fin.get_honorarios_imob()
        return render_template('financeiro.html', financeiros=lista_fin, total_vendas=total_vendas,
                               total_honorarios=total_honorarios,
                               total_honorarios_corr=total_honorarios_corr, total_honorarios_imob=total_honorarios_imob,
                               corretores=lista_corr)