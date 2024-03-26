class Pessoa():
    
    def __init__(self, id, nome=""):
        self.id =id
        self.__nome=nome
    
    @property 
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome
        
        
pessoa = Pessoa(0)
pessoa.nome ='Fulano De Tal'
print(pessoa.nome)