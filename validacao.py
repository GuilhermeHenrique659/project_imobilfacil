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
    #validação dos campos texto
    erro_list.valida_campo_texto(imovel._sigla,'sigla')
    erro_list.valida_campo_texto(imovel._tipo,'tipo')
    erro_list.valida_campo_texto(imovel._bairro,'bairro')
    erro_list.valida_campo_texto(imovel._lote,'lote')
    erro_list.valida_campo_texto(imovel._area,'area')
    erro_list.valida_campo_texto(imovel._valor_imovel,'valor')
    erro_list.valida_campo_texto(imovel._porcentagem,'porcentagem')

    #validação dos campos select
    erro_list.valida_campo_select(imovel._finalidade,'finalidade')
    erro_list.valida_campo_select(imovel._status,'status')
    erro_list.valida_campo_select(imovel._proprietario_id,'proprietario')
    erro_list.valida_campo_select(imovel._corretor_id,'corretor')
    return erro_list.get_erros()