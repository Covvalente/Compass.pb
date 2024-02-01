class Ordenadora:

    def __init__(self, lista=[]):
        self.__listaBaguncada = lista
        self.__listaDecrescente = None  # Adiciona a lista decrescente

    @property
    def listaBaguncada(self):
        return self.__listaBaguncada

    @listaBaguncada.setter
    def listaBaguncada(self, nova_lista):
        self.__listaBaguncada = nova_lista

    def ordenacaoCrescente(self):
        self.__listaCrescente = self.__listaBaguncada.copy()
        self.__listaCrescente.sort()
        return self.__listaCrescente

    def ordenacaoDecrescente(self):
        if self.__listaDecrescente is None:
            self.__listaDecrescente = self.__listaBaguncada.copy()
            self.__listaDecrescente.sort(reverse=True)
        return self.__listaDecrescente

# Corrigindo as instâncias das classes e corrigindo nome descrescente para decrescente
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 7])

# Utilizando os métodos corretos
print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
