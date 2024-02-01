def conta_vogais(texto:str)-> int:
    vogais = lambda x: x in ['a', 'e', 'i', 'o', 'u']
    # filtra as vogais da string e retorna o tamanho da lista gerada pela filtragem 
    return len(list(filter(vogais, texto.lower())))