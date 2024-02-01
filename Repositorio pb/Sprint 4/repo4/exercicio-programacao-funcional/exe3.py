from functools import reduce 

def calcula_saldo(lancamentos) -> float:
    # usa map para criar uma lista com os valores da tupla, positivos se era 'C' e negativo se 'D'
    lista = list(map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos))
    # retorna a soma de todos os valores da lista gerada
    return reduce(lambda x, y: x+y, lista)