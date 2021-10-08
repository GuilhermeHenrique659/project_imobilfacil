from flask import Flask, request, redirect, render_template, session, flash
from models import Usuario, imovel
from dao import imovelDao
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key='LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'projeto_db'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
Imovel_Dao = imovelDao(db)



usuario1 = Usuario('guilherme','Guilherme Henrique','naomecha')
usuario2 = Usuario('teste','Teste1','123456')

usuarios = {usuario1._id:usuario1 , usuario2._id:usuario2}

lista_user=[usuario1,usuario2]

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=''')
    return render_template('lista.html', corretores=lista_user)


#criar_imovel
@app.route('/novo_imovel')
def novo_imovel():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_imovel')
    return render_template('novo_imovel.html')

@app.route('/criar_imovel', methods=['POST'])
def criar_imovel():
    sigla = request.form['sigla']
    tipo =  request.form['tipo']
    finalidade = request.form['finalidade']
    bairro = request.form['bairro']
    quadra = request.form['quadra']
    lote = request.form['lote']
    valor = request.form['valor']
    status = request.form['status']
    porcentagem = request.form['porcentagem']
    honorarios = request.form['honorarios']
    proprietario = request.form['proprietario']
    Imovel = imovel(sigla,tipo,finalidade,bairro,quadra,lote,valor,status,porcentagem,honorarios,proprietario)
    Imovel_Dao.salvar(Imovel)
    return redirect('/')


#login, autenticar, logout#

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        print(usuario._senha, usuario._id, usuario._nome)
        if usuario.get_senha() == request.form['senha']:
            session['usuario_logado']=request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect('/{}'.format(proxima_pagina))
        else:
            flash('Senha incorreta!')
            return redirect('/login')
    flash('Usuario incorreto!')
    return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario deslogado')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)