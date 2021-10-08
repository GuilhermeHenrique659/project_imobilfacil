import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
'''conn.cursor().execute("DROP DATABASE `jogoteca`;")
conn.commit()'''
conn.cursor().execute("SET NAMES utf8;")
conn.cursor().execute("DROP DATABASE `Projeto_DB`;")
conn.commit()
conn.cursor().execute("CREATE DATABASE `Projeto_DB`;")
conn.commit()

conn.cursor().execute("USE `Projeto_DB`;")
criar_tabela_corretor = '''CREATE TABLE `CORRETORES` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `USUARIO` VARCHAR(45) NOT NULL,
    `EMAIL` VARCHAR(45) NOT NULL,
    `NOME` VARCHAR(45) NOT NULL,
    `NOME DA IMOBIL` VARCHAR(45) NOT NULL,
    `CRECI` CHAR(7) NOT NULL,
    `CELULAR` CHAR(11) NOT NULL,
    `CPF` CHAR(11) NOT NULL,
    `ENDERECO` VARCHAR(45) NOT NULL,
    `SENHA` VARCHAR(75) NOT NULL,
    PRIMARY KEY (`ID`),
    UNIQUE INDEX `USUARIO_UNIQUE` (`USUARIO` ASC),
    UNIQUE INDEX `EMAIL_UNIQUE` (`EMAIL` ASC),
    UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC)
   ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_corretor)
conn.commit()

criar_tabela_proprietario = '''CREATE TABLE `PROPRIETARIOS` (
        `ID` INT NOT NULL AUTO_INCREMENT,
        `NOME` VARCHAR(45) NOT NULL,
        `CPF` CHAR(11) NOT NULL,
        `ENDERECO` VARCHAR(45) NOT NULL,
        `TELEFONE` CHAR(11) NOT NULL,
        PRIMARY KEY (`ID`)
    ) ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_proprietario)
conn.commit()

criar_tabela_imovel = '''CREATE TABLE `IMOVEIS` (
        `ID` INT NOT NULL AUTO_INCREMENT,
        `SINGLA` CHAR(2) NOT NULL,
        `TIPO` VARCHAR(45) NOT NULL,
        `FINALIDADE` VARCHAR(45) NOT NULL,
        `BAIRRO` VARCHAR(45) NOT NULL,
        `QUADRA` VARCHAR(45) NOT NULL,
        `LOTE` VARCHAR(45) NOT NULL,
        `VALOR` REAL NOT NULL,
        `STATUS` VARCHAR(45) NOT NULL,
        `PORCENTAGEM` REAL NOT NULL,
        `HONORARIOS` REAL NOT NULL,
        `PROPRIETARIO_ID` INT NULL,
        PRIMARY KEY (`ID`),
        CONSTRAINT fk_IMOVEL_PROPRIETARIOS FOREIGN KEY (ID) REFERENCES PROPRIETARIOS (ID)
    )ENGINE=InnoDB;'''
conn.cursor().execute(criar_tabela_imovel)
conn.commit()

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO Projeto_DB.PROPRIETARIOS ( NOME, CPF, ENDERECO, TELEFONE) VALUES ( %s, %s, %s, %s)',
      [
          ('teste','12345678912','rua rua123', '35999999999'),
          ('testsae2', '12345678912', 'rua rua343', '35999999999')

      ])

cursor.execute('select * from Projeto_DB.PROPRIETARIOS')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[0])


# commitando senão nada tem efeito
conn.commit()
cursor.close()