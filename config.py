from flask import Flask,session,redirect,url_for
from flask_mysqldb import MySQL


class Server:
    def __init__(self) -> None:
        self.__app = Flask(__name__)
        self.__app.secret_key='MKTxmcwpZzIrsd3UurhSJjyTwNpD8apQ'
        self.__app.config['MYSQL_HOST'] = '108.179.252.251'
        self.__app.config['MYSQL_USER'] = 'appimo28_admindb'
        self.__app.config['MYSQL_PASSWORD'] = 'admindb123'
        self.__app.config['MYSQL_DB'] = 'appimo28_imobilfacilapp'
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