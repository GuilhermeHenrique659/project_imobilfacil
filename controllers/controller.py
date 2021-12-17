from flask import request, redirect, render_template, session, flash,url_for
import bcrypt

class Controller:
    def __init__(self, Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao):
        self._Imovel_Dao = Imovel_Dao
        self._Proprietario_dao = Proprietario_dao
        self._Corretores_dao = Corretores_dao
        self._CidadeDao = CidadeDao
        self._BairroDao = BairroDao

class IndexController(Controller):
    def __init__(self, Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao):
        super().__init__(Imovel_Dao,Proprietario_dao,Corretores_dao,CidadeDao,BairroDao)

    def index(self):
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/login?proxima=''')
        lista_imob = self._Imovel_Dao.listar()
        lista_prop = self._Proprietario_dao.listar()
        lista_corr = self._Corretores_dao.listar()
        lista_cidades = self._CidadeDao.lista()
        lista_bairro = self._BairroDao.lista()
        return render_template('lista.html', corretores=lista_corr, lista=lista_imob, proprietarios=lista_prop,
                               cidades=lista_cidades, bairros=lista_bairro)

    def login(self):
        proxima = request.args.get('proxima')
        if proxima == None:
            proxima = ''
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return render_template('login.html', proxima=proxima)
        else:
            return redirect('/')

    def autenticar(self):
        usuario = self._Corretores_dao.buscar_por_id(request.form['usuario'])
        if usuario:
            if bcrypt.hashpw(request.form['senha'].encode(), usuario._senha.encode()) == usuario._senha.encode():
                session['usuario_logado'] = request.form['usuario']
                flash(usuario._nome + ' logou com sucesso!')
                proxima_pagina = request.form['proxima']
                return redirect('/{}'.format(proxima_pagina))
            else:
                flash('Senha incorreta!')
                return redirect('/login')
        flash('Usuario não encontrado!')
        return redirect('/login')

    def logout(self):
        session['usuario_logado'] = None
        flash('Usuario deslogado')
        return redirect('/login')
