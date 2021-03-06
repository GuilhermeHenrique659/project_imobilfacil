from .controller import IndexController
from .CorretorController import CorretorController
from .ImovelController import ImovelController
from .OthersController import OthersController
from .ProprietarioController import ProprietarioController
from .TerrenoController import TerrenoController

class FactoryController:
    def __init__(self) -> None:
        self.__system = IndexController()
        self.__corretor = CorretorController()
        self.__imovel = ImovelController()
        self.__others = OthersController()
        self.__proprietario = ProprietarioController()
        self.__terreno = TerrenoController()

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
    def financeiro(self):
        return self.__financeiro

    @property
    def system(self):
        return self.__system

    @property
    def orthers(self):
        return self.__others

    @property
    def terreno(self):
        return self.__terreno

controllers = FactoryController()