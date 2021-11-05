class Erros:
    def __init__(self):
        self.__erros = []

    def valida_campo_texto(self,campo,campo_nome):
        if campo == '':
            self.__erros.append('Campo requerido: '+ campo_nome)

    def valida_campo_select(self,campo,campo_nome):
        if campo == "0":
            self.__erros.append('Campo nao selecionado: '+ campo_nome)

    def get_erros(self):
        if len(self.__erros) > 0:
            return self.__erros
        else:
            return None

def imovel_valida(imovel):
    erro_list = Erros()

    erro_list.valida_campo_select(imovel._tipo,'tipo')
    erro_list.valida_campo_select(imovel._cidade,'cidade')
    erro_list.valida_campo_select(imovel._bairro,'bairro')
    erro_list.valida_campo_texto(imovel._endereco,'endereço')
    erro_list.valida_campo_select(imovel._finalidade, 'finalidade')

    erro_list.valida_campo_texto(imovel._valor_imovel,'valor')
    erro_list.valida_campo_texto(imovel._porcentagem,'porcentagem')
    erro_list.valida_campo_select(imovel._status,'status')

    erro_list.valida_campo_select(imovel._proprietario,'proprietario')
    erro_list.valida_campo_select(imovel._corretor,'corretor')

    return erro_list.get_erros()