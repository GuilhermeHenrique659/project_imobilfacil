from flask import request, redirect, render_template, session, flash,url_for
import bcrypt
from daofactory import dao
from config import server


class IndexController():

    @server.loggin_required
    def index(self):
        corretores = dao.corretor.listar()
        return render_template('lista_corr.html',corretores=corretores)

    def login(self):
        proxima = request.args.get('proxima')
        if proxima == None:
            proxima = ''
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return render_template('login.html', proxima=proxima)
        else:
            return redirect('/')

    def autenticar(self):
        usuario = dao.corretor.buscar_por_id(request.form['usuario'])
        if usuario:
            if bcrypt.hashpw(request.form['senha'].encode(), usuario._senha.encode()) == usuario._senha.encode():
                session['usuario_logado'] = request.form['usuario']
                session['nome_usuario'] = usuario._nome
                session['usuario_id'] = usuario._id_corr
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
