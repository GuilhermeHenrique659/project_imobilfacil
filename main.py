from flask import Flask, request, redirect, render_template, session, flash
from models import Imovel, Proprietario, Corretores,Tipo,Cidade,Bairro, Financeiro
from dao import imovelDao, cad_proprietario_dao, cad_corretor_dao,tiposDao,ciadadeDao,bairroDao,financeiroDao
from flask_mysqldb import MySQL
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
FinDao = financeiroDao(db)
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

#financerio
def cria_financeiro(imovel):
    FinDao.pocura_deleta(imovel._imob_id)
    financeiro = Financeiro(imovel.honorarios, 1, imovel._imob_id, imovel._corretor)
    if imovel._status == 'Vendido':
        FinDao.salvar(financeiro)
    else:
        return

@app.route('/financeiro')
def financeiro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=''')
    lista_fin = FinDao.lista()
    return render_template('financeiro.html', financeiros = lista_fin)

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


@app.route('/filtro', methods=['POST'])
def filtro():
    filtro = request.form['filtro']
    id = request.form[filtro]
    lista_imob = Imovel_Dao.filtra(id,filtro)
    if len(lista_imob) == 0:
        flash("Nao foi encontrado nenhum imovel com esse filtro!")
        return redirect('/')
    lista_prop = Proprietario_dao.listar()
    lista_corr = Corretores_dao.listar()
    lista_cidades = CidadeDao.lista()
    return render_template('lista.html', corretores=lista_corr, lista=lista_imob, proprietarios=lista_prop, cidades=lista_cidades)

#exclui_imovel

@app.route('/deleta_imovel/<int:id>')
def deleta_imovel(id):
    Imovel_Dao.deletar_imob(id)
    return redirect('/')

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
    Imovel_Dao.salvar(imovel)
    cria_financeiro(imovel)
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
    id = Imovel_Dao.salvar(imovel)
    imovel.set_id(id)
    cria_financeiro(imovel)
    return redirect('/')

#Criar Proprietario
@app.route('/Proprietario')
def rota_proprietario():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_proprietario.html')
    lista_cidades = CidadeDao.lista()
    lista_bairro = BairroDao.lista()
    return render_template('novo_proprietario.html', cidades=lista_cidades, bairros=lista_bairro)

@app.route('/cad_prop', methods=['POST'])
def criar_proprietario():
    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email = request.form['email']
    cidade = request.form['cidades']
    bairro = request.form['bairros']
    proprietario = Proprietario(nome, cpf, rg, endereco, telefone, email, cidade, bairro)
    Proprietario_dao.salvar(proprietario)
    return redirect('/')
@app.route('/editar_prop/<int:id>')
def editar_proprietario(id):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar_prop.html')
    lista_cidades = CidadeDao.lista()
    lista_bairro = BairroDao.lista()
    proprietario = Proprietario_dao.busca_por_id(id)
    return render_template('editar_prop.html', proprietario=proprietario,cidades=lista_cidades ,bairros=lista_bairro)

@app.route('/atualizar_prop', methods=['POST'])
def atualizar_proprietario():

    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email = request.form['email']
    cidade = request.form['cidades']
    bairro = request.form['bairros']
    id = request.form['id']
    proprietario = Proprietario(nome, cpf, rg, endereco, telefone, email, cidade ,bairro, id)
    Proprietario_dao.salvar(proprietario)
    return redirect('/')
@app.route('/deletar_prop/<int:id>')
def deletar_prop(id):
    Proprietario_dao.deletar_prop(id)
    return redirect('/')
#corretor
@app.route('/Corretor')
def rota_corretor():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=novo_proprietario.html')
    lista_cidades = CidadeDao.lista()
    lista_bairro = BairroDao.lista()
    return render_template('novo_corretor.html',cidades=lista_cidades,bairros=lista_bairro)

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
    cidade = request.form['cidades_corr']
    bairro = request.form['bairros_corr']
    senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
    corretor = Corretores(usuario,email, nome, imobil, creci, celular, cpf, endereco, senha, cidade, bairro)
    Corretores_dao.salvar(corretor)
    return redirect('/')

@app.route('/editar_corretor/<int:id>')
def editar_corretor(id):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar-corr.html')
    lista_cidades = CidadeDao.lista()
    lista_bairro = BairroDao.lista()
    corretor = Corretores_dao.busca_por_id_edit(id)
    return render_template('editar_corr.html', corretor=corretor, cidades=lista_cidades, bairros=lista_bairro)

@app.route('/atualizar_corretor', methods=['POST'])
def atualizar_corretor():
    usuario = request.form['usuario_corr']
    email = request.form['email_corr']
    nome = request.form['nome_corr']
    imobil = request.form['imobil_corr']
    creci = request.form['creci_corr']
    celular = request.form['celular_corr']
    cpf = request.form['cpf_corr']
    endereco = request.form['endereco_corr']
    senha = request.form['senha_corr']
    cidade = request.form['cidades_corr']
    bairro = request.form['bairros_corr']
    id = request.form['id_corr']
    senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
    corretor = Corretores(usuario,email,nome,imobil,creci,celular,cpf,endereco,senha,cidade,bairro,id)
    Corretores_dao.salvar(corretor)
    return redirect('/')

@app.route('/deletar_corr/<int:id>')
def deletar_corr(id):
    Corretores_dao.deletar_corr(id)
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