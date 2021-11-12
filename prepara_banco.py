import MySQLdb
import bcrypt
from user import *

print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("SET NAMES utf8;")
#conn.cursor().execute("DROP DATABASE `Projeto_DB`;")
#conn.commit()
conn.cursor().execute("CREATE DATABASE `Projeto_DB`;")
conn.commit()

conn.cursor().execute("USE `Projeto_DB`;")

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
        `USUARIO` VARCHAR(45) NOT NULL,
        `EMAIL` VARCHAR(45) NULL,
        `NOME` VARCHAR(45) NULL,
        `IMOBIL` VARCHAR(45) NULL,
        `CRECI` CHAR(15) NULL,
        `CELULAR` CHAR(25) NULL,
        `CPF` CHAR(25) NULL,
        `ENDERECO` VARCHAR(45) NULL,
        `SENHA` VARCHAR(128) NULL,
        PRIMARY KEY (`ID_CORR`),
        UNIQUE INDEX `USUARIO_UNIQUE` (`USUARIO` ASC),
        UNIQUE INDEX `EMAIL_UNIQUE` (`EMAIL` ASC),
        UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC),
        `ID_CIDADE` INT NULL,
        `ID_BAIRRO` INT NULL,
    CONSTRAINT `fk_CORRETOR_BAIRRO`
        FOREIGN KEY (`ID_BAIRRO`)
        REFERENCES `BAIRRO` (`ID_BAIRRO`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_CORRETOR_CIDADE`
        FOREIGN KEY (`ID_CIDADE`)
        REFERENCES `CIDADE` (`ID_CID`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
   ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_corretor)
conn.commit()

criar_tabela_proprietario = '''CREATE TABLE `PROPRIETARIOS` (
        `ID_PROP` INT NOT NULL AUTO_INCREMENT,
        `NOME` VARCHAR(45) NOT NULL,
        `CPF` CHAR(25) NOT NULL,
        `RG` VARCHAR(20) NOT NULL,
        `ENDERECO` VARCHAR(45) NOT NULL,
        `TELEFONE` CHAR(25) NOT NULL,
        `EMAIL` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`ID_PROP`),
        UNIQUE INDEX `EMAIL_UNIQUE` (`EMAIL` ASC),
        `ID_CIDADE` INT NULL,
        `ID_BAIRRO` INT NULL,
    CONSTRAINT `fk_PROPRIETARIO_BAIRRO`
        FOREIGN KEY (`ID_BAIRRO`)
        REFERENCES `BAIRRO` (`ID_BAIRRO`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_PROPRIETARIO_CIDADE`
        FOREIGN KEY (`ID_CIDADE`)
        REFERENCES `CIDADE` (`ID_CID`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
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
    ON UPDATE CASCADE
    )
ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_imovel)
conn.commit()

# inserindo usuarios
cursor = conn.cursor()
senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
cursor.execute('INSERT INTO Projeto_DB.CORRETORES ( USUARIO, NOME, EMAIL, SENHA ) VALUES ( %s, %s, %s, %s)', (usuario,nome,email,senha) )

cursor.executemany(
      'INSERT INTO Projeto_DB.PROPRIETARIOS ( NOME, CPF, RG, ENDERECO, TELEFONE, EMAIL) VALUES ( %s, %s, %s, %s, %s, %s)',
      [
          ('teste','12345678912','MG123456789','rua rua123', '35999999999','teste@gmail.com'),
          ('testsae2', '12345678912','MG123456489','rua rua343', '35999999999','teste123@gmail.com')

      ])



cursor.execute('select * from Projeto_DB.PROPRIETARIOS')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[0])


# commitando senão nada tem efeito
conn.commit()
cursor.close()