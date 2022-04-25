from .controller import IndexController
from .CorretorController import CorretorController
from .ImovelController import ImovelController
from .FinanceiroController import FinanceiroController
from .OthersController import OthersController
from .ProprietarioController import ProprietarioController


class FactoryController:
    def __init__(self) -> None:
        self.__system = IndexController()
        self.__corretor = CorretorController()
        self.__imovel = ImovelController()
        self.__financeiro = FinanceiroController()
        self.__others = OthersController()
        self.__proprietario = ProprietarioController()

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


controllers = FactoryController()