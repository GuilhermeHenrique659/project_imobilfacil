from flask import Flask, request, redirect, render_template, session, flash,url_for
from models import Imovel, Proprietario, Corretores,Tipo,Cidade,Bairro
from dao import imovelDao, cad_proprietario_dao, cad_corretor_dao,tiposDao,ciadadeDao,bairroDao
from flask_mysqldb import MySQL
from validacao import imovel_valida
import bcrypt

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
TiposDao = tiposDao(db)
CidadeDao = ciadadeDao(db)
BairroDao = bairroDao(db)

#index
@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=''')
    lista_imob = Imovel_Dao.listar()
    lista_prop = Proprietario_dao.listar()
    lista_corr = Corretores_dao.listar()
    lista_cidades = CidadeDao.lista()

    return render_template('lista.html', corretores=lista_corr, lista=lista_imob, proprietarios=lista_prop, cidades=lista_cidades)

#tipos,cidade e bairro


#tipo
@app.route('/novo_tipo', methods=['POST'])
def novo_tipo():
    Tipo_nome= request.form['tipo']
    tipo = Tipo(Tipo_nome)
    TiposDao.salvar(tipo)
    return redirect('/novo_imovel')
#cidade
@app.route('/nova_cidade', methods=['POST'])
def nova_cidade():
    cidade_nome = request.form['cidade']
    cidade = Cidade(cidade_nome)
    CidadeDao.salvar(cidade)
    return redirect('/novo_imovel')

#bairro
@app.route('/novo_bairro', methods=['POST'])
def novo_bairro():
    cidade = request.form['cidade_bairro']
    bairro_nome = request.form['bairro']
    bairro = Bairro(bairro_nome,cidade)
    BairroDao.salvar(bairro)
    return redirect('/novo_imovel')


#visualização do imovel
@app.route('/view_imovel/<int:id>')
def view_imovel(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=view_imovel/<int:id>')
    imovel = Imovel_Dao.busca_imob_id(id)
    return render_template('view_imovel.html', imovel=imovel)

@app.route('/resumo_imovel/<int:id>')
def resumo_imovel(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=view_imovel/<int:id>')
    imovel = Imovel_Dao.busca_imob_id(id)
    return render_template('resumo_imovel.html', imovel=imovel)

#exclui_imovel
@app.route('/deleta_imovel/<int:id>')
def deleta_imovel(id):
    Imovel_Dao.deletar_imob(id)
    return redirect('/')

@app.route('/filtro/<int:id>')
def filtro(id):
    lista = Imovel_Dao.filtra(id)
    return render_template('lista.html', lista = lista)

#editar_imovel
@app.route('/editar_imovel/<int:id>')
def editar_imovel(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=editar_imovel/id')
    Imovel = Imovel_Dao.busca_imob_id(id)
    lista_prop = Proprietario_dao.listar()
    lista_corr = Corretores_dao.listar()
    lista_tipo = TiposDao.lista()
    lista_cidades = CidadeDao.lista()
    lista_bairro = BairroDao.lista()
    return render_template('editar_imovel.html', imovel=Imovel, proprietarios=lista_prop, corretores=lista_corr,tipos=lista_tipo,cidades=lista_cidades,bairros=lista_bairro)

#padrao mvc
#diego.saqui@muz.ifsuldeminas.edu.br
@app.route('/atualizar_imovel', methods=['POST'])
def atualiza_imovel():
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
    imovel = Imovel(tipo,finalidade,cidade,bairro,endereco,area,descriacao,valor,status,porcentagem ,proprietario,corretor,
                    banheiro=banheiro, quartos=quartos, garagem=garagem, imob_id=id)
    erros = imovel_valida(imovel)
    if erros:
        for e in erros:
            flash(e)
        return redirect(url_for('editar_imovel',id=id))
    else:
        Imovel_Dao.salvar(imovel)
        return redirect('/')

#criar_imovel
@app.route('/novo_imovel')
def novo_imovel():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_imovel')
    lista_prop = Proprietario_dao.listar()
    lista_corr = Corretores_dao.listar()
    lista_tipo = TiposDao.lista()
    lista_cidades = CidadeDao.lista()
    lista_bairro = BairroDao.lista()
    return render_template('novo_imovel.html', proprietarios=lista_prop, corretores=lista_corr,tipos=lista_tipo,cidades=lista_cidades,bairros=lista_bairro)

@app.route('/criar_imovel', methods=['POST'])
def criar_imovel():
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
    imovel = Imovel(tipo,finalidade,cidade,bairro,endereco,area,descriacao,valor,status,porcentagem,proprietario, corretor,
                    banheiro=banheiro,quartos=quartos,garagem=garagem)
    #verfica se os campos foram preenchidos
    erros = imovel_valida(imovel)
    if erros:
        for e in erros:
            flash(e)
        return redirect('/novo_imovel')
    else:
        Imovel_Dao.salvar(imovel)
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
    email = request.form['email']
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
    senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
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
        if bcrypt.hashpw(request.form['senha'].encode(), usuario._senha.encode()) == usuario._senha.encode():
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