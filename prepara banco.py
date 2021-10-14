import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
'''conn.cursor().execute("DROP DATABASE `jogoteca`;")
conn.commit()'''
'''conn.cursor().execute("SET NAMES utf8;")
conn.cursor().execute("DROP DATABASE `Projeto_DB`;")
conn.commit()'''
conn.cursor().execute("CREATE DATABASE `Projeto_DB`;")
conn.commit()

conn.cursor().execute("USE `Projeto_DB`;")
criar_tabela_corretor = '''CREATE TABLE `CORRETORES` (
    `ID_CORR` INT NOT NULL AUTO_INCREMENT,
    `USUARIO` VARCHAR(45) NOT NULL,
    `EMAIL` VARCHAR(45) NULL,
    `NOME` VARCHAR(45) NULL,
    `NOME DA IMOBIL` VARCHAR(45) NULL,
    `CRECI` CHAR(15) NULL,
    `CELULAR` CHAR(25) NULL,
    `CPF` CHAR(25) NULL,
    `ENDERECO` VARCHAR(45) NULL,
    `SENHA` VARCHAR(75) NULL,
    PRIMARY KEY (`ID_CORR`),
    UNIQUE INDEX `USUARIO_UNIQUE` (`USUARIO` ASC),
    UNIQUE INDEX `EMAIL_UNIQUE` (`EMAIL` ASC),
    UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC)
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
        UNIQUE INDEX `EMAIL_UNIQUE` (`EMAIL` ASC)
    ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_proprietario)
conn.commit()

criar_tabela_imovel = '''CREATE TABLE `IMOVEIS` (
        `ID_IMOB` INT NOT NULL AUTO_INCREMENT,
        `ID_CORR` INT NULL,
        `ID_PROP` INT NULL,
        `SINGLA` CHAR(2) NULL,
        `TIPO` VARCHAR(45) NULL,
        `FINALIDADE` VARCHAR(45) NULL,
        `BAIRRO` VARCHAR(45) NULL,
        `QUADRA` VARCHAR(45) NULL,
        `LOTE` VARCHAR(45) NULL,
        `AREA` REAL NULL,
        `DETALHES` VARCHAR(512) NULL,
        `VALOR_IMOVEL` REAL NULL,
        `VALOR_VENDA` REAL NULL,
        `STATUS` VARCHAR(45) NULL,
        `PORCENTAGEM` REAL NULL,
        `HONORARIOS` REAL NULL,
        PRIMARY KEY (`ID_IMOB`),
        CONSTRAINT fk_IMOVEIS_ID_PROP FOREIGN KEY (ID_PROP) REFERENCES PROPRIETARIOS (ID_PROP),
        CONSTRAINT fk_IMOVEIS_ID_CORR FOREIGN KEY (ID_CORR) REFERENCES CORRETORES (ID_CORR)
    )ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_imovel)
conn.commit()

# inserindo usuarios
cursor = conn.cursor()
cursor.execute('INSERT INTO Projeto_DB.CORRETORES ( USUARIO, NOME, EMAIL, SENHA ) VALUES ( %s, %s, %s, %s)', ('guilherme','Guilherme Henrique','teste@gmail.com','123456') )

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