from flask import Flask,session,redirect,url_for
from flask_mysqldb import MySQL


class Server:
    def __init__(self) -> None:
        self.__app = Flask(__name__)
        self.__app.secret_key='MKTxmcwpZzIrsd3UurhSJjyTwNpD8apQ'
        self.__app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
        self.__app.config['MYSQL_USER'] = 'b8ab2bd3638752'
        self.__app.config['MYSQL_PASSWORD'] = '7627e7de'
        self.__app.config['MYSQL_DB'] = 'heroku_7f17bca4c88d1c7'
        self.__app.config['MYSQL_PORT'] = 3306
        self.__app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        self.__db = MySQL(self.__app)
            
    def loggin_required(self, controller):
        def wrapper(*agrs, **kwargs):
            if 'usuario_logado' not in session or session['usuario_logado'] == None:
                return redirect(url_for('login'))
            return controller(*agrs, **kwargs)
        return wrapper

    def run(self):
        self.__app.run(
            debug=True
        )

    @property
    def app(self):
        return self.__app

    @property
    def db(self):
        return self.__db


server = Server()