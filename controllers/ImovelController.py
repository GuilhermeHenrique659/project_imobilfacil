from controllers.controller import *
from models import Imovel, Financeiro

class ImovelController(Controller):
    def __init__(self,Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao,TiposDao,FinDao):
        super().__init__(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao)
        self._TiposDao = TiposDao
        self._FinDao = FinDao

    def novo_imovel(self):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=novo_imovel')
        lista_prop = self._Proprietario_dao.listar()
        lista_corr = self._Corretores_dao.listar()
        lista_tipo = self._TiposDao.lista()
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        return render_template('novo_imovel.html', proprietarios=lista_prop, corretores=lista_corr,
                               tipos=lista_tipo, cidades=lista_cidades, bairros=lista_bairro)

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
        id = self._Imovel_Dao.salvar(imovel)
        imovel.set_id(id)
        self.cria_financeiro(imovel)

        return redirect('/')

    def editar_imovel(self, id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=''')
        Imovel = self._Imovel_Dao.busca_imob_id(id)
        lista_prop = self._Proprietario_dao.listar()
        lista_corr = self._Corretores_dao.listar()
        lista_tipo = self._TiposDao.lista()
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        return render_template('editar_imovel.html', imovel=Imovel, proprietarios=lista_prop, corretores=lista_corr,
                               tipos=lista_tipo, cidades=lista_cidades, bairros=lista_bairro)

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
        self._Imovel_Dao.salvar(imovel)
        self.cria_financeiro(imovel)
        return redirect('/')

    def deleta_imovel(self,id):
        self._Imovel_Dao.deletar_imob(id)
        return redirect('/')

    def resumo_imovel(self,id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=view_imovel/<int:id>')
        imovel = self._Imovel_Dao.busca_imob_id(id)
        return render_template('resumo_imovel.html', imovel=imovel)

    def view_imovel(self,id):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=view_imovel/<int:id>')
        imovel = self._Imovel_Dao.busca_imob_id(id)
        return render_template('view_imovel.html', imovel=imovel)

    def filtro(self):
        filtro = request.form['filtro']
        id = request.form[filtro]
        lista_imob = self._Imovel_Dao.filtra(id, filtro)
        if len(lista_imob) == 0:
            flash("Nao foi encontrado nenhum imovel com esse filtro!")
            return redirect('/')
        lista_prop = self._Proprietario_dao.listar()
        lista_corr = self._Corretores_dao.listar()
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        return render_template('lista.html', corretores=lista_corr, lista=lista_imob, proprietarios=lista_prop,
                               cidades=lista_cidades, bairros=lista_bairro)

    def cria_financeiro(self,imovel):
        fin = self._FinDao.pocurar(imovel._imob_id)
        if fin:
            if imovel._status == "Vendido":
                financeiro = Financeiro((imovel._honorarios * fin.get_porcetagem_corr()), fin._porcentagem_corr,
                                        (imovel._honorarios * fin.get_porcetagem_imob()),
                                        fin._porcentagem_imob, imob=imovel._imob_id, corr=imovel._corretor,
                                        id_fin=fin._id_fin)
                self._FinDao.salvar(financeiro)
                return
            else:
                self._FinDao.deletar(imovel._imob_id)
        financeiro = Financeiro((imovel.honorarios / 2), 50, (imovel.honorarios / 2), 50, imob=imovel._imob_id,
                                corr=imovel._corretor)
        if imovel._status == 'Vendido':
            self._FinDao.salvar(financeiro)
        else:
            return
