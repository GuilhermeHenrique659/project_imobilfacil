from controllers.controller import *
from models import Financeiro

class FinanceiroController:
    def __init__(self, FinDao, Corretores_dao):
        self._Corretores_dao = Corretores_dao
        self._FinDao = FinDao

    def financeiro(self):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=/financeiro')
        lista_corr = self._Corretores_dao.listar()
        total_vendas = 0
        total_honorarios = 0
        total_honorarios_corr = 0
        total_honorarios_imob = 0
        lista_fin = self._FinDao.lista()
        for fin in lista_fin:
            total_vendas = total_vendas + fin.valor_total
            total_honorarios = total_honorarios + fin.honorarios_total
            total_honorarios_corr = total_honorarios_corr + fin.get_honorarios_corr()
            total_honorarios_imob = total_honorarios_imob + fin.get_honorarios_imob()
        return render_template('financeiro.html', financeiros=lista_fin, total_vendas=total_vendas,
                               total_honorarios=total_honorarios,
                               total_honorarios_corr=total_honorarios_corr, total_honorarios_imob=total_honorarios_imob,
                               corretores=lista_corr)

    def atualizar_finceiro(self):
        corretor = request.form['corretor']
        porcentagem_corr = request.form['porcentagem_corr']
        honorarios_corr = request.form['valor_corr']
        porcentagem_imob = request.form['porcentagem_imob']
        honorarios_imob = request.form['valor_imob']
        id = request.form['id']
        financeiro = Financeiro(honorarios_corr, porcentagem_corr, honorarios_imob, porcentagem_imob, corr=corretor,
                                id_fin=id)
        self._FinDao.salvar(financeiro)
        return redirect('/financeiro')

    def finaceiro_filtro(self,filtro):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=/financeiro')
        lista_corr = self._Corretores_dao.listar()
        total_vendas = 0
        total_honorarios = 0
        total_honorarios_corr = 0
        total_honorarios_imob = 0
        lista_fin = self._FinDao.filtro(filtro)
        for fin in lista_fin:
            total_vendas = total_vendas + fin.valor_total
            total_honorarios = total_honorarios + fin.honorarios_total
            total_honorarios_corr = total_honorarios_corr + fin.get_honorarios_corr()
            total_honorarios_imob = total_honorarios_imob + fin.get_honorarios_imob()
        return render_template('financeiro.html', financeiros=lista_fin, total_vendas=total_vendas,
                               total_honorarios=total_honorarios,
                               total_honorarios_corr=total_honorarios_corr, total_honorarios_imob=total_honorarios_imob,
                               corretores=lista_corr)