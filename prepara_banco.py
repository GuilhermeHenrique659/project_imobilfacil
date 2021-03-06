import MySQLdb
import bcrypt
from user import *

print('Conectando...')

#Bancos de dados do Heroku de teste

conn:MySQLdb = MySQLdb.connect(user='b8ab2bd3638752', passwd='7627e7de', host='us-cdbr-east-04.cleardb.com', port=3306, charset='utf8')
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

criar_tabela_cidade = '''CREATE TABLE `CIDADE` (
        `ID_CID` INT NOT NULL AUTO_INCREMENT,
        `CIDADE` VARCHAR(45) NOT NULL UNIQUE,
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
        CONSTRAINT UK_BAIRRO_CIDADE UNIQUE(BAIRRO,CIDADE_ID_CID),
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
        `ID_CIDADE` INT NULL,
        `ID_BAIRRO` INT NULL,
        `CATEGORIA` VARCHAR(45) NOT NULL,
        `FORMA` VARCHAR(25) NOT NULL,
        `LADO_ESQ` INT NOT NULL,
        `LADO_DIR` INT NOT NULL,
        `LADO_FRE` INT NOT NULL,
        `LADO_FUN` INT NOT NULL,
        `TOTAL` INT NOT NULL,
        `TOPOGRAFIA` VARCHAR(45) NOT NULL,
        `AREA_UTIL` INT NOT NULL,
        `CONSTRUIDA` INT NOT NULL,
        `EDICULA` INT NOT NULL,
        `AREA_INFO` TEXT NULL,
        `TIPO` VARCHAR(45) NULL,
        `SUBTIPO` VARCHAR(45) NULL,
        `ENDERECO_IMOVEL` VARCHAR(45) NOT NULL,
        `NUMERO` INT NOT NULL,
        `CEP` VARCHAR(10) NOT NULL,
        `END_INFO` TEXT NULL,
        `PLACA` INT NOT NULL,
        `DATA_PLACA` DATE NULL,
        `DATA_VISITA` DATE NULL,
        `DATA_ULTIMA_VIS` DATE NULL,
        `URL` VARCHAR(255) NULL,
        `COD_ANUNCIO` INT NOT NULL UNIQUE,
        `ANUNCIO_INFO` TEXT NULL,
        `VALOR_IMOVEL` REAL NULL,
        `VALOR_VENDA` REAL NULL,
        `CORRETAGEM` REAL NULL,
        `REPASSE_IMOB` REAL NULL,
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

criar_tabela_casa_descrição = '''CREATE TABLE `IMOVEL_DESC` (
    `ID_DESC` INT NOT NULL AUTO_INCREMENT,
    `ID_IMOB` INT NOT NULL,
    `VAGAS` INT NOT NULL,
    `BANHEIRO` INT NOT NULL,
    `SUITE` INT NOT NULL,
    `DORMITORIOS` INT NOT NULL,
    `AREA_SERVICO` INT NULL,
    `COPA` INT NULL,
    `EDICULA` INT NULL,
    `LAREIRA` INT NULL,
    `PORTAO_ELEC` INT NULL,
    `HIDROMSG` INT NULL,
    `PISO` INT NULL,
    `SACADA` INT NULL,
    `SALA_VIST` INT NULL,
    `SALA_ESTAR` INT NULL,
    `SOTAO` INT NULL,
    `AMARINHO` INT NULL,
    `COZINHA` INT NULL,
    `ESCRITORIO` INT NULL,
    `LAVABO` INT NULL,
    `SALA_JANTAR` INT NULL,
    `VARANDA` INT NULL,
    `CLARABOIA` INT NULL,
    `DEP_EMPREGADA` INT NULL,
    `GARAGE` INT NULL,
    `LIVING_ROOM` INT NULL,
    `QUINTAL` INT NULL,
    `SALA_TV` INT NULL,
    `W_C_EMPREGADA` INT NULL,
    `CLOSET` INT NULL,
    `DESPENSA` INT NULL,
    `CHURRASQUEIRA` INT NULL,
    `PORTARIA_24H` INT NULL,
    `SALAO_FESTA` INT NULL,
    `JD_INVERNO` INT NULL,
    `QUADRA` INT NULL,
    `SAUNA` INT NULL,
    `PISCINA` INT NULL,
    `ENTRADA_INDEP` INT NULL,
    `QUADRA_TENIS` INT NULL,
    `PLAYGROUND` INT NULL,
    `SALA_GINASTICA` INT NULL,
    PRIMARY KEY (`ID_DESC`),
    CONSTRAINT `fk_IMOVEIS_IMOVEL_DESC`
        FOREIGN KEY (`ID_IMOB`)
        REFERENCES `IMOVEIS` (`ID_IMOB`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE=InnoDB;
'''
conn.cursor().execute(criar_tabela_casa_descrição)
conn.commit()


id_auto_increment_start_1000 = '''ALTER TABLE IMOVEIS AUTO_INCREMENT=1000;
    ALTER TABLE CORRETORES AUTO_INCREMENT=1000;
    ALTER TABLE PROPRIETARIOS AUTO_INCREMENT=1000;
'''

conn.cursor().execute(id_auto_increment_start_1000)

# inserindo usuarios
cursor = conn.cursor()
senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
cursor.execute('INSERT INTO CORRETORES ( USUARIO, NOME, EMAIL, SENHA ) VALUES ( %s, %s, %s, %s)', (usuario,nome,email,senha) )

# commitando senão nada tem efeito
print('conexção completa!')
conn.commit()
cursor.close()