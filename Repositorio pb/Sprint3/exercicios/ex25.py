class Aviao():
    # atributo de classe, todas as instancias tem com esse mesmo valor
    cor = "azul"

    # construtor
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.__modelo = modelo
        self.__velocidade_maxima = velocidade_maxima
        self.__capacidade = capacidade
    
    #getters e setter dos atributos
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.modelo = novo_modelo

    @property
    def velocidade_maxima(self):
        return self.__velocidade_maxima
    
    @velocidade_maxima.setter
    def velocidade_maxima(self, nova_velocidade):
        self.velocidade_maxima = nova_velocidade
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self.capacidade = nova_capacidade

# cria uma lista com 3 objetos da classe Aviao
lista = []
lista.append(Aviao("BOIENG456", "1500 km/h", "400"))
lista.append(Aviao("Embraer Praetor 600", "863km/h", "14"))
lista.append(Aviao("Antonov An-2", "258 Km/h", "12"))

# exibe os valores de cada objeto
for i in lista:
    print(f"O avião de modelo {i.modelo} possui uma velocidade máxima de {i.velocidade_maxima}, capacidade para {i.capacidade} passageiros e é da cor {Aviao.cor}")