from flask import Flask, request, redirect, render_template, session, flash
from models import Usuario, imovel, Proprietario, Corretores
from dao import imovelDao, cad_proprietario_dao, cad_corretor_dao
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key='LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'projeto_db'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)

#DAO
Imovel_Dao = imovelDao(db)
Proprietario_dao = cad_proprietario_dao(db)
Corretores_dao = cad_corretor_dao(db)

#index
@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=''')
    lista_imob = Imovel_Dao.listar()
    lista_prop = Proprietario_dao.listar()
    lista_corr = Corretores_dao.listar()
    return render_template('lista.html', corretores=lista_corr, imoveis=lista_imob, proprietarios=lista_prop)


#criar_imovel
@app.route('/novo_imovel')
def novo_imovel():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_imovel')
    lista_prop = Proprietario_dao.listar()
    lista_corr = Corretores_dao.listar()
    return render_template('novo_imovel.html', proprietarios=lista_prop, corretores=lista_corr)

@app.route('/criar_imovel', methods=['POST'])
def criar_imovel():
    sigla = request.form['sigla']
    tipo =  request.form['tipo']
    finalidade = request.form['finalidade']
    bairro = request.form['bairro']
    quadra = request.form['quadra']
    lote = request.form['lote']
    area = request.form['area']
    descriacao = request.form['detalhes']
    valor = request.form['valor']
    status = request.form['status']
    porcentagem = request.form['porcentagem']
    proprietario = request.form['proprietario']
    corretor = request.form['corretor']
    Imovel = imovel(sigla,tipo,finalidade,bairro,quadra,lote,area,descriacao,valor,status,porcentagem,proprietario,corretor)
    Imovel_Dao.salvar(Imovel)
    return redirect('/')

#Criar Proprietario
@app.route('/Proprietario')
def rota_proprietario():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_proprietario.html')
    return render_template('novo_proprietario.html')


@app.route('/cad_prop', methods=['POST'])
def criar_proprietario():
    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email  = request.form['email']
    proprietario = Proprietario(nome,cpf,rg,endereco,telefone,email)
    Proprietario_dao.salvar(proprietario)
    return redirect('/')

#corretor
@app.route('/Corretor')
def rota_corretor():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_proprietario.html')
    return render_template('novo_corretor.html')


@app.route('/cad_corretor', methods=['POST'])
def criar_Corretor():
    usuario = request.form['usuario_corr']
    email = request.form['email_corr']
    nome = request.form['nome_corr']
    imobil = request.form['imobil_corr']
    creci = request.form['creci_corr']
    celular = request.form['celular_corr']
    cpf = request.form['cpf_corr']
    endereco = request.form['endereco_corr']
    senha = request.form['senha_corr']
    corretor = Corretores(usuario,email,nome,imobil,creci,celular,cpf,endereco,senha)
    Corretores_dao.salvar(corretor)
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
    usuario = Corretores_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario._senha == request.form['senha']:
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