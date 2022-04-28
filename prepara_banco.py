import MySQLdb
import bcrypt
from user import *

print('Conectando...')

#Bancos de dados do Heroku de teste

conn = MySQLdb.connect(user='b8ab2bd3638752', passwd='7627e7de', host='us-cdbr-east-04.cleardb.com', port=3306, charset='utf8')

#Bancos de dados do Heroku de produção

#conn = MySQLdb.connect(user='bdbbbc8d2b231a', passwd='5deebf3c', host='us-cdbr-east-04.cleardb.com', port=3306, charset='utf8')
# Descomente se quiser desfazer o banco...

conn.cursor().execute("SET NAMES utf8;")
conn.cursor().execute("DROP DATABASE `heroku_7f17bca4c88d1c7`;")
conn.cursor().execute("CREATE DATABASE `heroku_7f17bca4c88d1c7`;")
conn.commit()

'''
conn.cursor().execute("SET NAMES utf8;")
conn.cursor().execute("DROP DATABASE `heroku_405b84a0ef05c35`;")
conn.cursor().execute("CREATE DATABASE `heroku_405b84a0ef05c35`;")
conn.commit()

conn.cursor().execute("USE `heroku_405b84a0ef05c35`;")
'''
conn.cursor().execute("USE `heroku_7f17bca4c88d1c7`;")

criar_tabela_tipo = '''CREATE TABLE `TIPOS` (
        `ID_TIPO` INT NOT NULL AUTO_INCREMENT,
        `TIPO` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`ID_TIPO`)
    ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_tipo)
conn.commit()

criar_tabela_cidade = '''CREATE TABLE `CIDADE` (
        `ID_CID` INT NOT NULL AUTO_INCREMENT,
        `CIDADE` VARCHAR(45) NOT NULL,
        `UF` VARCHAR(2) NULL,
        PRIMARY KEY (`ID_CID`)    
    ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_cidade)
conn.commit()

criar_tabela_bairro = '''CREATE TABLE `BAIRRO` (
        `ID_BAIRRO` INT NOT NULL AUTO_INCREMENT,
        `BAIRRO` VARCHAR(45) NOT NULL,
        `CIDADE_ID_CID` INT NOT NULL,
        PRIMARY KEY (`ID_BAIRRO`, `CIDADE_ID_CID`),
    CONSTRAINT `fk_BAIRRO_CIDADE`
    FOREIGN KEY (`CIDADE_ID_CID`)
    REFERENCES `CIDADE` (`ID_CID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_bairro)
conn.commit()
criar_tabela_corretor = '''CREATE TABLE `CORRETORES` (
        `ID_CORR` INT NOT NULL AUTO_INCREMENT,
        `CODIGO` INT NOT NULL UNIQUE,
        `USUARIO` VARCHAR(45) NOT NULL UNIQUE,
        `EMAIL` VARCHAR(45) NOT NULL UNIQUE,
        `NOME` VARCHAR(45) NULL,
        `CRECI` CHAR(15) NULL,
        `ESTADO_CIVIL` VARCHAR(25) NOT NULL,
        `CPF` CHAR(25) NULL,
        `SEXO` CHAR(1) NOT NULL,
        `NATURALIDADE` VARCHAR(45) NOT NULL,
        `ENDERECO` VARCHAR(45) NULL,
        `NUMERO` INT NOT NULL,
        `DATA_CAD` DATE NOT NULL,
        `TELEFONE` CHAR(25) NULL,
        `CELULAR` CHAR(25) NULL,
        `WHATAPPS` CHAR(25) NULL,
        `FUNCAO` INT NOT NULL,
        `SENHA` VARCHAR(128) NULL,
        PRIMARY KEY (`ID_CORR`),
        `ID_CIDADE` INT NULL,
        `ID_BAIRRO` INT NULL,
    CONSTRAINT `fk_CORRETOR_BAIRRO`
        FOREIGN KEY (`ID_BAIRRO`)
        REFERENCES `BAIRRO` (`ID_BAIRRO`)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT `fk_CORRETOR_CIDADE`
        FOREIGN KEY (`ID_CIDADE`)
        REFERENCES `CIDADE` (`ID_CID`)
        ON DELETE SET NULL
        ON UPDATE CASCADE
   ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_corretor)
conn.commit()

criar_tabela_proprietario = '''CREATE TABLE `PROPRIETARIOS` (
        `ID_PROP` INT NOT NULL AUTO_INCREMENT,
        `CODIGO` INT NOT NULL UNIQUE,
        `PESSOA` INT NOT NULL,
        `NOME` VARCHAR(45) NULL,
        `RAZAO` VARCHAR(45) NULL,
        `CPF_CNPJ` CHAR(25) NULL,
        `RG_INSC_ETAD` VARCHAR(20) NULL,
        `SEXO` CHAR(1) NULL,
        `ENDERECO` VARCHAR(45) NULL,
        `CEP` CHAR(9) NOT NULL,
        `NUMERO` INT NOT NULL,
        `DATA_CAD` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `TELEFONE` CHAR(25) NULL,
        `CELULAR` CHAR(25) NULL,
        `WHATAPPS` CHAR(25) NULL,
        `EMAIL` VARCHAR(45) NULL,
        `CAPITAL` INT NULL,
        `PATRIMONIO` INT NULL,
        `ATIVIDADE` VARCHAR(45) NULL,
        PRIMARY KEY (`ID_PROP`),
        `ID_CIDADE` INT NULL,
        `ID_BAIRRO` INT NULL,
    CONSTRAINT `fk_PROPRIETARIO_BAIRRO`
        FOREIGN KEY (`ID_BAIRRO`)
        REFERENCES `BAIRRO` (`ID_BAIRRO`)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    CONSTRAINT `fk_PROPRIETARIO_CIDADE`
        FOREIGN KEY (`ID_CIDADE`)
        REFERENCES `CIDADE` (`ID_CID`)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_proprietario)
conn.commit()

criar_tabela_imovel = '''CREATE TABLE `IMOVEIS` (
        `ID_IMOB` INT NOT NULL AUTO_INCREMENT,
        `ID_CORR` INT NULL,
        `ID_PROP` INT NULL,
        `ID_TIPO` INT NULL,
        `FINALIDADE` VARCHAR(45) NULL,
        `ID_CIDADE` INT NULL,
        `ID_BAIRRO` INT NULL,
        `ENDERECO_IMOVEL` VARCHAR(45) NULL,
        `AREA` REAL NULL,
        `DETALHES` VARCHAR(512) NULL,
        `VALOR_IMOVEL` REAL NULL,
        `VALOR_VENDA` REAL NULL,
        `STATUS` VARCHAR(45) NULL,
        `PORCENTAGEM` REAL NULL,
        `HONORARIOS` REAL NULL,
        `BANHEIRO` INT NULL,
        `QUARTOS` INT NULL,
        `GARAGEM` INT NULL,
        PRIMARY KEY (`ID_IMOB`),
  CONSTRAINT `fk_IMOVEIS_PROPRIETARIOS`
    FOREIGN KEY (`ID_PROP`)
    REFERENCES `PROPRIETARIOS` (`ID_PROP`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_IMOVEIS_CORRETORES`
    FOREIGN KEY (`ID_CORR`)
    REFERENCES `CORRETORES` (`ID_CORR`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_IMOVEIS_TIPOS`
    FOREIGN KEY (`ID_TIPO`)
    REFERENCES `TIPOS` (`ID_TIPO`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_IMOVEIS_BAIRRO`
    FOREIGN KEY (`ID_BAIRRO`)
    REFERENCES `BAIRRO` (`ID_BAIRRO`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_IMOVEIS_CIDADE`
    FOREIGN KEY (`ID_CIDADE`)
    REFERENCES `CIDADE` (`ID_CID`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_imovel)
conn.commit()

criar_tabela_financeiro = '''CREATE TABLE `FINANCEIRO` (
    `ID_FIN` INT NOT NULL AUTO_INCREMENT,
    `HONORARIOS_CORR` REAL NULL,
    `PORCENTAGEM_CORR` REAL NULL,
    `HONORARIOS_IMOB` REAL NULL,
    `PORCENTAGEM_IMOB` REAL NULL,
    `ID_CORR_FIN` INT NOT NULL,
    `ID_IMOB_FIN` INT NOT NULL,
    PRIMARY KEY (`ID_FIN`,`ID_CORR_FIN`,`ID_IMOB_FIN`),
    CONSTRAINT `fk_FINANCEIRO_CORRETORES`
        FOREIGN KEY (`ID_CORR_FIN`)
        REFERENCES `CORRETORES` (`ID_CORR`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT `fk_FINANCEIRO_IMOVEIS`
        FOREIGN KEY (`ID_IMOB_FIN`)
        REFERENCES `IMOVEIS` (`ID_IMOB`)
        ON DELETE CASCADE
        ON UPDATE CASCADE)
    ENGINE = InnoDB;
'''
conn.cursor().execute(criar_tabela_financeiro)
conn.commit()

# inserindo usuarios
cursor = conn.cursor()
senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
cursor.execute('INSERT INTO CORRETORES ( USUARIO, NOME, EMAIL, SENHA ) VALUES ( %s, %s, %s, %s)', (usuario,nome,email,senha) )

# commitando senão nada tem efeito
print('conexção completa!')
conn.commit()
cursor.close()