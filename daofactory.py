from dao import *
from config import server

class DaoFactory:
    def __init__(self) -> None:
        self.__imovel = imovelDao(server.db)
        self.__corretor = CorretorDao(server.db)
        self.__proprietario = ProprietarioDao(server.db)
        self.__cidade = ciadadeDao(server.db)
        self.__bairro = bairroDao(server.db)

    @property
    def imovel(self):
        return self.__imovel

    @property
    def corretor(self):
        return self.__corretor

    @property
    def proprietario(self):
        return self.__proprietario


    @property
    def cidade(self):
        return self.__cidade

    @property
    def bairro(self):
        return self.__bairro


dao = DaoFactory()